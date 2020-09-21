"""
See readme for information about this file.
Ethoflow: computer vision and artificial intelligence-based software for automatic behavior analysis
v 1.0

DOI: 10.1101/2020.07.23.218255
LicenseCC BY-NC-ND 4.0

@developer: Rodrigo Cupertino Bernardes
https://www.researchgate.net/profile/Rodrigo_Cupertino_Bernardes
"""


import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import to_categorical

from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import BatchNormalization
#from keras.constraints import maxnorm
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D

#from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import pickle
import cv2
import os
import random

from tensorflow.keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping

#matrix confusion
import itertools


def getdata (classes,pathbehavior,pathnonbehavior):

    behavior =pathbehavior
    non_behavior =pathnonbehavior
    
   
    
    # grab the image paths and randomly shuffle them
    imagePaths = sorted(behavior + non_behavior)
    #random.seed(42)
    random.shuffle(imagePaths)
    
    
    # initialize the data and labels
    data = []
    labels = []
    # loop over the input images
    for imagePath in (imagePaths):
          
        # load the image, pre-process it, and store it in the data list
        image = cv2.imread('data/'+imagePath)
        #print(image)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        #print(imagePath)
        image = cv2.resize(image, (124, 124))
        
        image = img_to_array(image)
        data.append(image)
        # extract the class label from the image path and update the
        # labels list
        #l = label = imagePath.split(os.path.sep)[-2].split("_")
      
        #labels.append(l)
        
        #labels
       
        label = os.path.split(imagePath)[0]    #imagePath.split(os.path.sep)[0]
         
        if label == "behavior": label=0
        elif label == "non_behavior": label=1  
        else : pass
        labels.append(label)
      
      
      
      
    # scale the raw pixel intensities to the range [0, 1]
    data = np.array(data, dtype="float") / 255.0
    labels = np.array(labels)
    
    #lb = LabelBinarizer()
    #labels = lb.fit_transform(labels)
    
    #lb = LabelBinarizer()
    #labels_strat= lb.fit_transform(labels)
    
    (testX, trainX, testY, trainY) = train_test_split(data, labels, test_size=0.7,  random_state= 10)#stratify= labels_strat,
    
    
    # convert the labels from integers to vectors
    trainY = to_categorical(trainY, num_classes=classes)# num_classes é de acordo com o n de classes
    testY = to_categorical(testY, num_classes=classes)
    
    return (testX, trainX, testY, trainY)


def run_network (model_path,model_history,testX, trainX, testY, trainY):
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape=(124,124,3), activation='elu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(32, (3,3), activation='elu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(32, (3,3), activation='elu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    
    model.add(Dense(128, activation='elu'))
    model.add(Dropout(0.2))
    model.add(Dense(128, activation='elu'))
    model.add(Dropout(0.2))  
    model.add(Dense(2, activation='sigmoid'))
    
    model.compile(optimizer=SGD(lr=0.0001, momentum=0.9)  , loss='binary_crossentropy',metrics=['acc'])
    
    model.summary()
    
    
    ########
    
    aug = ImageDataGenerator(rotation_range=14, width_shift_range=0.06,
                         height_shift_range=0.06, shear_range=0.01, zoom_range=0.06,
                         horizontal_flip=True, fill_mode="nearest")

    checkpoint = ModelCheckpoint(model_path, monitor='val_acc', verbose=1, save_best_only=True,
                                 save_weights_only=False, mode='auto', period=1)
    early = EarlyStopping(monitor='val_acc', min_delta=0, patience=15, verbose=1, mode='auto')
    
    H = model.fit_generator(aug.flow(trainX, trainY,batch_size=5), validation_data=(testX, testY),
                            steps_per_epoch=int(len(trainX)/3),epochs = 100, verbose=1 ,callbacks =[checkpoint, early])
    
    
    
    
    
    # save:
    f = open(model_history, 'wb')
    pickle.dump(H.history, f)
    f.close()
    
    f = open(model_history, 'rb')
    model_history = pickle.load(f)
    f.close()
    
    plt.figure(figsize=(11,6))

    plt.rcParams["font.size"] = "16"
    plt.plot((model_history['acc']), linestyle='-', marker='o', color='m',markersize=9, linewidth=3 ,label='Training accuracy')
    plt.plot((model_history['val_acc']), linestyle='dashed', marker='o', color='limegreen', markersize=9,linewidth=3 ,label='Validation accuracy')
    
    
    plt.plot((model_history['loss']), linestyle='-', marker='s', color='m', markersize=9 ,linewidth=3 ,label='Training loss')
    plt.plot((model_history['val_loss']), linestyle='--', marker='s', color='limegreen', markersize=9 ,linewidth=3 ,label='Validation loss')
    
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy and Loss')
    
    #plt.ylim((0, 0.95))
    #plt.ylim(top=1)
    #plt.xlim((0, 76))
    
    #plt.title('')
    plt.legend(fontsize=14,loc=(1.04,0.5))
    plt.tight_layout() # para sair a figura toda
    plt.show
    

def plot_history(model_history):
       
    f = open(model_history, 'rb')
    model_history = pickle.load(f)
    f.close()
    
    plt.figure(figsize=(11,6))

    plt.rcParams["font.size"] = "16"
    plt.plot((model_history['acc']), linestyle='-', marker='o', color='m',markersize=9, linewidth=3 ,label='Training accuracy')
    plt.plot((model_history['val_acc']), linestyle='dashed', marker='o', color='limegreen', markersize=9,linewidth=3 ,label='Validation accuracy')
    
    
    plt.plot((model_history['loss']), linestyle='-', marker='s', color='m', markersize=9 ,linewidth=3 ,label='Training loss')
    plt.plot((model_history['val_loss']), linestyle='--', marker='s', color='limegreen', markersize=9 ,linewidth=3 ,label='Validation loss')
    
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy and Loss')
    
    #plt.ylim((0, 0.95))
    #plt.ylim(top=1)
    #plt.xlim((0, 76))
    
    #plt.title('')
    plt.legend(fontsize=14,loc=(1.04,0.5))
    plt.tight_layout() # para sair a figura toda
    plt.show
    

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.grid(False)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    #plt.figure(figsize=(8,8))
    plt.rcParams["font.size"] = "10"
    
    
    
def metrics (MC):
    
    c=MC.shape[0]

    SC=np.sum(MC,0) # somatório das colunas
    SL=np.sum(MC,1) # somatório das linhas
    
    EG=np.float(np.sum(np.diagonal(MC,0)))/np.sum(MC)*100 # exatidão global
    
    #print ('producer accuracy',np.diagonal(MC,0)/ np.float32(SC)) #acuracia do produtor
    
    np.diagonal(MC,0)/ np.float32(SL) #acuracia do usuário
    
    Kappa=np.float(np.sum(np.diagonal(MC,0)))*np.sum(MC)
    Kappa=Kappa-np.sum(SC*SL)
    Kappa=Kappa/(np.sum(MC)**2-np.sum(SC*SL)) #kappa
    
    Theta1=np.float(np.sum(np.diagonal(MC,0)))/np.sum(MC)
    Theta2=np.float(np.sum(SC*SL))/np.sum(MC)**2
    Theta3=np.float(np.sum(np.diagonal(MC,0)*(SC+SL)))/np.sum(MC)**2
    Theta4=0.
    for i in range(0,c):
        for j in range (0,c):
            Theta4=Theta4+MC[i,j]*(SL[j]+SC[i])**2
    Theta4=Theta4/np.sum(MC)**3
    
    Apoio1=(Theta1*(1-Theta1)/(1-Theta2)**2)
    Apoio2=(2*(1-Theta1)*(2*Theta1*Theta2-Theta3))/(1-Theta2)**3
    Apoio3=(((1-Theta1)**2)*(Theta4-4*Theta2**2))/(1-Theta2)**4
    
    VarK=(Apoio1+Apoio2+Apoio3)/np.sum(MC) # variancia
    #print ('Variance',VarK)
    
    Zc=Kappa/np.sqrt(VarK) # Z calculado
    Ztab=1.96 #Z tabela 
    print ('Global accuracy =', EG)
    print ('Kappa index  = ', Kappa)
    print ('Z-test = ', Zc,'\n')
    
    if Zc > Ztab:    
        print ('Rejects H0, the classification is different from random.')
    else:
        print ('Does not reject H0, classification is at random.')
        
