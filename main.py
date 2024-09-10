import sys
import argparse
from PySide6.QtWidgets import QApplication
#from evolution_runner import run_prokaryotic_evolution
#from distributed_runner import run_distributed_evolution
from evobox.ui.ui import MainWindow

def main():
    #parser = argparse.ArgumentParser(description="Запуск эволюционной симуляции")
    #parser.add_argument('--distributed', action='store_true', help="Запуск в распределённом режиме")
    #args = parser.parse_args()

    #if args.distributed:
        #print("Запуск в распределённом режиме...")
        #run_distributed_evolution()
    #else:
        #print("Запуск локальной симуляции...")
        #run_prokaryotic_evolution()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
