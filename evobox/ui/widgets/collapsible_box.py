from PySide6.QtWidgets import QWidget, QVBoxLayout, QVBoxLayout, QPushButton, QFormLayout
from PySide6.QtCore import QPropertyAnimation, QParallelAnimationGroup

class CollapsibleBox(QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QPushButton(title)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(False)
        self.toggle_button.toggled.connect(self.on_pressed)

        self.toggle_animation = QParallelAnimationGroup(self)

        self.content_area = QWidget()
        self.content_layout = QFormLayout(self.content_area)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

        self.setLayout(lay)

        self.on_pressed(False)

    def on_pressed(self, checked):
        self.toggle_animation.setDirection(QPropertyAnimation.Forward if checked else QPropertyAnimation.Backward)
        self.toggle_animation.start()

    def setContentLayout(self, layout):
        # Удаляем старый layout, если он существует
        if self.content_area.layout():
            QWidget().setLayout(self.content_area.layout())
        
        # Устанавливаем новый layout
        self.content_area.setLayout(layout)
        
        collapsed_height = self.sizeHint().height() - self.content_area.maximumHeight()
        content_height = layout.sizeHint().height()
        
        for i in range(self.toggle_animation.animationCount()-1, -1, -1):
            self.toggle_animation.removeAnimation(self.toggle_animation.animationAt(i))

        content_animation = QPropertyAnimation(self.content_area, b"maximumHeight")
        content_animation.setDuration(100)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)
        self.toggle_animation.addAnimation(content_animation)

        self.toggle_animation.setDirection(QPropertyAnimation.Backward)
        self.toggle_animation.start()
        self.toggle_animation.finished.connect(lambda: self.content_area.setMaximumHeight(content_height if self.toggle_button.isChecked() else 0))
