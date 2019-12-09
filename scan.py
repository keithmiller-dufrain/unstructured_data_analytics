#!/usr/bin/env python3
# import libraries
import os
from os import stat
import datetime as dt
from pwd import getpwuid
import read_directory
import gather_data
import time
from pathlib import Path


# get file creation date
def get_file_creation_date(file_path):
    c = time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(file_path)))
    print('Creation Date '+ c)
    return c


# get file modification date
def get_modification_date(file_path):
    m = time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(file_path)))
    print('Modification Date '+ m)
    return m


# get last accessed
def get_last_accessed_date(file_path):
    a = time.strftime('%d/%m/%Y', time.gmtime(os.path.getatime(file_path)))
    print('Accessed Date '+ a)
    return a


# get file size, this returns in bytes
def get_file_size(file_path):
    s = os.path.getsize(file_path)
    print(s)
    return s


# get file owner/creator
def get_file_owner(file_path):
    o = getpwuid(stat(file_path).st_uid).pw_name
    print(o)
    return o


file_paths = []
# get filename and store it in a variable, do this in other script and read in results?
def get_file_path(directory):
    directory_len = read_directory.list_directory(directory)
    #length = len(directory_len)
    for file in sorted(directory.rglob('*')):
        # for each file in the directory, return the full path for passing into information gathering functions. store in character string 
        file_path = os.path.abspath(file)
        file_paths.append(file_path)

    

def gather_file_info(file_paths):
        print(file_paths)
        for file in range(len(file_paths)):
                get_file_owner(file)
                get_file_size(file)
                get_file_creation_date(file)
                get_modification_date(file)
                get_last_accessed_date(file)

                #print(file_paths)



if __name__ == '__main__':
    get_file_path(Path.cwd())
    gather_file_info('./scan.py')
    



