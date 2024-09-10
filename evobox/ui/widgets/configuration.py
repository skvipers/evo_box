from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QFormLayout, QGroupBox, QCheckBox
from PySide6.QtCore import Qt
from evobox.ui.widgets.collapsible_box import CollapsibleBox

import config

class ConfigurationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)  # Устанавливаем выравнивание по верху

        # Коллапсируемый бокс для глобальной сетки
        self.global_grid_box = CollapsibleBox("Global Grid Settings")
        global_form_layout = QFormLayout()

        # Поле ввода для размера глобальной сетки
        self.global_grid_size_input = QLineEdit()
        self.global_grid_size_input.setText(str(config.GLOBAL_GRID_SIZE))  # Пример значения по умолчанию
        global_form_layout.addRow("Global Grid Size:", self.global_grid_size_input)

        # Поле ввода для размера ячеек глобальной сетки
        self.cell_size_global_input = QLineEdit()
        self.cell_size_global_input.setText(str(config.GLOBAL_CELL_SIZE))  # Пример значения по умолчанию
        global_form_layout.addRow("Global Cell Size:", self.cell_size_global_input)

        self.global_grid_box.setContentLayout(global_form_layout)

        # Коллапсируемый бокс для локальной сетки
        self.local_grid_box = CollapsibleBox("Local Grid Settings")
        local_form_layout = QFormLayout()

        # Поле ввода для размера локальной сетки
        self.local_grid_size_input = QLineEdit()
        self.local_grid_size_input.setText(str(config.LOCAL_GRID_SIZE))  # Пример значения по умолчанию
        local_form_layout.addRow("Local Grid Size:", self.local_grid_size_input)

        # Поле ввода для размера ячеек локальной сетки
        self.cell_size_local_input = QLineEdit()
        self.cell_size_local_input.setText(str(config.LOCAL_CELL_SIZE))  # Пример значения по умолчанию
        local_form_layout.addRow("Local Cell Size:", self.cell_size_local_input)

        self.local_grid_box.setContentLayout(local_form_layout)

        # Добавляем коллапсируемые боксы в основной макет
        layout.addWidget(self.global_grid_box)
        layout.addWidget(self.local_grid_box)

        # Кнопка "Continue"
        self.continue_button = QPushButton("Continue")
        layout.addWidget(self.continue_button)

        self.setLayout(layout)

    def get_config(self):
        """Сбор конфигурации из полей ввода"""
        try:
            # Собираем параметры глобальной и локальной сетки
            global_grid_size = int(self.global_grid_size_input.text())
            cell_size_global = int(self.cell_size_global_input.text())
            local_grid_size = int(self.local_grid_size_input.text())
            cell_size_local = int(self.cell_size_local_input.text())

            return {
                "global_grid_size": global_grid_size,
                "cell_size_global": cell_size_global,
                "local_grid_size": local_grid_size,
                "cell_size_local": cell_size_local,
            }
        except ValueError:
            # Обработка некорректного ввода
            return None
