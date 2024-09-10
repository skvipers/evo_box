from PySide6.QtWidgets import QMainWindow, QDockWidget, QTabWidget, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from evobox.ui.widgets.left_panel import LeftPanel
from evobox.ui.widgets.right_panel import RightPanel
from evobox.ui.widgets.top_panel import TopPanel
from evobox.ui.widgets.canvas import CanvasWidget
from evobox.ui.widgets.graphics import GraphicsWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EvoBox UI")

        # Создаем панели
        self.init_docking_panels()

        # Центральный виджет с вкладками
        self.init_central_widget()

    def init_docking_panels(self):
        # Левая панель
        self.left_dock = QDockWidget("Left Panel", self)
        self.left_panel = LeftPanel()
        self.left_dock.setWidget(self.left_panel)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.left_dock)

        # Правая панель
        self.right_dock = QDockWidget("Right Panel", self)
        self.right_panel = RightPanel()
        self.right_dock.setWidget(self.right_panel)
        self.addDockWidget(Qt.RightDockWidgetArea, self.right_dock)

        # Верхняя панель (без докинга)
        self.top_panel = TopPanel(self)
        self.setMenuWidget(self.top_panel)

    def init_central_widget(self):
        # Вкладки для основного окна и графиков
        self.tabs = QTabWidget()
        self.main_tab = CanvasWidget()  # Вкладка с основным канвасом
        self.graphics_tab = GraphicsWidget()  # Вкладка для графиков

        # Добавляем вкладки
        self.tabs.addTab(self.main_tab, "Main")
        self.tabs.addTab(self.graphics_tab, "Graphs")

        # Устанавливаем центральный виджет
        self.setCentralWidget(self.tabs)
