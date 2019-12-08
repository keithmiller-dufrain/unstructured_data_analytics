# import libraries
import os
from os import stat
import datetime as dt
from pwd import getpwuid
import read_directory
import gather_data


# get filename and store it in a variable, do this in other script and read in results?
def get_file_path(directory):
    read_directory.list_directory(directory)
    for file in directory:
        # for each file in the directory, return the full path for passing into information gathering functions

        print(file_path)
        return file_path
        #file_path = ‎⁨'~/Macintosh HD⁩/Users⁩/fraserblack⁩/Desktop⁩/Dufrain⁩/Insight into Unstructured Data.docx'
    

# get file creation date
def get_file_creation_date(file_path):
    c = os.path.getctime(file_path)
    print(dt.datetime.fromtimestamp(c))
    return dt.datetime.fromtimestamp(c)


# get file modification date
def get_modification_date(file_path):
    m = os.path.getmtime(file_path)
    print(dt.datetime.fromtimestamp(m))
    return dt.datetime.fromtimestamp(m)


# get last accessed
def get_last_accessed_date(file_path):
    a = os.path.getatime(file_path)
    print(dt.datetime.fromtimestamp(a))
    return dt.datetime.fromtimestamp(a)


# get file size, will need to edit with sizes and make uniform e.g all MB or GB.
def get_file_size(file_path):
    s = os.path.getsize(file_path)
    print(s)
    return s


# get file owner/creator
def get_file_owner(file_path):
    o = getpwuid(stat(file_path).st_uid).pw_name
    print(o)
    return o




if __name__ == '__main__':
    read_directory.list_directory(Path.cwd())
    get_file_path(directory)
    get_file_creation_date(file_path)
    get_modification_date(file_path)
    get_last_accessed_date(file_path)
    get_file_owner(file_path)
    get_file_size(file_path)



