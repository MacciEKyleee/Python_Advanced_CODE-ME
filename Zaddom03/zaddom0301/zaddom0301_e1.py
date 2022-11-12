# Maciej Cieszyński
import os.path

def strip_extensions(files):

    #files = [str(s).rsplit(".")[0] for s in files]
    files = [os.path.splitext(str(s))[0] for s in files if str(s)!='None']

    return files

if __name__ == '__main__':
    files = ['spreadsheet.xlsx', 'music.mp3', 'backup.log', None, 'temp', 'archive.tar.gz']

    print(strip_extensions(files))
