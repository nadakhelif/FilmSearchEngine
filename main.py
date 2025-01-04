from PyQt5 import QtWidgets
from indexing.indexer import FilmIndexer
from search_engine import SearchEngine
from gui.search_window import SearchWindow
import os

def setup_system():
    # Setup directories
    data_dir = os.path.join(os.path.dirname(__file__), 'data', 'films')
    index_path = os.path.join(os.path.dirname(__file__), 'data', 'index.json')
    
    # Create sample data if needed
    
    from sample_films import create_sample_data
    create_sample_data(data_dir)
    
    # Initialize and run indexer
    indexer = FilmIndexer(data_dir)
    indexer.index_films()
    indexer.save_index(index_path)
    
    return indexer

def main():
    # Setup system
    indexer = setup_system()
    
    # Initialize search engine with index
    search_engine = SearchEngine()
    search_engine.load_index(indexer.index, indexer.films)
    
    # Start GUI
    app = QtWidgets.QApplication([])
    window = SearchWindow(search_engine)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()