# -*- coding: utf-8 -*-
import os
import os.path
import hashlib

def add_file_value(func,filedir):
    return {item : func(filedir+item) for item in os.listdir(filedir)}

def get_filesize(filepath):
    return os.path.getsize(filepath)

def get_file_md5(filepath):
    md5 = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(2048 * md5.block_size), b''):
            md5.update(chunk)
    return  md5.hexdigest()

def check_overlappedfile_by_filesize():
    filedir1 = 'csvdatav1/'
    filedir2 = 'csvdatav2/'

    filedict1 = add_file_value(get_file_md5, filedir1)
    filedict2 = add_file_value(get_file_md5, filedir2)

    for key1, value1 in filedict1.items():
        for key2, value2 in filedict2.items():
            if value1 == value2:
                print("Maybe {file1} in csvdatav1 is duplicated as {file2} in csvdatav2.".format(\
                file1=key1, file2=key2))
                os.remove(filedir2+key2)

if __name__ == '__main__':
    check_overlappedfile_by_filesize()
