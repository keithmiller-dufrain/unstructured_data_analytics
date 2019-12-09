#!/usr/bin/env python3
from pathlib import Path
import os


# print directory tree - WORKS
def list_directory(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')




# def function to return full path off all files in the directory, full path will be used for scanning 

if __name__ == '__main__':
    list_directory(Path.cwd())


