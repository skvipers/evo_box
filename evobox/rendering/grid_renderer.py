from PySide6.QtCore import Qt

class GridRenderer:
    def __init__(self, grid, cell_size, show_grid=False):
        """
        grid: структура данных для хранения информации о сетке (например, список списков)
        cell_size: размер одной ячейки сетки
        show_grid: флаг для отображения сетки
        """
        self.grid = grid
        self.cell_size = cell_size
        self.show_grid = show_grid

    def render(self, painter, current_layer):
        """
        Отрисовка заданного слоя сетки (Z).
        painter: объект QPainter для отрисовки.
        current_layer: индекс текущего слоя Z для отрисовки.
        """
        if not self.show_grid:
            return  # Если сетка не отображается, выходим из метода

        # Проверяем, есть ли текущий слой в сетке
        if current_layer < len(self.grid):
            layer = self.grid[current_layer]

            grid_size = len(layer)
            for i in range(grid_size):
                for j in range(grid_size):
                    x = i * self.cell_size
                    y = j * self.cell_size

                    # Например, заполняем ячейки разными цветами в зависимости от содержимого
                    if layer[i][j] is not None:
                        painter.setBrush(Qt.blue)  # Можно настраивать цвет
                    else:
                        painter.setBrush(Qt.white)
                    if self.show_grid:
                        painter.drawRect(x, y, self.cell_size, self.cell_size)
