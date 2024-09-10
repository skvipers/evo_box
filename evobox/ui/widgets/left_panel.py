from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class LeftPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Left Panel Content"))
        self.setLayout(layout)
