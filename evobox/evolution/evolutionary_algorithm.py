import random
from modules.evo_tracker import EvoTracker

class EvolutionaryAlgorithm:
    def __init__(self, population, environment, mutation_rate=0.01, logger=None):
        """
        population: список клеток
        environment: условия окружающей среды, влияющие на клетки
        mutation_rate: вероятность мутации
        logger: объект для логирования (опционально)
        """
        self.population = population
        self.environment = environment
        self.mutation_rate = mutation_rate
        self.logger = logger if logger else EvoTracker("Evolution")

    def mutate(self, cell):
        """Мутация клетки."""
        if random.random() < self.mutation_rate:
            self.logger.debug(f"Mutation occurred in cell with shape {cell.shape.value}.")
            # Пример мутации: изменение метаболизма или формы клетки
            mutation_type = random.choice(["metabolism", "shape"])
            if mutation_type == "metabolism":
                cell.metabolism_rate += random.uniform(-0.1, 0.1)  # Изменяем скорость метаболизма
                self.logger.debug(f"New metabolism rate: {cell.metabolism_rate}.")
            elif mutation_type == "shape":
                cell.shape = random.choice(list(cell.shape.__class__))  # Изменение формы
                cell.movement_type = cell.determine_movement_type(cell.shape)
                self.logger.debug(f"New shape: {cell.shape.value}.")

    def evaluate_fitness(self, cell):
        """Оценка приспособленности клетки."""
        # Например, fitness может зависеть от метаболизма и условий окружающей среды
        cell.fitness = cell.metabolism_rate * self.environment["resource_availability"]
        self.logger.debug(f"Cell fitness evaluated: {cell.fitness}.")

    def select_best(self):
        """Отбор клеток с лучшими показателями fitness."""
        # Сортируем клетки по их приспособленности и выбираем лучших
        self.population.sort(key=lambda cell: cell.fitness, reverse=True)
        survivors = self.population[:len(self.population)//2]  # Отбираем лучших 50%
        self.logger.debug(f"{len(survivors)} cells selected for reproduction.")
        return survivors

    def reproduce(self, survivors):
        """Создание нового поколения клеток."""
        offspring = []
        for parent in survivors:
            child = parent.__class__(parent.size, parent.metabolism_rate, parent.shape, self.logger)
            self.mutate(child)  # Мутации могут происходить у потомков
            offspring.append(child)
        self.logger.debug(f"{len(offspring)} offspring created.")
        return offspring

    def evolve(self, generations):
        """Основной цикл эволюции."""
        for generation in range(generations):
            self.logger.debug(f"Generation {generation+1} started.")
            
            # Оцениваем приспособленность каждой клетки
            for cell in self.population:
                self.evaluate_fitness(cell)

            # Отбор лучших клеток
            survivors = self.select_best()

            # Создание нового поколения
            self.population = survivors + self.reproduce(survivors)

            self.logger.debug(f"Generation {generation+1} completed.")
