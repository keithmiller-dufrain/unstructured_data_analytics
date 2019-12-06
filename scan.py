# import libraries
import os
from os import stat
import datetime as dt
from pwd import getpwuid

# get filename


# get file creation date
def get_file_creation_date(filename):
    c = os.path.getctime(filename)
    return dt.datetime.fromtimestamp(c)


# get file modification date
def modification_date(filename):
    m = os.path.getmtime(filename)
    return dt.datetime.fromtimestamp(m)


# get file size, will need to edit with sizes and make uniform e.g all MB or GB.
def get_file_size(filename):
    s = os.path.getsize(filename)
    return s

#get file owner/creator
def get_file_owner(filename):
    o = getpwuid(stat(filename).st_uid).pw_name
    return o

if __name__ == '__main__':
    get_file_creation_date()
    get_file_owner()
    get_file_size()


