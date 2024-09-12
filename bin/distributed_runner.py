from evobox.cells.types.prokaryotic_cell import ProkaryoticCell, ProkaryoticCellShape
from evobox.evolution.evolutionary_algorithm import EvolutionaryAlgorithm
from modules.evo_tracker import EvoTracker
import dask
from dask.distributed import Client

# Настройка распределённых вычислений
client = Client(processes=True)  # Локальный клиент для распределения задач на нескольких ядрах
# Или для удалённого кластера: client = Client("tcp://scheduler-address:8786")

def run_distributed_evolution():
    logger = EvoTracker("Prokaryotic Evolution")

    # Среда
    environment = {"resource_availability": 1.0}

    # Создание популяции клеток
    population = [
        ProkaryoticCell(size=1.0, metabolism_rate=0.8, shape=ProkaryoticCellShape.BACILLUS, logger=logger),
        ProkaryoticCell(size=0.9, metabolism_rate=0.7, shape=ProkaryoticCellShape.COCCUS, logger=logger),
        ProkaryoticCell(size=1.1, metabolism_rate=0.9, shape=ProkaryoticCellShape.SPIRILLUM, logger=logger),
        ProkaryoticCell(size=0.8, metabolism_rate=0.85, shape=ProkaryoticCellShape.VIBRIO, logger=logger)
    ]

    # Параллельная оценка fitness для каждой клетки
    @dask.delayed
    def calculate_cell_fitness(cell):
        return cell.evaluate_fitness()

    fitness_tasks = [calculate_cell_fitness(cell) for cell in population]
    dask.compute(*fitness_tasks)

    # Запуск эволюции
    evolution = EvolutionaryAlgorithm(population, environment, mutation_rate=0.05, logger=logger)
    evolution.evolve(generations=10)
