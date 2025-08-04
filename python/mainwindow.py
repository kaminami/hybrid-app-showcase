from PySide6.QtCore import QUrl
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

from timeticker import TimeTicker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hybrid App Showcase")
        self.resize(1900, 1080)

        self.browser = QWebEngineView()

        self._add_menu_bar()

        self._ticker = TimeTicker(1000)  # 1000 ms = 1秒

        self.channel = QWebChannel()
        self.channel.registerObject("ticker", self._ticker)

        self.browser.page().setWebChannel(self.channel)

        self.browser.load(QUrl("http://127.0.0.1:8910/"))  # FastAPIのサーバーが提供するURL
        self.setCentralWidget(self.browser)

        self.start_ticking()

    def _add_menu_bar(self):
        self._add_file_menu()
        self._add_go_menu()

    def _add_file_menu(self):
        menu = self.menuBar().addMenu("File")
        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

    def _add_go_menu(self):
        menu = self.menuBar().addMenu("Go")

        top_action = menu.addAction("Top")
        top_action.triggered.connect(lambda _: self._goto_url("http://127.0.0.1:8910/"))

        menu.addSeparator()  # separator

        external_sites = {"Google": "https://www.google.com/",
                          "Yahoo": "https://www.yahoo.co.jp/",
                          "YouTube": "https://www.youtube.com/"}

        for name, url in external_sites.items():
            action = menu.addAction(name)
            action.triggered.connect(lambda _, u=url: self._goto_url(u))

    def _goto_url(self, url: str):
        self.browser.setUrl(QUrl(url))

    def start_ticking(self):
        self._ticker.tick.connect(lambda ms: print(f"Tick at {ms} ms"))
        self._ticker.start()

    def stop_ticking(self):
        self._ticker.stop()
        self._ticker.tick.disconnect()

