from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

class TopPanel(QWidget):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)

        # Статус симуляции
        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)

        # Кнопки управления симуляцией
        self.start_button = QPushButton("Start Simulation")
        self.stop_button = QPushButton("Stop Simulation")
        self.stop_button.setEnabled(False)  # Изначально отключена

        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

        if self.controller:
            self.connect_buttons()

    def connect_buttons(self):
        # Подключаем кнопки к методам контроллера
        self.start_button.clicked.connect(self.controller.start_simulation)
        self.stop_button.clicked.connect(self.controller.stop_simulation)

    def set_controller(self, controller):
        self.controller = controller
        self.connect_buttons()

    def update_status(self, status):
        self.status_label.setText(status)

    def toggle_buttons(self, simulation_running):
        self.start_button.setEnabled(not simulation_running)
        self.stop_button.setEnabled(simulation_running)
