import re
from pathlib import Path
from typing import List, Dict
import math
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

class SearchEngine:
    def __init__(self):
        self.index = {}
        self.documents = {}
        self.stopwords = set(stopwords.words('french'))
        
    def load_index(self, index: dict, films: dict):
        """Load pre-computed index and film data."""
        self.index = index
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
        print(terms)
        
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
                    op_stack.append(term)
                    print(term)
                else:
                    docs = set(self.index.get(term, {}).keys())
                    result_stack.append(docs)
            
            while op_stack:
                result_stack.append(self._apply_operator(op_stack.pop(), result_stack))
            
            return result_stack[-1] if result_stack else set()
        
        results = evaluate(terms)
        return sorted(list(results))
    
    def _apply_operator(self, op: str, stack: List[set]) -> set:
        print(stack)
        print(op)
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
    
    def vector_search(self, query: str, top_k: int = 5) -> List[tuple]:
        """Perform vector space model search using cosine similarity."""
        query_terms = self.preprocess_text(query)
        if not query_terms:
            return []
            
        # Calculate query vector
        query_vec = Counter(query_terms)
        
        # Calculate document scores
        scores = []
        for doc_id, doc_terms in self.documents.items():
            doc_vec = Counter(doc_terms)
            
            # Calculate cosine similarity
            dot_product = sum(query_vec[term] * doc_vec[term] for term in query_vec)
            query_norm = math.sqrt(sum(freq * freq for freq in query_vec.values()))
            doc_norm = math.sqrt(sum(freq * freq for freq in doc_vec.values()))
            
            if query_norm == 0 or doc_norm == 0:
                similarity = 0
            else:
                similarity = dot_product / (query_norm * doc_norm)
            
            scores.append((doc_id, similarity))
        
        # Sort by score and return top k
        return sorted(scores, key=lambda x: x[1], reverse=True)[:top_k]