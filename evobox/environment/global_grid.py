from modules.position import Point3D
from evobox.environment.local_grid import LocalGrid

class GlobalCell:
    def __init__(self, terrain_type, position: Point3D, entities=None):
        self.terrain_type = terrain_type  # Ландшафт: воздух, вода, земля
        self.position = position  # Позиция в 3D
        self.entities = [] if entities is None else entities  # Существа или объекты в ячейке
        self.local_grid = None  # Локальная сетка для детализированных объектов

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)

    def create_local_grid(self, size):
        """Создаем локальную сетку внутри глобальной ячейки."""
        if not self.local_grid:
            self.local_grid = LocalGrid(size)

class GlobalGrid:
    def __init__(self, width, height, depth):
        # Теперь глобальная сетка работает в 3D (ширина, высота, глубина)
        self.grid = [[[GlobalCell("air", Point3D(x, y, z)) for z in range(depth)] for y in range(height)] for x in range(width)]

    def get_cell(self, x, y, z):
        """Получаем ячейку глобальной сетки по координатам."""
        return self.grid[x][y][z]
