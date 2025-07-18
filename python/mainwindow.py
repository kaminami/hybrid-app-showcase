from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hybrid App Showcase")
        self.resize(1900, 1080)

        self.browser = QWebEngineView()
        self.browser.load(QUrl("http://127.0.0.1:8910/"))  # FastAPIのサーバーが提供するURL
        self.setCentralWidget(self.browser)
