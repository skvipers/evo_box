from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class GraphicsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.graph_label = QLabel("Graph Layer: 0")
        self.switch_graph_button = QPushButton("Switch Graph Layer")

        layout.addWidget(self.graph_label)
        layout.addWidget(self.switch_graph_button)

        # TODO: Добавить логику переключения слоев графиков

        self.setLayout(layout)
