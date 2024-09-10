import sys
from PySide6.QtWidgets import QApplication
from evobox.ui.ui import MainWindow
from evobox.ui.controller import Controller
from modules.evo_tracker import EvoTracker  # Логгер для отслеживания событий

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создаем главное окно UI
    window = MainWindow()
    window.show()

    # Создаем логгер
    logger = EvoTracker("SimulationLogger")

    # Создаем контроллер и передаем его в UI
    controller = Controller(window, logger)  # Передаем logger в контроллер
    window.set_controller(controller)

    sys.exit(app.exec())
