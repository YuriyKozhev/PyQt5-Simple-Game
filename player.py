from unit import Unit


class Player(Unit):
    def __init__(self, start_pos_x: int, start_pos_y: int, path_to_image: str,
                 parent = None, health_points: int = 100) -> None:
        super().__init__(start_pos_x, start_pos_y, path_to_image, parent, health_points)

    def move(self, keys_pressed):
        dx = 0
        dy = 0
        if Qt.Key_Left in keys_pressed:
            dx -= PLAYER_SPEED
        if Qt.Key_Right in keys_pressed:
            dx += PLAYER_SPEED
        if Qt.Key_Up in keys_pressed:
            dy -= PLAYER_SPEED
        if Qt.Key_Down in keys_pressed:
            dy += PLAYER_SPEED
        self.setPos(self.x() + dx, self.y() + dy)