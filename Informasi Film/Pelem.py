import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # UI elements
        self.search_lineedit = QtWidgets.QLineEdit()
        self.search_button = QtWidgets.QPushButton("Search")
        self.results_listwidget = QtWidgets.QListWidget()

        # Layouts
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)
        layout.addWidget(self.search_lineedit)
        layout.addWidget(self.search_button)
        layout.addWidget(self.results_listwidget)

        # Signals and slots
        self.search_button.clicked.connect(self.search_movies)
        self.results_listwidget.itemDoubleClicked.connect(self.show_movie_details)

    def search_movies(self):
        # Get search query from line edit
        query = self.search_lineedit.text()
        if not query:
            return

        # Set up API request
        api_key = "2b07d5cdfcaf0776e579d0296067aaf1"
        endpoint = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": api_key,
            "query": query,
            "language": "en-US"
        }
        response = requests.get(endpoint, params=params)

        # Check if request was successful
        if response.status_code != 200:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to fetch movie data")
            return

        # Parse response and display results in list widget
        results = json.loads(response.text)["results"]
        self.results_listwidget.clear()
        for result in results:
            item = QtWidgets.QListWidgetItem(result["title"], self.results_listwidget)
            item.setData(QtCore.Qt.UserRole, result["id"])

    def show_movie_details(self, item):
        # Get movie ID from item data
        movie_id = item.data(QtCore.Qt.UserRole)

        # Set up API request
        api_key = "2b07d5cdfcaf0776e579d0296067aaf1"
        endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "api_key": api_key,
            "language": "en-US"
        }
        response = requests.get(endpoint, params=params)

        # Check if request was successful
        if response.status_code != 200:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to fetch movie data")
            return

        # Parse response and display movie details in a message box
        movie_data = json.loads(response.text)
        message = (
            f"Title: {movie_data['title']}\n"
            f"Release date: {movie_data['release_date']}\n"
            f"Rating: {movie_data['vote_average']}\n"
            f"Duration: {movie_data['runtime']} minutes\n"
            f"Genres: {movie_data['genres']}\n"
            f"Overview: {movie_data['overview']}"
        )
        QtWidgets.QMessageBox.information(self, "Movie Details", message)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


