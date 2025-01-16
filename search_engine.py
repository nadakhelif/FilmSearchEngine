import re
from typing import List, Dict, Tuple
import math
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

class SearchEngine:
    def __init__(self):
        self.index = {}
        self.document_lengths = {}
        self.films = {}
        self.documents = {}
        self.stopwords = set(stopwords.words('english'))
       
    def load_index(self, index: dict, document_lengths: dict, films: dict):
        """Load pre-computed index, document lengths and film data."""
        self.index = index
        self.document_lengths = document_lengths
        self.films = films
        # Convert film objects to indexable text for search
        for film_id, film in self.films.items():
            self.documents[film_id] = self.preprocess_text(film.to_text())
   
    def preprocess_text(self, text: str) -> List[str]:
        """Clean and tokenize text."""
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        words = text.split()
        return [w for w in words if w not in self.stopwords]
   
    def boolean_search(self, query: str) -> List[str]:
        """Perform boolean search with AND, OR, NOT operators."""
        query = query.lower()
        terms = re.findall(r'\w+|AND|OR|NOT|\(|\)', query)
        
        def evaluate(terms):
            if not terms:
                return set()
           
            result_stack = []
            op_stack = []
           
            for term in terms:
                if term == '(':
                    op_stack.append(term)
                elif term == ')':
                    while op_stack and op_stack[-1] != '(':
                        result_stack.append(self._apply_operator(op_stack.pop(), result_stack))
                    op_stack.pop()  # Remove '('
                elif term.upper() in ('AND', 'OR', 'NOT'):
                    op_stack.append(term.lower())
                else:
                    # Use the pre-computed index to get matching documents
                    docs = set(self.index.get(term, {}).keys())
                    result_stack.append(docs)
           
            while op_stack:
                result_stack.append(self._apply_operator(op_stack.pop(), result_stack))
           
            return result_stack[-1] if result_stack else set()
       
        results = evaluate(terms)
        return sorted(list(results))
   
    def _apply_operator(self, op: str, stack: List[set]) -> set:
        if op == 'not':
            set1 = stack.pop()
            return set(self.documents.keys()) - set1
        set2 = stack.pop()
        set1 = stack.pop()
        if op == 'and':
            return set1 & set2
        elif op == 'or':
            return set1 | set2
        return set()
   
    def vector_search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """Perform vector space model search using cosine similarity with TF-IDF weights."""
        query_terms = self.preprocess_text(query)
        if not query_terms:
            return []
        
        # Calculate query vector using TF-IDF weights
        query_vec = {}
        query_term_freq = Counter(query_terms)
        num_docs = len(self.documents)
        
        for term, tf in query_term_freq.items():
            if term in self.index:
                # Calculate IDF for query terms
                doc_freq = len(self.index[term])
                idf = math.log10(num_docs / doc_freq) if doc_freq > 0 else 0
                query_vec[term] = tf * idf
        
        # Calculate document scores using pre-computed weights
        scores = []
        for doc_id in self.documents.keys():
            # Calculate dot product using stored TF-IDF weights
            dot_product = 0
            for term, query_weight in query_vec.items():
                if term in self.index and doc_id in self.index[term]:
                    dot_product += query_weight * self.index[term][doc_id]
            
            # Get document length from pre-computed values
            doc_norm = self.document_lengths[doc_id]
            
            # Calculate query vector length
            query_norm = math.sqrt(sum(w * w for w in query_vec.values()))
            
            # Calculate cosine similarity
            if query_norm == 0 or doc_norm == 0:
                similarity = 0
            else:
                similarity = dot_product / (query_norm * doc_norm)
            
            scores.append((doc_id, similarity))
        
        # Sort by score and return top k
        return sorted(scores, key=lambda x: x[1], reverse=True)[:top_k]