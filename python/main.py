import sys

from PySide6.QtWidgets import QApplication, QMainWindow

import webapp
import mainwindow

if __name__ == "__main__":
    # FastAPIサーバーを起動
    webapp.start_server_thread()

    # Qtアプリケーションを起動
    app = QApplication(sys.argv)
    window = mainwindow.MainWindow()
    window.show()
    sys.exit(app.exec())
