import sys

from PySide6.QtWidgets import QApplication

import webapp
from mainwindow import MainWindow

if __name__ == "__main__":
    # FastAPIサーバーを起動
    webapp.start_server_thread()

    # Qtアプリケーションを起動
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
