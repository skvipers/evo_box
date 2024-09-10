class LocalGrid:
    def __init__(self, width, height, depth):
        self.cells = [[[None for _ in range(depth)] for _ in range(height)] for _ in range(width)]

    def add_cell(self, cell, x, y, z):
        """Добавляем клетку в локальную сетку."""
        self.cells[x][y][z] = cell

    def remove_cell(self, x, y, z):
        """Удаляем клетку из локальной сетки."""
        self.cells[x][y][z] = None
