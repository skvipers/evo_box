from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

class TopPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Top Panel"))
        self.setLayout(layout)
