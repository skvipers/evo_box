from PySide6.QtCore import QObject, Signal, QThread
import time

class SimulationThread(QThread):
    # Поток для симуляции
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            # Здесь выполняется логика симуляции
            print(f"Running simulation with config: {self.config}")
            time.sleep(1)  # Имитация работы

    def stop(self):
        self.running = False

class SimulationManager(QObject):
    simulation_started = Signal()
    simulation_stopped = Signal()

    def __init__(self):
        super().__init__()
        self.simulation_thread = None

    def start_simulation(self, config):
        if self.simulation_thread and self.simulation_thread.isRunning():
            print("Simulation already running.")
            return

        self.simulation_thread = SimulationThread(config)
        self.simulation_thread.started.connect(self.on_started)
        self.simulation_thread.finished.connect(self.on_stopped)
        self.simulation_thread.start()

    def stop_simulation(self):
        if self.simulation_thread and self.simulation_thread.isRunning():
            self.simulation_thread.stop()
            self.simulation_thread.wait()
        else:
            print("No simulation is running.")

    def on_started(self):
        print("Simulation has started.")
        self.simulation_started.emit()

    def on_stopped(self):
        print("Simulation has stopped.")
        self.simulation_stopped.emit()
