from PySide6.QtCore import Signal
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow

class DevToolsWindow(QMainWindow):
    closed = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("DevTools")
        self.resize(1200, 1080)
        self.view = QWebEngineView()
        self.setCentralWidget(self.view)

        self.dev_tools_page = QWebEnginePage()
        self.view.setPage(self.dev_tools_page)

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)
