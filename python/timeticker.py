import time

from PySide6.QtCore import QObject, Signal, Property, QTimer


class TimeTicker(QObject):
    tick = Signal(float) # Signalはクラススコープにて定義する必要がある

    def __init__(self, interval_ms):
        super().__init__()
        self._interval_ms = interval_ms

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._on_timeout)

    def _on_timeout(self):
        current_time = time.time() # UNIX時間, float型で秒数
        self.tick.emit(current_time)

    def start(self):
        self._timer.start(self._interval_ms)

    def stop(self):
        if self._timer.isActive():
            self._timer.stop()

    @Property(int)
    def interval_ms(self):
        return self._interval_ms
