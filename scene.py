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

from player import Player

import os


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

        # add player to bottom center of scene
        self._create_player()

        # show window with up-to-date scene
        self._show()

    def _create_player(self):
        self._player = Player(start_pos_x=0, start_pos_y=0, 
                              path_to_image=os.path.join("icons", "player_icon.png"))
        player_x_pos: int = SCREEN_WIDTH // 2 - self._player.get_width() // 2
        player_y_pos: int = SCREEN_HEIGHT - self._player.get_height() 
        self._player.setPos(player_x_pos, player_y_pos)
        self.addItem(self._player)
        
    def _draw_background(self):
        bg = QGraphicsRectItem()
        bg.setRect(-1, -1, SCREEN_WIDTH+1, SCREEN_HEIGHT+1)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)

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
        self._player.move(self.keys_pressed)