import zipfile
import os
import re, os.path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score





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
#---------------------------------

def GenerateGraphs(acc, val_acc, loss, val_loss):
     epochs = range(len(acc))
     plt.plot(epochs, acc, 'bo', label='Training accuracy')
     plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
     plt.title('Training and validation accuracy')
     plt.figure()
     plt.plot(epochs, loss, 'bo', label='Training Loss')
     plt.plot(epochs, val_loss, 'b', label='Validation Loss')
     plt.title('Training and validation loss')
     plt.legend()
     plt.show()
     
     
     
def plot_image(i, predictions_array, true_labels, images):
  predictions_array, true_label, img = predictions_array[i], true_labels[i], images[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
   
  plt.imshow(img[...,0], cmap=plt.cm.binary)
 
  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
   
  plt.xlabel("{} {:2.0f}% ({})".format(class_object[predicted_label],
                                100*np.max(predictions_array),
                                class_object[true_label]),
                                color=color)






def averageOfList(num):
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers = sumOfNumbers + t

    avg = sumOfNumbers / len(num)
    return avg









def PrintMetrics(testX, testY, model):
    yhat_probs = model.predict(testX, verbose=0)
    yhat_classes = model.predict_classes(testX, verbose=0)
    accuracy = accuracy_score(testY, yhat_classes)
    precision = precision_score(testY, yhat_classes, average="macro")
    print('Accuracy: %f' % accuracy)
    print('Precision: %f' % precision)
    recall = recall_score(testY, yhat_classes,average="macro")
    print('Recall: %f' % recall)
    f1 = f1_score(testY, yhat_classes,average="macro")
    print('F1 score: %f' % f1)
    kappa = cohen_kappa_score(testY, yhat_classes)
    print('Cohens kappa: %f' % kappa)
 


