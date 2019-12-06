# import libraries
import os
import datetime as dt

# get filename


# get file creation date
def get_file_creation_date(filename):
    c = os.path.getctime(filename)
    return dt.datetime.fromtimestamp(c)


# get file modification date
def modification_date(filename):
    m = os.path.getmtime(filename)
    return dt.datetime.fromtimestamp(m)


# get file size
def get_file_size(filename):


#get file owner/creator
def get_file_owner(filename):