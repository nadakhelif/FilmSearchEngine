from PyQt5 import QtWidgets, QtCore, QtGui
from search_engine import SearchEngine

class SearchWindow(QtWidgets.QMainWindow):
    def __init__(self, search_engine: SearchEngine):
        super().__init__()
        self.search_engine = search_engine
        self.setup_ui()
        
    def setup_ui(self):
        self.setWindowTitle("Recherche de Films")
        self.setFixedSize(800, 600)
        
        # Create central widget
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        layout = QtWidgets.QVBoxLayout(central)
        
        # Search controls
        search_layout = QtWidgets.QHBoxLayout()
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setPlaceholderText("Entrer votre recherche...")
        self.search_type = QtWidgets.QComboBox()
        self.search_type.addItems(["Booléen", "Vectoriel"])
        search_btn = QtWidgets.QPushButton("Rechercher")
        
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_type)
        search_layout.addWidget(search_btn)
        
        # Results list
        self.results_list = QtWidgets.QListWidget()
        
        # Add widgets to main layout
        layout.addLayout(search_layout)
        layout.addWidget(self.results_list)
        
        # Connect signals
        search_btn.clicked.connect(self.perform_search)
        self.search_input.returnPressed.connect(self.perform_search)
        
        # Style
        self.setStyleSheet("""
            QMainWindow {
                background-color: white;
            }
            QPushButton {
                background-color: #2596be;
                color: white;
                padding: 5px 15px;
                border: none;
                border-radius: 3px;
            }
            QLineEdit {
                padding: 5px;
                border: 1px solid #2596be;
                border-radius: 3px;
            }
        """)
    
    def perform_search(self):
        query = self.search_input.text()
        search_type = self.search_type.currentText()
        
        self.results_list.clear()
        
        if search_type == "Booléen":
            results = self.search_engine.boolean_search(query)
            for doc_id in results:
                film = self.search_engine.films[doc_id]
                self.results_list.addItem(f"{film.title} ({doc_id})")
        else:
            results = self.search_engine.vector_search(query)
            for doc_id, score in results:
                film = self.search_engine.films[doc_id]
                self.results_list.addItem(f"{film.title} ({doc_id}) - Score: {score:.3f}")