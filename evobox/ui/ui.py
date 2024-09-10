from PySide6.QtWidgets import QMainWindow, QStackedWidget, QTabWidget, QDockWidget, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

# Импортируем виджеты
from evobox.ui.widgets.left_panel import LeftPanel
from evobox.ui.widgets.right_panel import RightPanel
from evobox.ui.widgets.top_panel import TopPanel
from evobox.ui.widgets.canvas import CanvasWidget
from evobox.ui.widgets.graphics import GraphicsWidget
from evobox.ui.widgets.configuration import ConfigurationWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EvoBox UI")

        # Создаем главный виджет с переключаемыми экранами
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Экран конфигурации
        self.config_widget = ConfigurationWidget()
        self.config_widget.continue_button.clicked.connect(self.switch_to_main_interface)

        # Основной интерфейс с панелями
        self.main_interface_widget = QWidget()

        # Добавляем виджеты в стек
        self.stacked_widget.addWidget(self.config_widget)  # Экран конфигурации
        self.stacked_widget.addWidget(self.main_interface_widget)  # Основной интерфейс

        # Отображаем сначала экран конфигурации
        self.stacked_widget.setCurrentWidget(self.config_widget)

        # Инициализируем панели заранее, чтобы избежать ошибки
        self.init_docking_panels()
        self.hide_docking_panels()

    def init_main_interface(self, global_grid_size, cell_size_global, local_grid_size, cell_size_local):
        """Инициализация интерфейса с учетом переданных параметров сетки."""
        self.main_interface_widget_layout = QVBoxLayout(self.main_interface_widget)

        # Вкладки для основного окна и графиков
        self.main_tab = CanvasWidget()  # Вкладка с основным канвасом
        self.graphics_tab = GraphicsWidget()  # Вкладка для графиков

        # Добавляем вкладки
        self.tabs = QTabWidget()
        self.tabs.addTab(self.main_tab, "Main")
        self.tabs.addTab(self.graphics_tab, "Graphs")

        # Добавляем вкладки на основной интерфейс
        self.main_interface_widget_layout.addWidget(self.tabs)

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

        # Верхняя панель (контроллер передадим после его создания)
        self.top_panel = TopPanel(None)  # Передаем None вместо контроллера
        self.setMenuWidget(self.top_panel)

    def hide_docking_panels(self):
        """Скрываем боковые и верхнюю панели."""
        self.left_dock.hide()
        self.right_dock.hide()
        self.top_panel.hide()

    def show_docking_panels(self):
        """Показываем боковые и верхнюю панели."""
        self.left_dock.show()
        self.right_dock.show()
        self.top_panel.show()

    def switch_to_main_interface(self):
        """Переключаемся на основной интерфейс."""
        config = self.config_widget.get_config()
        if config:
            global_grid_size = config["global_grid_size"]
            cell_size_global = config["cell_size_global"]
            local_grid_size = config["local_grid_size"]
            cell_size_local = config["cell_size_local"]

            # Инициализируем основной интерфейс с переданными параметрами
            self.init_main_interface(global_grid_size, cell_size_global, local_grid_size, cell_size_local)

            # Переключаемся на основной интерфейс
            self.stacked_widget.setCurrentWidget(self.main_interface_widget)
            
            # Показываем док-панели
            self.show_docking_panels()

    def set_controller(self, controller):
        """Устанавливаем контроллер для top_panel после его создания."""
        self.top_panel.set_controller(controller)
