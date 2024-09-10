from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class CanvasWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.layer_label = QLabel("Global Layer: 0")
        self.switch_layer_button = QPushButton("Switch Global Layer")

        layout.addWidget(self.layer_label)
        layout.addWidget(self.switch_layer_button)

        # TODO: Добавить логику переключения слоев

        self.setLayout(layout)
