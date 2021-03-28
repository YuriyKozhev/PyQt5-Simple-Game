from movable_object import MovableObject


class Unit(MovableObject):
    def __init__(self, start_pos_x: int, start_pos_y: int, path_to_image: str,
                 parent = None, health_points: int = 100) -> None:
        super().__init__(start_pos_x, start_pos_y, path_to_image, parent)
        self._health_points = health_points
        self._is_alive = True

    def get_health_points(self) -> int:
        return self._health_points
    
    def reduce_health_points(self, damage_points: int) -> None:
        self._health_points -= damage_points
        if self._health_points <= 0:
            self._is_alive = False

