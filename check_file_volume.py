import os
import os.path

def get_file_volume(filedir):
    filedict = {}
    filevolumelist = []
    for item in filelist1:
        filedict[item] = os.path.getsize(filedir+item)
        filevolumelist.append(filedict)
    return filevolumelist

def main():
    filedir1 = 'csvdatav1/'
    filedir2 = 'csvdatav2/'
    filelist1 = os.listdir(filedir1)
    filelist2 = os.listdir(filedir2)

    filedict1 = get_file_volume(filedir1)
    filedict2 = get_file_volume(filedir2)



if __name__ == '__main__':
    main()
