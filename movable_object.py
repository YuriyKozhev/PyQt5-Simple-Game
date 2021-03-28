from PyQt5.QtWidgets import QGraphicsPixmapItem

from PyQt5.QtGui import QPixmap


class MovableObject(QGraphicsPixmapItem):
    def __init__(self, start_pos_x: int, start_pos_y: int, path_to_image: str, parent = None) -> None:
        super().__init__(parent)
        self.setPos(start_pos_x, start_pos_y)
        self._set_icon(path_to_image)

    def _set_icon(self, path_to_image: str) -> None:
        self.setPixmap(QPixmap(path_to_image))

    def get_width(self) -> int:
        return self.pixmap().width()

    def get_height(self) -> int:
        return self.pixmap().height()