import os
import json
from typing import Dict, List
import math
from collections import Counter
from models.film import Film

class FilmIndexer:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.index: Dict[str, Dict[str, float]] = {}  # term -> {doc_id -> weight}
        self.films: Dict[str, Film] = {}
        self.document_lengths: Dict[str, float] = {}
        
    def index_films(self):
        """Index all films in the data directory."""
        # Clear existing index
        self.index.clear()
        self.films.clear()
        
        # Load and index each film
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                film_id = filename[:-5]  # Remove .json extension
                film_path = os.path.join(self.data_dir, filename)
                with open(film_path, 'r', encoding='utf-8') as f:
                    film_data = json.load(f)
                    film = Film(**film_data)
                    self.films[film_id] = film
                    self._index_film(film_id, film)
                    
        # Calculate IDF weights and document lengths
        self._calculate_weights()
    
    def _index_film(self, film_id: str, film: Film):
        """Index a single film."""
        # Get text representation
        text = film.to_text().lower()
        terms = self._tokenize(text)
        
        # Calculate term frequencies
        term_freq = Counter(terms)
        
        # Add to index
        for term, freq in term_freq.items():
            if term not in self.index:
                self.index[term] = {}
            self.index[term][film_id] = freq
    
    def _calculate_weights(self):
        """Calculate TF-IDF weights for all terms."""
        num_docs = len(self.films)
        
        # Calculate IDF for each term
        idfs = {}
        for term, docs in self.index.items():
            idf = math.log10(num_docs / len(docs))
            idfs[term] = idf
            
            # Calculate TF-IDF weight for each document
            for doc_id, tf in docs.items():
                self.index[term][doc_id] = tf * idf
        
        # Calculate document lengths
        for doc_id in self.films.keys():
            length = 0
            for term_index in self.index.values():
                if doc_id in term_index:
                    length += term_index[doc_id] ** 2
            self.document_lengths[doc_id] = math.sqrt(length)
    
    def _tokenize(self, text: str) -> List[str]:
        return text.split()
    
    def save_index(self, index_path: str):
        """Save index to file."""
        index_data = {
            'index': self.index,
            'document_lengths': self.document_lengths
        }
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)
    
    def load_index(self, index_path: str):
        """Load index from file."""
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            self.index = index_data['index']
            self.document_lengths = index_data['document_lengths']