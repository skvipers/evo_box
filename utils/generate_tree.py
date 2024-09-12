import os
import argparse
import pyperclip

def generate_tree(root_dir, max_depth, exclude_files, exclude_dirs, prefix=''):
    tree = ''
    if max_depth == 0:
        return tree

    try:
        items = sorted(os.listdir(root_dir))
    except PermissionError:
        return tree

    items = [item for item in items if item not in exclude_files and item not in exclude_dirs]

    pointers = ['├── '] * (len(items) - 1) + ['└── '] if items else []
    for pointer, item in zip(pointers, items):
        path = os.path.join(root_dir, item)
        if os.path.isdir(path):
            if item in exclude_dirs:
                continue
            tree += prefix + pointer + item + os.sep + '\n'
            extension = '│   ' if pointer == '├── ' else '    '
            tree += generate_tree(path, max_depth -1 if max_depth > 0 else -1, exclude_files, exclude_dirs, prefix + extension)
        else:
            if item in exclude_files:
                continue
            tree += prefix + pointer + item + '\n'
    return tree

def main():
    parser = argparse.ArgumentParser(description='Генерация дерева проекта и копирование в буфер обмена.')
    parser.add_argument('root_dir', nargs='?', default='.', help='Корневая директория проекта.')
    parser.add_argument('--depth', type=int, default=-1, help='Максимальная глубина поиска. -1 для полной глубины.')
    parser.add_argument('--exclude-files', nargs='*', default=[], help='Файлы для исключения.')
    parser.add_argument('--exclude-dirs', nargs='*', default=[], help='Папки для исключения.')
    args = parser.parse_args()

    tree = generate_tree(args.root_dir, args.depth, args.exclude_files, args.exclude_dirs)
    print(tree)
    pyperclip.copy(tree)
    print('Дерево проекта скопировано в буфер обмена.')

if __name__ == '__main__':
    main()
