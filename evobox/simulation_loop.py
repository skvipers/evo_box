class SimulationLoop:
    def __init__(self, population, environment, logger, evolve_interval=10):
        """
        population: список существ или клеток.
        environment: объект среды, с которым взаимодействует популяция.
        logger: объект логирования для отслеживания событий.
        evolve_interval: количество циклов между вызовами эволюции (по умолчанию 10).
        """
        self.population = population
        self.environment = environment
        self.logger = logger
        self.evolve_interval = evolve_interval
        self.current_cycle = 0

    def run_cycle(self):
        """
        Запуск одного цикла симуляции.
        Здесь можно обновлять состояние среды и клеток, запускать эволюцию по расписанию.
        """
        self.logger.debug(f"Running cycle {self.current_cycle}")
        
        # Обновление состояния клеток, метаболизм и прочее
        self.update_population()

        # Проверка, нужно ли запускать эволюцию в этом цикле
        if self.current_cycle % self.evolve_interval == 0:
            self.run_evolution()

        self.current_cycle += 1

    def update_population(self):
        """Обновление состояния каждой клетки в популяции."""
        for cell in self.population:
            cell.metabolize()  # Обновление метаболизма клетки
            # Другие процессы, которые происходят в клетке

    def run_evolution(self):
        """Запуск эволюции для популяции."""
        self.logger.debug("Running evolution")
        # Эволюционный алгоритм
        # Например, вызов EvolutionaryAlgorithm

    def start(self, total_cycles):
        """Запуск симуляции на определённое количество циклов."""
        for _ in range(total_cycles):
            self.run_cycle()
