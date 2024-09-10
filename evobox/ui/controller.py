from PySide6.QtCore import QObject, Signal
from evobox.rendering.grid_renderer import GridRenderer
from evobox.simulation.simulation_loop import SimulationLoop
from evobox.simulation.simulation import Simulation

class Controller(QObject):
    start_signal = Signal()
    stop_signal = Signal()
    update_canvas_signal = Signal()

    def __init__(self, ui, logger):
        super().__init__()
        self.ui = ui
        self.logger = logger
        self.simulation = None
        self.simulation_loop = None

    def start_simulation(self):
        config = self.ui.config_widget.get_config()
        if config:
            global_size = config["global_grid_size"]
            cell_size_global = config["cell_size_global"]
            local_size = config["local_grid_size"]
            cell_size_local = config["cell_size_local"]

            # Инициализируем симуляцию с этими параметрами
            self.simulation = Simulation(global_size, cell_size_global, local_size, cell_size_local)

            # Инициализируем цикл симуляции и передаем обновление канваса через сигнал
            self.simulation_loop = SimulationLoop(self.simulation, self.logger, self.update_canvas)

            self.grid_renderer = GridRenderer(self.simulation.global_grid, cell_size_global, self.ui.right_panel.is_grid_enabled())
            self.ui.main_tab.set_grid(self.simulation.global_grid, cell_size_global)
            self.ui.main_tab.drawing_area.grid_renderer = self.grid_renderer
            # Запуск симуляции
            self.simulation_loop.start()

        self.ui.top_panel.update_status("Simulation Running")
        self.ui.top_panel.toggle_buttons(simulation_running=True)


    def stop_simulation(self):
        if self.simulation_loop:
            self.simulation_loop.stop()
        
        self.ui.top_panel.update_status("Simulation Stopped")
        self.ui.top_panel.toggle_buttons(simulation_running=False)

    def update_canvas(self):
        """Вызывается из симуляционного цикла для обновления отрисовки."""
        self.grid_renderer.show_grid = self.ui.right_panel.is_grid_enabled()
        self.ui.main_tab.drawing_area.update()  # Обновляем область отрисовки
