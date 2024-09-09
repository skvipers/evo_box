class EvoTracker:
    levels = {
        'DEBUG': 10,
        'INFO': 20,
        'SHORT_INFO': 30,
        'WARNING': 40,
        'ERROR': 50,
        'CRITICAL': 60,
    }

    def __init__(self, channel_name, level='INFO'):
        self.channel_name = channel_name
        self.level = level
        self.logs = []

    def set_level(self, level):
        if level in EvoTracker.levels:
            self.level = level
        else:
            raise ValueError(f"Invalid log level: {level}")

    def log(self, message, level='INFO'):
        if EvoTracker.levels[level] >= EvoTracker.levels[self.level]:
            self.logs.append(f"[{level}] [{self.channel_name}] {message}")
            print(f"[{level}] [{self.channel_name}] {message}")

    def debug(self, message):
        self.log(message, level='DEBUG')

    def info(self, message):
        self.log(message, level='INFO')

    def short_info(self, message):
        self.log(message, level='SHORT_INFO')

    def warning(self, message):
        self.log(message, level='WARNING')

    def error(self, message):
        self.log(message, level='ERROR')

    def critical(self, message):
        self.log(message, level='CRITICAL')

    def get_logs(self):
        return self.logs


# Создаем несколько логгеров для разных каналов
cell_logger = EvoTracker('Cell', level='INFO')
environment_logger = EvoTracker('Environment', level='INFO')

