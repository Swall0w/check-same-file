import os
import os.path

def get_file_volume(filedir,filelist):
    return {item : os.path.getsize(filedir+item) for item in filelist}

def main():
    filedir1 = 'csvdatav1/'
    filedir2 = 'csvdatav2/'
    filelist1 = os.listdir(filedir1)
    filelist2 = os.listdir(filedir2)

    filedict1 = get_file_volume(filedir1,filelist1)
    filedict2 = get_file_volume(filedir2,filelist2)
    print(filedict1)



if __name__ == '__main__':
    main()
