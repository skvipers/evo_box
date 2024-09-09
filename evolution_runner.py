from evobox.cells.types.prokaryotic_cell import ProkaryoticCell, ProkaryoticCellShape
from evobox.evolution.evolutionary_algorithm import EvolutionaryAlgorithm
from modules.evo_tracker import EvoTracker

def run_prokaryotic_evolution():
    # Логгер для отслеживания эволюции
    logger = EvoTracker("Prokaryotic Evolution", level='DEBUG')

    # Определение среды
    environment = {"resource_availability": 1.0}

    # Создание начальной популяции прокариотических клеток
    population = [
        ProkaryoticCell(size=1.0, metabolism_rate=0.8, shape=ProkaryoticCellShape.BACILLUS, logger=logger),
        ProkaryoticCell(size=0.9, metabolism_rate=0.7, shape=ProkaryoticCellShape.COCCUS, logger=logger),
        ProkaryoticCell(size=1.1, metabolism_rate=0.9, shape=ProkaryoticCellShape.SPIRILLUM, logger=logger),
        ProkaryoticCell(size=0.8, metabolism_rate=0.85, shape=ProkaryoticCellShape.VIBRIO, logger=logger)
    ]

    # Инициализация эволюционного алгоритма
    evolution = EvolutionaryAlgorithm(population, environment, mutation_rate=0.05, logger=logger)

    # Запуск эволюции на 10 поколений
    evolution.evolve(generations=10)
