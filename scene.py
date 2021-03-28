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

from PyQt5.QtGui import (
    QBrush,
    QPixmap,
    QFont,
)

from settings import (
    FRAME_TIME_MS, 
    SCREEN_HEIGHT, 
    SCREEN_WIDTH
)


class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys that are being pressed
        self.keys_pressed = set()

        # use a timer to refresh scene
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        # draw black blackground
        self._draw_background()

    def _draw_background(self):
        bg = QGraphicsRectItem()
        bg.setRect(-1, -1, SCREEN_WIDTH+1, SCREEN_HEIGHT+1)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)
        self._show()

    def _show(self):
        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setSceneRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.update()
        self.game_update()

    def game_update(self):
        pass