from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsTextItem
)

from PyQt5.QtCore import (
    Qt,
    QBasicTimer,
    QUrl
)

from settings import FRAME_TIME_MS


class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys that are being pressed
        self.keys_pressed = set()

        # use a timer to refresh scene
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.update()

    def update(self):
        print("update")