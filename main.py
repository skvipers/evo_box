import argparse
from evolution_runner import run_prokaryotic_evolution
from distributed_runner import run_distributed_evolution

def main():
    parser = argparse.ArgumentParser(description="Запуск эволюционной симуляции")
    parser.add_argument('--distributed', action='store_true', help="Запуск в распределённом режиме")
    args = parser.parse_args()

    if args.distributed:
        print("Запуск в распределённом режиме...")
        run_distributed_evolution()
    else:
        print("Запуск локальной симуляции...")
        run_prokaryotic_evolution()

if __name__ == "__main__":
    main()
