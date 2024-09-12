from PySide6.QtCore import QObject, QTimer

class SimulationLoop(QObject):
    """Отвечает за управление потоком симуляции, временными циклами и обновлениями интерфейса."""
    def __init__(self, simulation, logger, update_canvas_callback, evolve_interval=10):
        """
        simulation: объект симуляции.
        logger: объект логирования для отслеживания событий.
        update_canvas_callback: функция, вызываемая для обновления интерфейса.
        evolve_interval: количество циклов между вызовами эволюции.
        """
        super().__init__()
        self.simulation = simulation
        self.logger = logger
        self.update_canvas_callback = update_canvas_callback
        self.evolve_interval = evolve_interval
        self.current_cycle = 0
        self.running = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.run_cycle)

    def start(self):
        """Запускает симуляцию."""
        self.running = True
        self.timer.start(1000 / 60)  # Запуск с частотой 60 FPS

    def stop(self):
        """Останавливает симуляцию."""
        self.running = False
        self.timer.stop()

    def run_cycle(self):
        """Запуск одного цикла симуляции."""
        if not self.running:
            return

        self.logger.debug(f"Running cycle {self.current_cycle}")

        # Обновляем популяцию
        self.simulation.update_population()

        # Проверяем, нужно ли запустить эволюцию
        if self.current_cycle % self.evolve_interval == 0:
            self.simulation.run_evolution()

        # Обновляем интерфейс (перерисовываем канвас)
        self.update_canvas_callback()

        self.current_cycle += 1
