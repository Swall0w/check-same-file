# -*- coding: utf-8 -*-
import os
import os.path

def get_file_volume(filedir,filelist):
    return {item : os.path.getsize(filedir+item) for item in filelist}

def check_overlappedfile_by_filesize():
    filedir1 = 'csvdatav1/'
    filedir2 = 'csvdatav2/'
    filelist1 = os.listdir(filedir1)
    filelist2 = os.listdir(filedir2)

    filedict1 = get_file_volume(filedir1,filelist1)
    filedict2 = get_file_volume(filedir2,filelist2)

    for key1, value1 in filedict1.items():
        for key2, value2 in filedict2.items():
            if value1 == value2:
                print("Maybe {file1} in csvdatav1 is duplicated as {file2} in csvdatav2.".format(\
                file1=key1, file2=key2))

if __name__ == '__main__':
    check_overlappedfile_by_filesize()
