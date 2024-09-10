from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QFrame, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter

from evobox.rendering.grid_renderer import GridRenderer

class CanvasWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = None  # Сетка будет установлена позже
        self.cell_size = 0
        self.current_layer = 0  # Изначально выбранный слой

        #self.grid_renderer = None  # Рендерер будет создан позже
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout(self)

        # Панель для переключения слоев (Z) с прокруткой
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedWidth(100)
        self.layer_panel = QWidget()
        self.layer_panel_layout = QVBoxLayout(self.layer_panel)

        self.scroll_area.setWidget(self.layer_panel)

        # Область отрисовки
        self.drawing_area = DrawingArea()

        # Устанавливаем политику изменения размера
        self.drawing_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        main_layout.addWidget(self.drawing_area)
        main_layout.addWidget(self.scroll_area)

        self.setLayout(main_layout)

    def set_grid(self, grid, cell_size):
        """Устанавливаем сетку и параметры после старта симуляции."""
        self.grid = grid
        self.cell_size = cell_size
        #self.grid_renderer = GridRenderer(self.grid, self.cell_size, show_grid=True)
        #self.drawing_area.grid_renderer = self.grid_renderer

        # Обновляем панель с кнопками переключения слоев
        self.update_layer_buttons()

    def update_layer_buttons(self):
        """Обновляем кнопки для переключения слоев на основе новой сетки."""
        # Очищаем старые кнопки
        for i in reversed(range(self.layer_panel_layout.count())):
            widget = self.layer_panel_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Добавляем новые кнопки для слоев
        if self.grid:
            for i in range(len(self.grid)):  # Создаем кнопки на основе количества слоев
                button = QPushButton(f"Layer {i+1}")
                button.clicked.connect(lambda _, i=i: self.switch_layer(i))
                self.layer_panel_layout.addWidget(button)

        self.drawing_area.update()

    def switch_layer(self, layer_index):
        """Переключение слоя."""
        self.current_layer = layer_index
        self.drawing_area.set_layer(layer_index)
        self.drawing_area.update()


class DrawingArea(QFrame):
    def __init__(self):
        super().__init__()
        self.grid_renderer = None
        self.current_layer = 0

    def set_layer(self, layer_index):
        """Обновляем текущий слой для отрисовки."""
        self.current_layer = layer_index

    def paintEvent(self, event):
        if self.grid_renderer is not None:
            painter = QPainter(self)

            # Рисуем сетку для текущего слоя
            self.grid_renderer.render(painter, self.current_layer)
