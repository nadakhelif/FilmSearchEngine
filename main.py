from PyQt5 import QtWidgets
from indexing.indexer import FilmIndexer
from models.film import Film
from search_engine import SearchEngine
from gui.search_window import SearchWindow
import os
import json
"""def setup_system():
    # Setup directories
    tsv_filepath = "filtered_final_movies_3.tsv" 
    data_dir = os.path.join(os.path.dirname(__file__), 'data', 'films')
    index_path = os.path.join(os.path.dirname(__file__), 'data', 'index.json')
    
    # Create sample data if needed
    
    ##from sample_films import create_film_files_from_tsv
    ##create_film_files_from_tsv(tsv_filepath,data_dir)
    
    # Initialize and run indexer
    # indexer = FilmIndexer(data_dir)
    # indexer.index_films()
    # indexer.save_index(index_path)
    
    with open(index_path, 'r') as f:
        index_data = json.load(f)
    
    # Assuming the index file contains both the index and films data
    index = index_data.get('index', {})
    films = index_data.get('films', {})

    return index, films """

def setup_system():
    # Setup directories
    data_dir = os.path.join(os.path.dirname(__file__), 'data', 'films')
    index_path = os.path.join(os.path.dirname(__file__), 'data', 'index.json')
   
    # Load the pre-computed index with UTF-8 encoding
    with open(index_path, 'r', encoding='utf-8') as f:  # Added encoding='utf-8'
        index_data = json.load(f)
    
    # Get index and document lengths from the saved data
    index = index_data.get('index', {})
    document_lengths = index_data.get('document_lengths', {})
    
    # Load film data
    films = {}
    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            film_id = filename[:-5]
            with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
                film_data = json.load(f)
                films[film_id] = Film(**film_data)
    
    return index, document_lengths, films
def main():
    # Setup system
    index, document_lengths, films = setup_system()
   
    # Initialize search engine with index
    search_engine = SearchEngine()
    search_engine.load_index(index, document_lengths, films)
    
    # Start GUI
    app = QtWidgets.QApplication([])
    window = SearchWindow(search_engine)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()