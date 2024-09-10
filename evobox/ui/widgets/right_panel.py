from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox
from evobox.ui.widgets.collapsible_box import CollapsibleBox  # Импортируем CollapsibleBox

class RightPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Основной layout
        layout = QVBoxLayout()

        # Добавляем CollapsibleBox для отрисовки сетки
        grid_box = CollapsibleBox("Grid Options")
        
        # Добавляем чекбокс для включения/выключения отрисовки сетки
        self.grid_checkbox = QCheckBox("Show Grid")
        self.grid_checkbox.setChecked(True)  # По умолчанию сетка включена
        
        # Добавляем чекбокс в CollapsibleBox
        grid_box.content_layout.addWidget(self.grid_checkbox)
        
        # Добавляем CollapsibleBox в основной layout
        layout.addWidget(grid_box)
        
        # Добавляем текст для примера
        layout.addWidget(QLabel("Right Panel Content"))

        self.setLayout(layout)

    def is_grid_enabled(self):
        """Метод для получения состояния чекбокса (включена ли отрисовка сетки)"""
        return self.grid_checkbox.isChecked()
