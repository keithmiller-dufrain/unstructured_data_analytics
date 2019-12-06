# import libraries
import os
from os import stat
import datetime as dt
from pwd import getpwuid


# get filename and store it in a variable, do this in other script and read in results?
def get_filename():



# get file creation date
def get_file_creation_date(filename):
    c = os.path.getctime(filename)
    print(dt.datetime.fromtimestamp(c))
    return dt.datetime.fromtimestamp(c)


# get file modification date
def get_modification_date(filename):
    m = os.path.getmtime(filename)
    print(dt.datetime.fromtimestamp(m))
    return dt.datetime.fromtimestamp(m)


# get last accessed
def get_last_accessed_date(filename):
    a = os.path.getatime(filename)
    print(dt.datetime.fromtimestamp(a))
    return dt.datetime.fromtimestamp(a)


# get file size, will need to edit with sizes and make uniform e.g all MB or GB.
def get_file_size(filename):
    s = os.path.getsize(filename)
    print(s)
    return s


# get file owner/creator
def get_file_owner(filename):
    o = getpwuid(stat(filename).st_uid).pw_name
    print(o)
    return o


if __name__ == '__main__':
    get_filename()
    get_file_creation_date()
    get_modification_date()
    get_last_accessed_date()
    get_file_owner()
    get_file_size()



