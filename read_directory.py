#!/usr/bin/env python3

from pathlib import Path
import os


# print directory tree
def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')


def list_directory(path):
    p = Path(path)
    print(p)
    list(p.glob('*.py'))


if __name__ == '__main__':
    tree()
    list_directory('.')
