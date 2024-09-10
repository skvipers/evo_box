from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class RightPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Right Panel Content"))
        self.setLayout(layout)
