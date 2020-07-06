import zipfile
import os
import re, os.path

def DownLoadFiles(folderId,drive):
    file_list = drive.ListFile(
    {'q': "'"+folderId+"' in parents"}).GetList()

    for f in file_list:
         print('title: %s, id: %s' % (f['title'], f['id']))
         fname = f['title']
         print('downloading to {}'.format(fname))
         f_ = drive.CreateFile({'id': f['id']})
         f_.GetContentFile(fname)


def Unzip(source_Path, dest_Path):
    zip = zipfile.ZipFile(source_Path, 'r')
    zip.setpassword(b"virus")
    for name in zip.namelist():
        if not name.endswith(('/', '\\')):
            with open(os.path.join(dest_Path, os.path.basename(name)), 'wb') as f:
                 f.write(zip.read(name))
    zip.close()


def fileCount(directory):
    count = 0
    d = directory
    for path in os.listdir(d):
        if os.path.isfile(os.path.join(d, path)):
            count += 1
    print(count)



def RemoveFiles(directory):   
    mypath = directory
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))


#-------------------------------- Data Augmentation Functions ----------------------------------------------------------------------------#

def PrepareAugmentedData(trainX,trainY):
    arr1  = np.fliplr(trainX)
    resultX = np.concatenate((trainX,arr1), axis=0)
    resultY = np.concatenate((trainY,trainY), axis=0) 
    return resultX, resultY


