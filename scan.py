#!/usr/bin/env python3
# import libraries
import os
import time
import ast
import read_directory
import datetime as dt
from os import stat
from pwd import getpwuid
from pathlib import Path


# get file creation date
def get_file_creation_date(file_path):
        c = time.strftime('%d/%m/%Y', time.gmtime(os.path.getctime(file_path)))
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
        print('Owner '+ o)
        return o


def get_filename(file_path):
        f = os.path.basename(file_path)
        print('Filename '+ f)
        return f


file_paths = []
# get filename and store it in a variable, do this in other script and read in results?
def get_file_path(directory):
        directory_len = read_directory.list_directory(directory)
        #length = len(directory_len)
        for file in sorted(directory.rglob('**/*py')):
                # for each file in the directory, return the full path for passing into information gathering functions. store in character string 
                file_path = os.path.abspath(file)
                file_paths.append(file_path)
        print("\n".join(file_paths))
        print(file_paths)
        return file_paths
       
    

def gather_file_info(file_paths):
        #print(file_paths)
        n = range(len(file_paths))
        print(n)
        for file in range(len(file_paths)):
                fil = get_filename(str(file_paths[file]))
                own = get_file_owner(file_paths[file])
                siz = get_file_size(file_paths[file])
                cre = get_file_creation_date(file_paths[file])
                mod = get_modification_date(file_paths[file])
                acc = get_last_accessed_date(file_paths[file])
                create_dictionary(fil, own, siz, cre, mod, acc)
                

        #print("\n".join(file_paths))


def create_dictionary(filename,owner,size,modification,creation,accessed):
        keys = ["filename","owner", "size", "creation_date", "modification_date", "accessed_date"]
        values = [filename, owner, size, modification, creation, accessed]
        mydict = dict(zip(keys, values))
        print(mydict.keys())
        create_sql_statement(mydict)


def create_sql_statement(mydict):
        for dict in mydict:
                placeholders = ', '.join(['%s'] * len(dict))
                columns = ', '.join("" + str(x).replace('/', '_') + "" for x in mydict.keys())
                values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
                sql = "INSERT INTO %s  (%s)  VALUES  (%s) ;" % ('test_table', columns, values)


                print(sql)
                f = open("./test.sql", "a")
                f.write(sql + '\n')
                return sql


if __name__ == '__main__':
    get_file_path(Path.cwd())
    gather_file_info(file_paths)
