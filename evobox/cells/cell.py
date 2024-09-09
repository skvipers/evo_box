from modules.evo_tracker import EvoTracker as evo_tracker


class Cell:
    def __init__(self, size, metabolism_rate):
        self.size = size  # Размер клетки в микрометрах
        self.has_membrane = True  # Все клетки имеют мембрану
        self.has_cytoplasm = True  # Все клетки содержат цитоплазму
        self.has_ribosomes = True  # Рибосомы есть у всех клеток
        self.metabolism_rate = metabolism_rate  # Базовый метаболический индекс
        self.shape = "undefined"  # Форма клетки по умолчанию не определена

    def absorb_nutrients(self, amount):
        # Логика поглощения питательных веществ
        evo_tracker.cell_logger.debug(
            f"Cell absorbs {amount} units of nutrients."
        )

    def divide(self):
        # Логика деления клетки (например, митоз)
        evo_tracker.cell_logger.debug("Cell is dividing.")

    def synthesize_proteins(self):
        # Логика синтеза белков
        evo_tracker.cell_logger.debug("Cell is synthesizing proteins.")

    def metabolize(self):
        # Процесс метаболизма (поглощение энергии и выделение отходов)
        evo_tracker.cell_logger.debug(
            "Cell with metabolism rate {self.metabolism_rate} is metabolizing."
        )

    def die(self):
        # Логика смерти клетки
        evo_tracker.cell_logger.debug("Cell has died.")
