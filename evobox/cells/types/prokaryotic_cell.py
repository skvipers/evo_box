from enum import Enum
from evobox.cells.cell import Cell

class ProkaryoticCellShape(Enum):
    COCCUS = "coccus"  # Шарообразная форма
    BACILLUS = "bacillus"  # Палочковидная форма
    SPIRILLUM = "spirillum"  # Спиралевидная форма
    VIBRIO = "vibrio"  # Изогнутая форма (в форме запятой)
    PLEOMORPHIC = "pleomorphic"  # Плеоморфные клетки (меняющие форму)


class ProkaryoticCell(Cell):
    def __init__(self, size, metabolism_rate,
                 shape: ProkaryoticCellShape, logger, position=None):
        # Наследуем базовые свойства из класса Cell
        super().__init__(size, metabolism_rate, position)
        self.has_nucleus = False  # Прокариоты не имеют ядра
        # Прокариоты не имеют мембранных органелл
        self.has_membrane_organelles = False
        # Большинство прокариотов имеют клеточную стенку
        self.has_cell_wall = True
        self.shape = shape  # Устанавливаем форму из перечисления
        self.movement_type = self.determine_movement_type(shape)
        self.logger = logger

    def determine_movement_type(self, shape):
        if shape in [ProkaryoticCellShape.BACILLUS,
                     ProkaryoticCellShape.SPIRILLUM]:
            return "flagellum"
        elif shape == ProkaryoticCellShape.COCCUS:
            return "passive"
        elif shape == ProkaryoticCellShape.VIBRIO:
            return "vibrating"
        else:
            return "unknown"

    def move(self, new_position):
        self.position = new_position
        movement_methods = {
            "flagellum": f"{self.shape.value.capitalize()} is moving using a flagellum.",
            "vibrating": f"{self.shape.value.capitalize()} is moving by vibrating.",
            "passive": f"{self.shape.value.capitalize()} is moving passively."
        }
        if self.movement_type in movement_methods:
            self.logger.debug(movement_methods[self.movement_type])
        else:
            self.logger.debug(
                f"{self.shape.value.capitalize()} has no movement method."
            )

    def divide(self):
        self.logger.debug(
            f"Prokaryotic cell with shape {self.shape.value} is dividing by binary fission."
        )
