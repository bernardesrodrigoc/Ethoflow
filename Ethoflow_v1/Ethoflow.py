# -*- coding: utf-8 -*-
"""
See readme for information about this file.
Ethoflow: computer vision and artificial intelligence-based software for automatic behavior analysis
v 1.0

DOI: 10.1101/2020.07.23.218255
LicenseCC BY-NC-ND 4.0

@developer: Rodrigo Cupertino Bernardes
https://www.researchgate.net/profile/Rodrigo_Cupertino_Bernardes
"""


# wdir='path/ethoflow'
import PyQt5
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5 import QtGui,QtCore
from PyQt5 import QtWidgets
import math

#importa a Classe Ui_Dialog no arquivo gui.py
from gui import Ui_ethoflow
# Others functions 
import cv2
import numpy as np
import pandas as pd
#from sklearn.cluster import KMeans
#from scipy.optimize import linear_sum_assignment
#from scipy.spatial.distance import cdist
#from scipy import ndimage
from random import randint
import random
import string
from datetime import datetime
import scipy.signal

#from random import randint
#from numba import vectorize
#import imutils
#from collections import deque
#import matplotlib.pyplot as plt
from collections import deque
from itertools import combinations
import networkx as nx

#from scipy import ndimage
from utils.video_utils import blob_extractor
from utils.coordenada import Coordenada
from utils import video_back_simple

#### mask
import os
import platform
import winsound

import sys
import re
import time
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
#import skimage
import glob

#from mask_rcnn.mrcnn import utils
from mask_rcnn.mrcnn import visualize
#from mask_rcnn.mrcnn.visualize import display_images
import mask_rcnn.mrcnn.model as modellib
#from mask_rcnn.mrcnn.model import log
#import mask_rcnn.bee
from mask_rcnn import bee


from threading import Thread
from imutils.video import FPS
from queue import Queue
from imutils.video import FileVideoStream

from utils.video_process_thread import videoprocess

from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import plot_model

from tensorflow import keras

class AppWindow(QtWidgets.QTabWidget):    
    def __init__(self):
        super().__init__()
        self.ui = Ui_ethoflow() 
        self.ui.setupUi(self)
################################# Desenvolver a partir daqui ############################ 
      
# Função para os botões
        
## bottons for configuration
        self.ui.upload_video.clicked.connect(self.upload_file_name)
        self.ui.close.clicked.connect(self.closeEvent)
        self.ui.run_video.clicked.connect(self.run_video_event)
        self.ui.stop_view_video.clicked.connect(self.stop_view_video_event)
        self.ui.save_parameters.clicked.connect(self.save_parameters_event)
        self.ui.read_parameters.clicked.connect(self.read_parameters_event)        
        self.ui.calc_dist.clicked.connect(self.apply_roi_event)
        self.ui.calc_dist_scale.clicked.connect(self.calc_dist_event)      
        
        self.ui.deter_center.clicked.connect(self.apply_center_event)
        
        self.ui.select_regions.clicked.connect(self.regions_event)
        
        self.ui.check_regions.clicked.connect(self.check_regions_event)
        self.ui.check_regions_ind.clicked.connect(self.check_regions_ind_event)
        
        
                       
### Verifica se ComBox do roi crop foi modificado pelo Usuario        
        self.ui.combo_roi.currentIndexChanged.connect(self.show_hide_bottom_event)
        self.ui.roi_shape_crop.currentIndexChanged.connect(self.show_circle_event)  

## global variables for configuration
        
        #self.video_name = str(self.ui.out_file_path.text())      
        self.tresh_value = int(self.ui.tresh_value.text())
        self.frame_number = int(self.ui.frame_number.text())
        self.max_area = int(self.ui.max_area.text())
        self.min_area = int(self.ui.min_area.text())
        self.max_len = int(self.ui.max_len.text())
        self.min_len = int(self.ui.min_len.text())
        self.n_ind = int(self.ui.n_ind.text())
        self.frame_resolution = int(self.ui.set_frame_resolution.text())
        self.distance = int(self.ui.distance_crop.text())
        self.capturing = False
        self.filename = ''
        self.frame_inicio = None
        self.crop_xyhw_rectangle = None
        self.crop_xyhw_circle = None
        self.bboxes=[]
        
        self.meas_last = list(np.zeros((self.n_ind,2)))
        self.meas_now = list(np.zeros((self.n_ind,2))) 
        
        
        self.kernel= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))    
        self.kernel1= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
        
        
        
        
        
## bottons for simple background
        self.ui.run_video_simple_ground.clicked.connect(self.video_simple_ground_Event)
        self.ui.close_2.clicked.connect(self.closeEvent)
        self.ui.stop_view_video_2.clicked.connect(self.stop_view_video_event)
        
        
        
## global variables for simple background
        self.video_time_in_frame = int(self.ui.video_time_in_frame.text())
        
        #self.frequency = 2500
        #self.duration = 1000
        

## bottons for complex background

        self.ui.run_video_complex_ground.clicked.connect(self.video_complex_ground_Event)
        self.ui.make_imgs_mask.clicked.connect(self.make_imgs_mask_Event)
        
        
## global variables for mask
        #self.custom_WEIGHTS_PATH = "mask_rcnn/logs/bee20190824T2037/mask_rcnn_bee_0001.h5"
        self.custom_WEIGHTS_PATH = "mask_rcnn/logs/bee20190824T2037/mask_rcnn_bee_0024.h5"
        
        

        self.MODEL_DIR = "mask_rcnn/logs"
        
        self.config = bee.BeeConfig()
        
        self.custom_DIR = "dataset"
        
        self.TEST_MODE = "inference"
        
        class InferenceConfig(self.config.__class__):
            # Run detection on one image at a time
            GPU_COUNT = 1
            IMAGES_PER_GPU = 1
        self.config = InferenceConfig()
        
        DEVICE = "/gpu:0"  # /cpu:0 or /gpu:0
        with tf.device(DEVICE):
            self.model_mask = modellib.MaskRCNN(mode="inference", model_dir=self.MODEL_DIR,
                                              config=self.config  )
            
        self.model_mask.load_weights(self.custom_WEIGHTS_PATH, by_name=True)

### bottons for behaviour

        self.ui.run_estimates.clicked.connect(self.stimates_event)
        self.ui.make_imgs_behavior.clicked.connect(self.make_imgs_train_behavior_event)
        self.ui.upload_model.clicked.connect(self.upload_model_event)
        self.ui.run_behaviour.clicked.connect(self.run_behaviour_event)
        

#### variabels for behaviour

        self.duration = 2000  # seconds
        self.freq = 940  # Hz        
                                 
    
# functions
    
    def upload_file_name (self):
        self.filename= QFileDialog.getOpenFileName(self,"Video file", "","All Files (*)")
        
        #self.filename= QFileDialog.getSaveFileName(self,"Arquivo de Log", "","All Files (*)")
        self.filename=self.filename[0]
                       
        
        
    def closeEvent(self):
        """Generate 'question' dialog on clicking 'X' button in title bar.

        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit? Any unsaved work will be lost.",
            QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Save)

        if reply == QMessageBox.Close:
            self.capturing = False
            self.close()            
        else:
            pass
        
     
    
    def run_video_event(self):        
        self.capturing = True        
        
        if str(self.ui.n_ind.text()) != '':
             self.n_ind = int(self.ui.n_ind.text())
        
        
        
        cap = cv2.VideoCapture(self.filename)
        self.total_frame_number = (int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
        self.ui.lcdNumber.display(str(self.total_frame_number))                      
        self.fps=cap.get(cv2.CAP_PROP_FPS)
                
        while(self.capturing):
                
            if str(self.ui.tresh_value.text()) != '':
                self.tresh_value = int(self.ui.tresh_value.text())
            
            if str(self.ui.frame_number.text()) != '':
                try:
                    self.frame_number = int(self.ui.frame_number.text())
                except:
                    self.frame_number = 0
                    reply = QMessageBox.information( self, "Message", "Invalid frame number. This returned to 0", QMessageBox.Ok)    
                    if reply == QMessageBox.Ok:
                        self.capturing = False
                        pass
                
            if str(self.ui.max_area.text()) != '':
                self.max_area = float(self.ui.max_area.text())
                
            if str(self.ui.min_area.text()) != '':
                self.min_area = float(self.ui.min_area.text())
                
            if str(self.ui.max_len.text()) != '':
                self.max_len = float(self.ui.max_len.text())
                
            if str(self.ui.min_len.text()) != '':
                self.min_len = float(self.ui.min_len.text())
                
            if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
                self.frame_resolution = int(self.ui.set_frame_resolution.text())
                
            if str(self.ui.distance_crop.text()) != '':
                self.distance = float(self.ui.distance_crop.text())
                
            if str(self.ui.max_prop.text()) != '':
                self.max_prop = float(self.ui.max_prop.text())
            if str(self.ui.min_prop.text()) != '':
                self.min_prop = float(self.ui.min_prop.text())
                
                                
             
                
            #read the frame            
            
            success, frame = cap.read()
            cap.set(1, self.frame_number)
            if not success:
                
                reply = QMessageBox.information( self, "Message", "Failed to read video. Check video file path", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    self.capturing = False
                    pass            
                
            else:             
                lista=self.ui.combo_roi.currentIndex()
                shape_crop_list = self.ui.roi_shape_crop.currentIndex()
                
                frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
           
                #cv2.circle(frame, (866, 169), 9, (255,255,255), -1)
                if lista==1:
                    if shape_crop_list==0:     
                        
                        
                        if self.distance < 10 and self.crop_xyhw_circle == None:
                            reply = QMessageBox.information( self, "Information", "Distance or center not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            try:
                                x,y,h,w = self.crop_xyhw_circle
                                
                                
                                
                                try:                                    
                                   
                                    frame = frame[y:y+w, x:x+h]
                                    
                                except:
                                    reply = QMessageBox.information( self, "Information", "Probably conflict between resolution and roi.", QMessageBox.Ok)    
                                    if reply == QMessageBox.Ok:
                                        self.capturing = False
                                        break
                                        pass
                                
                                
                                
                            except:
                                reply = QMessageBox.information( self, "Information", "Probably the unselected center.", QMessageBox.Ok)    
                                if reply == QMessageBox.Ok:
                                    self.capturing = False
                                    break
                                    pass
                    else:
                        if self.crop_xyhw_rectangle == None:
                            reply = QMessageBox.information( self, "Information", "ROI not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            x,y,h,w = self.crop_xyhw_rectangle
                            frame = frame[y:w, x:h]
                
                
                
                self.ui.shape_1.setText( str(frame.shape[1] ))
                self.ui.shape_0.setText( str(frame.shape[0] ) )
                
                    
                               
                lista_id=self.ui.thresh_option.currentIndex()
                if lista_id==0: self.thr_option = False
                else: self.thr_option = True  
                
                
                segmentedFrame,framegray = video_back_simple.colour_to_thresh(frame, self.tresh_value, self.kernel,self.kernel1,self.thr_option)# aqui eu entraria com a mask rcnn
                
                if shape_crop_list==0:
                    segmentedFrame= cv2.bitwise_and(segmentedFrame, segmentedFrame, mask=self.mask)
                
                                
                bounding_boxes, miniframes, centroids, \
                        areas, pixels, contours, estimated_body_lengths, countours_got,body_proportions = blob_extractor(segmentedFrame,
                                                                                                        segmentedFrame,
                                                                                                        self.min_area,
                                                                                                        self.max_area,
                                                                                                        self.min_len,
                                                                                                        self.max_len,
                                                                                                        self.max_prop,
                                                                                                        self.min_prop)
            
                
                
            
                
                if areas != []:
                    self.ui.output_max_area.setText( str(max(areas)) )
                    self.ui.output_min_area.setText( str(min(areas)) )                
                    self.ui.output_sd_area.setText( str(round(np.std((areas)),2)) )
                    self.ui.output_median_area.setText( str(np.median(areas)) )
                else:
                    self.ui.output_max_area.setText( "Nothing detected" )
                    self.ui.output_min_area.setText( "ND" ) 
                    self.ui.output_sd_area.setText( "ND" )
                    self.ui.output_median_area.setText( "ND" )
                    
                if estimated_body_lengths != []:
                    self.ui.output_max_len.setText( str(max(estimated_body_lengths)) )
                    self.ui.output_min_len.setText( str(min(estimated_body_lengths)) )                
                    self.ui.output_sd_len.setText( str(round(np.std((estimated_body_lengths)),2)) )
                    self.ui.output_median_len.setText( str(np.median(estimated_body_lengths)) )
                else:
                    self.ui.output_max_len.setText( "Nothing detected" )
                    self.ui.output_min_len.setText( "ND" ) 
                    self.ui.output_sd_len.setText( "ND" )
                    self.ui.output_median_len.setText( "ND" )
                    
                if body_proportions != []:
                    
                                                               
                    self.ui.output_max_prop.setText( str(round(max(body_proportions),2)))
                                                           
                    self.ui.output_min_prop.setText( str(round(min(body_proportions),2 ) ))
                    self.ui.output_sd_prop.setText( str(round(np.std((body_proportions)),2)) )
                    self.ui.output_median_prop.setText( str(round(np.median(body_proportions),2 ) ))
                else:
                    self.ui.output_max_prop.setText( "Nothing detected" )
                    self.ui.output_min_prop.setText( "ND" ) 
                    self.ui.output_sd_prop.setText( "ND" )
                    self.ui.output_median_prop.setText( "ND" )
                
                
                cv2.drawContours(frame, contours, -1, (0,0,255), -1)            
                          
                escala = min(500./frame.shape[0], 500./frame.shape[1]) 
                largura_window = int(frame.shape[1] * escala)
                altura_window = int(frame.shape[0] * escala)
                cv2.namedWindow('Ethoflow', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('Ethoflow', largura_window, altura_window)
                cv2.imshow('Ethoflow', frame)
                
                #cv2.imshow('Running...',cv2.resize(frame, (0,0), fy= round(520/frame.shape[1],1), fx= round(520/frame.shape[0],1)))
                cv2.waitKey(1)
        cv2.destroyAllWindows()
            
    

    
    def stop_view_video_event(self):
        self.capturing = False
        
    
    def save_parameters_event(self):
        
        if str(self.ui.tresh_value.text()) != '':
            self.tresh_value = int(self.ui.tresh_value.text())
            
        if str(self.ui.frame_number.text()) != '':
            self.frame_number = int(self.ui.frame_number.text())
                
        if str(self.ui.max_area.text()) != '':
            self.max_area = float(self.ui.max_area.text())
                
        if str(self.ui.min_area.text()) != '':
            self.min_area = float(self.ui.min_area.text())
                
        if str(self.ui.max_len.text()) != '':
            self.max_len = float(self.ui.max_len.text())
                
        if str(self.ui.min_len.text()) != '':
            self.min_len = float(self.ui.min_len.text())
            
        if str(self.ui.n_ind.text())!='':
            self.n_ind = int(self.ui.n_ind.text())
            
        if str(self.ui.distance_crop.text()) != '':
                self.distance = float(self.ui.distance_crop.text())
                
        if str(self.ui.distance_scale.text()) != '':
                self.distance_scale = float(self.ui.distance_scale.text())
                
        if str(self.ui.distance_scale_know.text()) != '':
                self.distance_scale_know = float(self.ui.distance_scale_know.text())
                
        if str(self.ui.interaction_threshold.text()) != '':
                self.interaction_threshold = float(self.ui.interaction_threshold.text())
                
        if str(self.ui.thersh_min_mov.text()) != '':
                self.thersh_min_mov = float(self.ui.thersh_min_mov.text())
                
        if str(self.ui.thersh_max_mov.text()) != '':
                self.thersh_max_mov = float(self.ui.thersh_max_mov.text())
                
        if str(self.ui.max_prop.text()) != '':
            self.max_prop = float(self.ui.max_prop.text())
            
        if str(self.ui.min_prop.text()) != '':
            self.min_prop = float(self.ui.min_prop.text())
                
                
        if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
                self.frame_resolution = int(self.ui.set_frame_resolution.text())
        
        self.filename_parameters= QFileDialog.getSaveFileName(self,"Parameter file", "","Text Files (*.txt)")
        self.filename_parameters=self.filename_parameters[0]
        
        try:f=open(self.filename_parameters,'w')
        except:f=open('settings/parameters_file','w')
        f.write('tresh =' + str(self.tresh_value) +'\n')
        f.write('max_area =' + str(self.max_area) +'\n')
        f.write('min_area =' + str(self.min_area) +'\n')
        f.write('max_len =' + str(self.max_len) +'\n')
        f.write('min_len =' + str(self.min_len) +'\n')
        f.write('n_obj =' + str(self.n_ind) +'\n')
        f.write('crop_distance =' + str(self.distance) +'\n')
        f.write('distance_scale =' + str(self.distance_scale) +'\n')
        f.write('distance_scale_know =' + str(self.distance_scale_know) +'\n')
        f.write('interaction_threshold =' + str(self.interaction_threshold) +'\n')
        f.write('thersh_min_mov =' + str(self.thersh_min_mov) +'\n')
        f.write('thersh_max_mov =' + str(self.thersh_max_mov) +'\n')
        f.write('max_prop =' + str(self.max_prop) +'\n')
        f.write('min_prop =' + str(self.min_prop) +'\n')
        f.write('frame_resolution =' + str(self.frame_resolution) +'\n')        
        f.close()
        
        
    def read_parameters_event(self):
        self.filename_read_parameters = QFileDialog.getOpenFileName(self,"Parameter file", "","Text Files (*.txt)")
        self.filename_read_parameters=self.filename_read_parameters[0]
        try:f=open(self.filename_read_parameters,'r')
        except:f=open('settings/default_parameters.txt','r')
        
        data = f.readlines()
        self.tresh_value, self.max_area, self.min_area, self.max_len, \
        self.min_len, self.n_ind, self.distance, self.distance_scale, \
        self.distance_scale_know, self.interaction_threshold, self.thersh_min_mov, \
        self.thersh_max_mov, self.max_prop, self.min_prop, self.frame_resolution = [d.split('=')[1].split('\n')[0] for d in data]
        
        
        self.ui.tresh_value.setText(str(self.tresh_value))
        self.ui.max_area.setText(str(self.max_area))
        self.ui.min_area.setText(str(self.min_area))
        self.ui.max_len.setText(str(self.max_len))
        self.ui.min_len.setText(str(self.min_len))
        self.ui.n_ind.setText(str(self.n_ind))
        self.ui.distance_crop.setText( str(self.distance) )
        self.ui.distance_scale.setText(str(self.distance_scale))
        self.ui.distance_scale_know.setText(str(self.distance_scale_know))
        self.ui.interaction_threshold.setText(str(self.interaction_threshold))
        self.ui.thersh_min_mov.setText(str(self.thersh_min_mov))
        self.ui.thersh_max_mov.setText(str(self.thersh_max_mov))
        
        self.ui.max_prop.setText(str(self.max_prop))
        self.ui.min_prop.setText(str(self.min_prop))
        self.ui.set_frame_resolution.setText( str(self.frame_resolution) )
        
    def apply_roi_event(self):
        
        
        
        cap = cv2.VideoCapture(self.filename)
        success, frame = cap.read()
            
        if success:
            
            if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
                self.frame_resolution = int(self.ui.set_frame_resolution.text())
            
            frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
                                       
            coordenadas_crop = Coordenada(frame)
                
            if len(coordenadas_crop) == 2:
                # centro
                centro_input = coordenadas_crop[0]
                # borda
                raios = coordenadas_crop[1]
                x_center, y_center = centro_input
                x_borda, y_borda = raios
                self.distance = int(math.sqrt(((x_center-x_borda)**2)+((y_center-y_borda)**2)))
                    
                I = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
                mask = np.zeros((I.shape[0], I.shape[1]))
                
                cv2.circle(mask, (x_center,  y_center), int(self.distance), 255, -1)
                
                I[mask == 0] = 255
                
                self.mask=mask
                
                            
                _,thresh = cv2.threshold(I.copy(),254,255,cv2.THRESH_BINARY_INV)        
                
                contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
                     
                #self.crop_xyhw = cv2.boundingRect(contours[0])
                    
                self.ui.distance_crop.setText( str(self.distance) )
                    
            else:
                reply = QMessageBox.information( self, "Information", "Select only two points", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    pass
            
        else:
            reply = QMessageBox.information( self, "Information", "Failed to read video. Check video file path", QMessageBox.Ok)    
            if reply == QMessageBox.Ok:
                pass 
                             


    def calc_dist_event(self):
        
        
        
        cap = cv2.VideoCapture(self.filename)
        success, frame = cap.read()
            
        if success:
            
            if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
                self.frame_resolution = int(self.ui.set_frame_resolution.text())
            
            frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
                                       
            coordenadas_crop = Coordenada(frame)
                
            if len(coordenadas_crop) == 2:
                # centro
                centro_input = coordenadas_crop[0]
                # borda
                raios = coordenadas_crop[1]
                x_center, y_center = centro_input
                x_borda, y_borda = raios
                self.distance_scale = int(math.sqrt(((x_center-x_borda)**2)+((y_center-y_borda)**2)))                                    
                    
                self.ui.distance_scale.setText( str(self.distance_scale) )
                    
            else:
                reply = QMessageBox.information( self, "Information", "Select only two points", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    pass
            
        else:
            reply = QMessageBox.information( self, "Information", "Failed to read video. Check video file path", QMessageBox.Ok)    
            if reply == QMessageBox.Ok:
                pass 
    
    
    
    
    
    def apply_center_event(self,indice):
        lista=self.ui.combo_roi.currentIndex()
        
        if lista ==1:
                    
            shape_crop_list = self.ui.roi_shape_crop.currentIndex()
            
            if str(self.ui.distance_crop.text()) != '':
                    self.distance = float(self.ui.distance_crop.text())
            
            cap = cv2.VideoCapture(self.filename)
            success, frame = cap.read()
                
            if success:
                
                if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
                    self.frame_resolution = int(self.ui.set_frame_resolution.text())  
                
                frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
                
                coordenadas_crop = Coordenada(frame)
                
                if shape_crop_list == 0:
                    if len(coordenadas_crop) == 1:
                        
                         # centro
                        centro_input = coordenadas_crop[0]
                        
                        x_center, y_center = centro_input
                                           
                        I = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
                        self.mask = np.zeros((I.shape[0], I.shape[1]), np.uint8)
                        
                        cv2.circle(self.mask, (x_center,  y_center), int(self.distance), (255,255,255), -1)
                        
                        I[self.mask == 0] = 255
                        #if circle == True:
                            #   frame[mask == 0] = (255,255,255)
                        
                        _,thresh = cv2.threshold(I.copy(),254,255,cv2.THRESH_BINARY_INV)        
                        
                        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                        
                        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
                        biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
                             
                        self.crop_xyhw_circle = cv2.boundingRect(biggest_contour)
                        
                        x,y,h,w = self.crop_xyhw_circle
                        self.mask = self.mask[y:y+w, x:x+h]
                        
                    else:
                        reply = QMessageBox.information( self, "Information", "Select only one point", QMessageBox.Ok)    
                        if reply == QMessageBox.Ok:
                            pass
                        
                else:
                    if len(coordenadas_crop) == 2:
                        
                         # centro
                        sup_esquerdo_input = coordenadas_crop[0]
                        
                        x_esquerdo, y_esquerdo = sup_esquerdo_input
                        
                        sup_direito_input = coordenadas_crop[1]
                        
                        x_direito, y_direito = sup_direito_input
                                                                                                    
                        self.crop_xyhw_rectangle = (x_esquerdo, y_esquerdo, x_direito,  y_direito)
                        
                    else:
                        error_dialog = QtWidgets.QErrorMessage()
                        error_dialog.showMessage('Select only two points')           
                        #pass
                    
                
            else:
                reply = QMessageBox.information( self, "Information", "Failed to read video. Check video file path", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    pass
                
        if lista ==0:
            self.ui.calc_dist.setDisabled(1)
            self.ui.distance_crop.setDisabled(1)
            self.ui.label1.setDisabled(1)
            self.ui.label2.setDisabled(1) 
            self.ui.label3.setDisabled(1) 
            self.ui.roi_shape_crop.setDisabled(1)            
            
            
        else:
            #self.ui.calc_dist.setEnabled(1)
            #self.ui.distance_crop.setEnabled(1)
            #self.ui.example_roi.setEnabled(1)
            #self.ui.label1.setEnabled(1)
            #self.ui.label2.setEnabled(1)
            self.ui.roi_shape_crop.setEnabled(1)
                    
                
                    
    def show_circle_event(self,indice):
        if indice==1: 
            self.ui.calc_dist.setDisabled(1)
            self.ui.distance_crop.setDisabled(1)
            self.ui.label1.setDisabled(1)
            self.ui.label2.setDisabled(1)
            self.ui.label3.setEnabled(1)
            self.ui.deter_center.setEnabled(1)
           
            
        else:
            self.ui.calc_dist.setEnabled(1)
            self.ui.distance_crop.setEnabled(1)
            self.ui.label1.setEnabled(1)
            self.ui.label2.setEnabled(1)
            self.ui.label3.setDisabled(1)
            self.ui.deter_center.setEnabled(1)
            
            
            
    def show_hide_bottom_event (self,indice):
        if indice==0:
            self.ui.Framenumber_7.setDisabled(1)            
            self.ui.roi_shape_crop.setDisabled(1)            
            self.ui.calc_dist.setDisabled(1)
            self.ui.label2.setDisabled(1)
            self.ui.distance_crop.setDisabled(1)
            self.ui.deter_center.setDisabled(1)
            self.ui.label1.setDisabled(1)
            self.ui.label3.setDisabled(1)            
        else:                       
            self.ui.roi_shape_crop.setEnabled(1)            
            

    def regions_event(self):            
                
        cap = cv2.VideoCapture(self.filename)
        self.bboxes = []
        
        if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
            self.frame_resolution = int(self.ui.set_frame_resolution.text())
                
        if str(self.ui.distance_crop.text()) != '':
            self.distance = float(self.ui.distance_crop.text())
            
        success, frame = cap.read()
            
        if not success:
                
            reply = QMessageBox.information( self, "Message", "Failed to read video. Check video file path", QMessageBox.Ok)    
            if reply == QMessageBox.Ok:                
                pass            
                
                     
        lista=self.ui.combo_roi.currentIndex()
        shape_crop_list = self.ui.roi_shape_crop.currentIndex()
                
        frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                         int((frame.shape[0] * self.frame_resolution)/100)))
           
            #cv2.circle(frame, (866, 169), 9, (255,255,255), -1)
        if lista==1:
            if shape_crop_list==0:     
                        
                        
                if self.distance < 10 and self.crop_xyhw_circle == None:
                    reply = QMessageBox.information( self, "Information", "Distance or center not set correctly", QMessageBox.Ok)    
                    if reply == QMessageBox.Ok:
                        pass
                else:
                    try:
                        x,y,h,w = self.crop_xyhw_circle
                                
                        try:                                    
                                   
                            frame = frame[y:y+w, x:x+h]
                                    
                        except:
                            reply = QMessageBox.information( self, "Information", "Probably conflict between resolution and roi.", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:                                
                                pass
                                
                                
                                
                    except:
                        reply = QMessageBox.information( self, "Information", "Probably the unselected center.", QMessageBox.Ok)    
                        if reply == QMessageBox.Ok:                            
                            pass
            else:
                if self.crop_xyhw_rectangle == None:
                    reply = QMessageBox.information( self, "Information", "ROI not set correctly", QMessageBox.Ok)    
                    if reply == QMessageBox.Ok:         
                        pass
                else:
                    x,y,h,w = self.crop_xyhw_rectangle
                    frame = frame[y:w, x:h]
                
                
                                         
            try:
                while True:
                    # tuple of format: x0, y0, width, height 
                    bbox = cv2.selectROI('EthoFlow', frame,fromCenter=False,showCrosshair=False)
                    self.bboxes.append(bbox)
                        
                    print("Press q to quit selecting boxes and start tracking")
                    print("Press any other key to select next object")
                    k = cv2.waitKey(0) & 0xFF
                    if (k == 113):
                        break # q is pressed
                    
            except:
                reply = QMessageBox.information( self, "Information", "Some error. Try again.", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:                            
                    pass
                
        
        cv2.destroyAllWindows()
        

    def check_regions_event(self):
        if self.ui.check_regions.isChecked():
            if self.bboxes == []:
                
                self.ui.check_regions.setChecked(False)
                self.ui.check_regions_ind.setChecked(False)                
                
                reply = QMessageBox.information( self, "Information", "Unselected regions. Select regions and try again", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    pass
        
    def check_regions_ind_event(self):
            if self.ui.check_regions_ind.isChecked():
                if self.bboxes == []:
                    
                    self.ui.check_regions.setChecked(False)
                    self.ui.check_regions_ind.setChecked(False)
                    
                    reply = QMessageBox.information( self, "Information", "Unselected regions. Select regions and try again", QMessageBox.Ok)    
                    if reply == QMessageBox.Ok:
                        pass
                else:
                    self.ui.check_regions.setChecked(True)


############################################# simple background #####################################
            
     ##########simple ground functions 
    class FileVideoStream:
            def __init__(self, path, queueSize=98):
                # initialize the file video stream along with the boolean
                # used to indicate if the thread should be stopped or not
                self.stream = cv2.VideoCapture(path)
                
                               
                self.stopped = False
        
                # initialize the queue used to store frames read from
                # the video file
                self.Q = Queue(maxsize=queueSize)
                
            def start(self):
                # start a thread to read frames from the file video stream
                t = Thread(target=self.update, args=())
                #t.daemon = True
                t.start()               
                             
                return self
            
            def update(self):
                # keep looping infinitely
                
                while True:
                    # if the thread indicator variable is set, stop the
                    # thread
                    if self.stopped:
                        return
         
                    # otherwise, ensure the queue has room in it
                    if not self.Q.full():
                        # read the next frame from the file
                        
                        (grabbed, frame) = self.stream.read()
         
                        # if the `grabbed` boolean is `False`, then we have
                        # reached the end of the video file
                        if not grabbed:
                            self.stop()
                            return
         
                        # add the frame to the queue
                        self.Q.put(frame)
                
            def read(self):
                # return next frame in the queue
                return self.Q.get()
            
            def more(self):
                # return True if there are still frames in the queue
                return self.Q.qsize() > 0
            
            def stop(self):
                # indicate that the thread should be stopped
                self.stopped = True
    
    

    
    class videoprocess:
            def __init__(self, frame, distance, x,y,h,w):
                # initialize the file video stream along with the boolean
                # used to indicate if the thread should be stopped or not
                
                self.frame = frame
                self.distance = distance
                self.x, self.y, self.h, self.w = x,y,h,w
                
                self.var1 = Queue(maxsize=100)
                self.stopped = False
                
                
            def start(self):
                # start a thread to read frames from the file video stream
                d = Thread(target=self.update, args=())
                d.daemon = True
                d.start()
                
                             
                return self
            
            def update(self):
                # keep looping infinitely
                
                while True:
                    # if the thread indicator variable is set, stop the
                    # thread
                    if self.stopped:
                        return
         
                    # otherwise, ensure the queue has room in it
                    if not self.var1.full():
                                           
                        mask = np.zeros((self.frame.shape[0], self.frame.shape[1]))
                        #mask = np.zeros((height, width))
                                    
                        cv2.circle(mask, (self.x+ int(self.h/2),  self.y+ int(self.w/2)), int(self.distance), 255, -1)                                                                       
                                    
                        self.mask=mask  
                        self.frame[self.mask == 0] = (255,255,255)
                        self.frame = self.frame[self.y: self.y+self.w, self.x:self.x+self.h]
                            
                        self.var1.put(self.frame)
                    
                        
                       
                
            def read(self):                
                                
                 return self.var1.get() 
            
            
            
            def more(self):
                # return True if there are still frames in the queue
                return self.var1 != []
            
            def stop(self):
                # indicate that the thread should be stopped
                self.stopped = True        
    
    
        
                  
               
    
    
    
    def video_simple_ground_Event (self, indice):
        
        lista_id=self.ui.thresh_option.currentIndex()
        if lista_id==0: self.thr_option = False
        else: self.thr_option = True  
        
        bb=2        
              
        self.ui.processing.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                            "color: rgb(30, 30, 255);\n"
                            "")
        self.ui.processing.setText('Processing ...')
        
       
        
        atual_frame_number= -1 
        self.capturing = True
        write_frame= False
        pts = deque(maxlen=360)
        #var_armazenada1 = Queue(maxsize=2)
        #var_armazenada2 = Queue(maxsize=2)
        #var_armazenada3 = Queue(maxsize=2)
        
        

        if self.ui.check_save_data.isChecked():
            self.filename_parameters_cvs= QFileDialog.getSaveFileName(self,"Save data", "","Comma Separated Value Files (*.csv)")
            self.filename_parameters_cvs = self.filename_parameters_cvs[0]              
        
                
        
        cap = FileVideoStream(self.filename).start()
        time.sleep(1.0)
        
                
        if self.ui.check_save_video.isChecked():
            
            write_frame= True
            
            
            if str(self.ui.shape_1.text()) != '' and str(self.ui.shape_0.text()) != '':
                self.shape_1 = int(self.ui.shape_1.text())
                self.shape_0 = int(self.ui.shape_0.text())
                       
            
            codec = 'DIVX'
            
            fourcc = cv2.VideoWriter_fourcc(*codec)
            output_framesize = (self.shape_1,self.shape_0)
            
            self.filename_parameters_video= QFileDialog.getSaveFileName(self,"Save video", "","mp4 Files (*.mp4)")
            self.filename_parameters_video = self.filename_parameters_video[0]
            
            try:
                out = cv2.VideoWriter(filename = self.filename_parameters_video, fourcc = fourcc,
                                  fps = 30.0, frameSize = output_framesize, isColor = True)
            
            except: 
                out = cv2.VideoWriter(filename = "auto_video_saved.mp4", fourcc = fourcc,
                                  fps = 30.0, frameSize = output_framesize, isColor = True)
            
        
        #self.total_frame_number = (int(cap_par.get(cv2.CAP_PROP_FRAME_COUNT)))
        
        if str(self.ui.n_ind.text()) != '':
                self.n_ind = int(self.ui.n_ind.text())
        
        colours = []
        #t_id = []        
        for i in range (0, self.n_ind ):
             cor=(randint(0, 255), randint(0, 255), randint(0, 255))
             colours.append(cor)
             
        t_id=random.sample(string.ascii_uppercase, self.n_ind)
        #t_id.append(id_letter)
             
                   
                        
        df = []
        #last = 0
            
        lista_id=self.ui.combo_id.currentIndex()
        if lista_id==0: mot = False
        else: mot = True  
                
        if str(self.ui.tresh_value.text()) != '':
            self.tresh_value = int(self.ui.tresh_value.text())
            
        #if str(self.ui.frame_number.text()) != '':
            #self.frame_number = int(self.ui.frame_number.text())
                
        if str(self.ui.max_area.text()) != '':
            self.max_area = float(self.ui.max_area.text())
                
        if str(self.ui.min_area.text()) != '':
            self.min_area = float(self.ui.min_area.text())
                
        if str(self.ui.max_len.text()) != '':
            self.max_len = float(self.ui.max_len.text())
                
        if str(self.ui.min_len.text()) != '':
            self.min_len = float(self.ui.min_len.text())
                
        if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
            self.frame_resolution = int(self.ui.set_frame_resolution.text())
                
        if str(self.ui.distance_crop.text()) != '':
            self.distance = float(self.ui.distance_crop.text())
            
        if str(self.ui.distance_scale.text()) != '':
            self.distance_scale = float(self.ui.distance_scale.text())
            
        if str(self.ui.distance_scale_know.text()) != '':
            self.distance_scale_know = float(self.ui.distance_scale_know.text())
            
        if str(self.ui.interaction_threshold.text()) != '':
            self.interaction_threshold = float(self.ui.interaction_threshold.text())
            
        if str(self.ui.thersh_min_mov.text()) != '':
            self.thersh_min_mov = float(self.ui.thersh_min_mov.text())
            
        if str(self.ui.thersh_max_mov.text()) != '':
            self.thersh_max_mov = float(self.ui.thersh_max_mov.text())
            
        if str(self.ui.max_prop.text()) != '':
            self.max_prop = float(self.ui.max_prop.text())
            
        if str(self.ui.min_prop.text()) != '':
            self.min_prop = float(self.ui.min_prop.text())
                
        try:
            if str(self.ui.video_time_in_frame.text()) != '' and int(self.ui.video_time_in_frame.text()) in range(1,self.total_frame_number+1,1):
                self.video_time_in_frame = int(self.ui.video_time_in_frame.text())
        except:
            reply = QMessageBox.information( self, "Message", "Failed in computer video size. Check video file path", QMessageBox.Ok)    
            if reply == QMessageBox.Ok:
                self.capturing = False
                pass

        
        
        time_ini = datetime.now()    
        while(self.capturing and cap.more()):           
            success= True
            frame = cap.read()
            if not success:
                
                reply = QMessageBox.information( self, "Message", "Failed to read video. Check video file path", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    self.capturing = False
                    pass            
                
            else:
                
                
                atual_frame_number += 1
                
                lista=self.ui.combo_roi.currentIndex()
                shape_crop_list = self.ui.roi_shape_crop.currentIndex()
                
                #if self.frame_resolution != 100:
                frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
           
                ######## tampar algo
                
                #cv2.circle(frame, (866, 169), 9, (255,255,255), -1)
                
                if lista==1:
                    if shape_crop_list==0:     
                        
                        
                        
                        if self.distance < 10 and self.crop_xyhw_circle == None:
                            reply = QMessageBox.information( self, "Information", "Distance or center not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            try:
                                x,y,h,w = self.crop_xyhw_circle                               
                                
                                
                                try:                                    
                                    #frame[self.mask == 0] = (255,255,255)
                                    
                                    frame = frame[y:y+w, x:x+h]
                                    
                                except:
                                    reply = QMessageBox.information( self, "Information", "Probably conflict between resolution and roi.", QMessageBox.Ok)    
                                    if reply == QMessageBox.Ok:
                                        self.capturing = False
                                        break
                                        pass
                                
                                
                                
                            except:
                                reply = QMessageBox.information( self, "Information", "Probably the unselected center.", QMessageBox.Ok)    
                                if reply == QMessageBox.Ok:
                                    self.capturing = False
                                    break
                                    pass
                    else:
                        if self.crop_xyhw_rectangle == None:
                            reply = QMessageBox.information( self, "Information", "ROI not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            x,y,h,w = self.crop_xyhw_rectangle
                            frame = frame[y:w, x:h]
                
                
                
               
                
                ######## tentar usar chamando function                   
                #, frameGray
                segmentedFrame,framegray = video_back_simple.colour_to_thresh(frame, self.tresh_value,self.kernel,self.kernel1,self.thr_option)# aqui eu entraria com a mask rcnn
                
                if shape_crop_list==0: 
                    segmentedFrame= cv2.bitwise_and(segmentedFrame, segmentedFrame, mask=self.mask)
                
                self.contours, self.meas_last, self.meas_now = video_back_simple.detect_and_draw_contours(segmentedFrame,self.meas_last, self.meas_now,self.min_area, self.max_area, self.min_len, self.max_len, self.max_prop,self.min_prop)
                
                
               
                
                if len(self.meas_now) != self.n_ind:
                    
                    try:
                        contours, self.meas_now = video_back_simple.apply_k_means(self.contours, self.n_ind, self.meas_now)
                        
                    except:
                                                
                        self.ui.processing.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                            "color: rgb(255, 5, 5);\n"
                            "")
                        
                        self.ui.processing.setText('Error: No objects detected. Check restrictions')                       
                                               
                        break
                        
                
                row_ind, col_ind = video_back_simple.hungarian_algorithm(self.meas_last, self.meas_now)
                final, self.meas_now, df = video_back_simple.reorder_and_draw(frame, colours, self.n_ind, col_ind, self.meas_now, df, mot, atual_frame_number, int(frame.shape[0]),int(frame.shape[1]),self.video_time_in_frame,t_id,pts,write_frame)
                            # Create output dataframe
                    
                for i in range(self.n_ind):
                    df.append([atual_frame_number, self.meas_now[i][0], self.meas_now[i][1], t_id[i]])           
                                  
                completed = int( (atual_frame_number/int(self.video_time_in_frame))*100)
                
                self.ui.processed_frame_number.display(str(atual_frame_number)) 
                
                self.ui.video_progressBar.setValue(completed)
                            
                if self.ui.check_save_video.isChecked():
                    out.write(final)
                    
                    
                if self.ui.show_video_processing.isChecked():
                    write_frame= True
                    #cv2.putText(final, "Queue Size: {}".format(cap.Q.qsize()),
                               # (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    
                    escala = min(500./frame.shape[0], 500./frame.shape[1]) 
                    largura_window = int(frame.shape[1] * escala)
                    altura_window = int(frame.shape[0] * escala)
                    cv2.namedWindow('Ethoflow', cv2.WINDOW_NORMAL)
                    cv2.resizeWindow('Ethoflow', largura_window, altura_window)
                    cv2.imshow('Ethoflow', final)
                                               
                
                if atual_frame_number >= self.video_time_in_frame:
                    self.capturing = False
                          
                            
                 
                
                #cv2.imshow('Running...',cv2.resize(frame, (0,0), fy= round(520/frame.shape[1],1), fx= round(520/frame.shape[0],1)))
                cv2.waitKey(1)
        #last = atual_frame_number
        cap.stop()
        
        try:           
            
            time_end = datetime.now()
            spent_time = str(time_end-time_ini)
            spent_time=spent_time.split(":")
            self.ui.display_spent_time.setText( str(spent_time[0]) + ":" + str(spent_time[1]) + ":" + str(spent_time[2]) )
            
        except:
            self.ui.display_spent_time.setText(str(1))
        
        
        if self.ui.check_end_video.isChecked():
            
            if platform.system() == "Windows":                
                winsound.Beep(self.freq, self.duration)
                
            elif platform.system() == "linux" or platform.system() == "linux2":                
                os.system('play -nq -t alsa synth {} sine {}'.format(self.duration/1000, self.freq))
                
            else:
                print("\a")
            
           
        
        df = pd.DataFrame(np.matrix(df), columns = ['frame','pos_x','pos_y', 'id'])
        
        
        
        if self.ui.check_save_data.isChecked():
            
            try: 
                df.to_csv(self.filename_parameters_cvs, sep=',')
                df = pd.read_csv(self.filename_parameters_cvs)
                
                prop = self.distance_scale/self.distance_scale_know
                
                df = pd.read_csv(self.filename_parameters_cvs)     
                df = df.drop(columns=['Unnamed: 0'])
                
                df['dir_x'] = df['pos_x'] - df['pos_x'].shift(self.n_ind)
                df['dir_y'] = df['pos_y'] - df['pos_y'].shift(self.n_ind)
                df['speed'] = np.sqrt(df['dir_x']**2 + df['dir_y']**2)
                df['dir_x'] /= df['speed'] # chegou em cordenada polar- delta_x/dist = cos(theta)
                df['dir_y'] /= df['speed'] # chegou em cordenada polar- delta_y/dist = sin(theta)
                
                df['time'] = df['frame'] / self.fps
                
                df = df.rename(index=str, columns={'speed':'distance_pixel'})
                
                
                #### network
                comb =(combinations(np.array(np.unique(df['id'])), 2) )                
                individuals_pars=[]
                encounters_pars=[]
                for i in (comb): 
                   
                    x_1=np.array(df.loc[df['id']==i[0],'pos_x'])
                    x_2=np.array(df.loc[df['id']==i[1],'pos_x'])
                
                    y_1=np.array(df.loc[df['id']==i[0],'pos_y'])
                    y_2=np.array(df.loc[df['id']==i[1],'pos_y'])
                
                    dist_x = x_1 - x_2
                    dist_y = y_1 - y_2
                
                    dist_between = (np.sqrt(dist_x**2 + dist_y**2))/prop #cm
                        
                    individuals_pars.append(i)
                    encounters_pars.append(len(dist_between[dist_between<= self.interaction_threshold]))
                    
                    
                G = nx.MultiGraph() # permite adicionar mais varias bordas para o mesmo par de borda
                S = nx.Graph()
                for t, ind in enumerate(np.array(np.unique(df['id']))):
                    G.add_node(ind)
                    S.add_node(ind)
                
                for i in range(0, len(encounters_pars)):
                        if encounters_pars[i]>0:
                            S.add_edge(individuals_pars[i][0], individuals_pars[i][1],weights= encounters_pars[i])
                            for j in range (0, encounters_pars[i]):
                                G.add_edge(individuals_pars[i][0], individuals_pars[i][1])
                
                degrees = G.degree()
                group_desity = nx.density(G)
                
                nx.write_gml(S,self.filename_parameters_cvs + '.gml')
                #######
                df['distance'] = df['distance_pixel']/prop # (cm)

                df['instantaneous_speed'] = df['distance'] * self.fps
                df['instantaneous_acceleration'] = df['instantaneous_speed'] - df['instantaneous_speed'].shift(self.n_ind)
                
                rad=(np.arctan2(np.array(df['dir_y']) , np.array(df['dir_x'])))*180 # aqui calcula theta em radianos, ai multiplicar por180 e               
                df['turning_angle'] = rad /np.pi        # dividir por pi da em graus        
                
                df['stop']=0
                df['mean_movement']=0
                df['fast_movement']=0
                
                df['stop'][df['distance']<self.thersh_min_mov]=1
                df['mean_movement'][ (df['distance'] >=self.thersh_min_mov) & (df['distance'] <= self.thersh_max_mov) ] = 1
                df['fast_movement'][df['distance']>self.thersh_max_mov]=1
                
                ################################# smoothed

                df = df.replace([np.inf, -np.inf], np.nan).dropna(axis=0, how="any")
                
                df['smoothed_distance'] = scipy.signal.savgol_filter(df['distance'], 9, 1)
                df['smoothed_instantaneous_speed'] = scipy.signal.savgol_filter(df['instantaneous_speed'], 9, 1)
                df['smoothed_instantaneous_acceleration'] = scipy.signal.savgol_filter(df['instantaneous_acceleration'], 9, 1)
                df['smoothed_turning_angle'] = scipy.signal.savgol_filter(df['turning_angle'], 9, 1)
                
                
                ################################# mean variables

                for i in (np.unique(df['id'])):
                    
                    df.loc[df['id']==i,'individuals']= i 
                    sum_dist=df.loc[df['id']==i,'distance'].sum()    
                    df.loc[df['id']==i,'tracked_distance']= sum_dist # (cm)
                    
                    # average_speed
                    df.loc[df['id']==i,'mean_speed']= sum_dist /df['time'].max() # (cm/s)
                    # max speed
                    df.loc[df['id']==i,'max_speed']= df.loc[df['id']==i,'instantaneous_speed'].max() # (cm/s)
                    
                    df.loc[df['id']==i,'mean_turn_angle']= abs(df.loc[df['id']==i,'turning_angle']).mean()# (graus)
                    df.loc[df['id']==i,'meandering']= abs(df.loc[df['id']==i,'turning_angle']).sum()/sum_dist # (graus/cm)
                    df.loc[df['id']==i,'number_stops']= df.loc[df['id']==i,'stop'].sum()
                    df.loc[df['id']==i,'resting_time']= df.loc[df['id']==i,'stop'].sum()*(1/self.fps)
                    
                    df.loc[df['id']==i,'number_mean_movement']= df.loc[df['id']==i,'mean_movement'].sum()
                    df.loc[df['id']==i,'mean_movement_time']= df.loc[df['id']==i,'mean_movement'].sum()*(1/self.fps)
                    
                    df.loc[df['id']==i,'number_fast_movement']= df.loc[df['id']==i,'fast_movement'].sum()
                    df.loc[df['id']==i,'mean_fast_time']= df.loc[df['id']==i,'fast_movement'].sum()*(1/self.fps)
                    #variable from network
                    df.loc[df['id']==i,'degree']= degrees[i]       
                
                # group variables from network
                df['group_density_network']= group_desity
                
     ###############     regions
                                
                if self.ui.check_regions.isChecked():
                    
                    df['proportions']= 'non'
                    df['region']= 'non'
                    
                    if self.ui.check_regions_ind.isChecked():
                        
                        df['ind_regions'] = 'non'
                        row_n=0
                        for j in (np.unique(df['id'])):   
                        
                            for i in range(0, len(self.bboxes)):
                                roi = self.bboxes[i]
                                
                                #prop = len(df[( df.loc[df['id']==j,'pos_x']  >  roi[0] ) & ( df.loc[df['id']==j,'pos_x'] < roi[0]+roi[2]) & ( df.loc[df['id']==j,'pos_y'] > roi[1]) & ( df.loc[df['id']==j,'pos_y'] < roi[1]+roi[3])]) / len( df.loc[df['id']==j,'pos_x'] )
                                #prop = len(df.loc[( [df['id']==j,'pos_x']  >  roi[0] ) & ( [df['id']==j,'pos_x'] < roi[0]+roi[2]) & ( [df['id']==j,'pos_y'] > roi[1]) & ( [df['id']==j,'pos_y'] < roi[1]+roi[3])]) / len( df.loc[df['id']==j,'pos_x'] )
                                prop = len( df[ (df['id'] ==j) & (df['pos_x'] >  roi[0]) & (df['pos_x'] < roi[0]+roi[2]) & (df['pos_y'] >  roi[1]) & (df['pos_y'] < roi[1]+roi[3]) ]) / len( df[ (df['id'] ==j)])

                                #print('----- The spent ' + str(prop*100) + '% of its time in the selected region of interest -----')
                                
                                df['proportions'][row_n] = str(round(prop*100,4))
                                df['region'][row_n] = str(i)
                                df['ind_regions'][row_n] = str(j)
                                
                                row_n+=1
                    else:
                        
                        for i in range(0, len(self.bboxes)):
                            roi = self.bboxes[i]
                            
                            prop = len(df[(df['pos_x'] > roi[0]) & (df['pos_x'] < roi[0]+roi[2]) & (df['pos_y'] > roi[1]) & (df['pos_y'] < roi[1]+roi[3])]) / len(df['pos_x'])
                            print('----- The spent ' + str(prop*100) + '% of its time in the selected region of interest -----')
                            
                            df['proportions'][i] = str(round(prop*100,4))
                            df['region'][i] = str(i)
                
                df.to_csv(self.filename_parameters_cvs, sep=',')
                #proportions.to_csv(self.filename_parameters_cvs+'proportions.csv', sep=',')
                self.ui.prop_detection.setText(str(1-len(np.where(df['instantaneous_speed'] > 2*np.percentile (df['instantaneous_speed'],95) )[0]) / len(df['frame']) ))
                
                
            except: 
                df.to_csv("auto_saved_data.csv", sep=',')
                self.ui.prop_detection.setText(str(1-len(np.where(df['instantaneous_speed'] > 2*np.percentile (df['instantaneous_speed'],95) )[0]) / len(df['frame'])))
                      
            
        
        cv2.destroyAllWindows()
        
        self.ui.processing.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                            "color: rgb(10, 255, 10);\n"
                            "")
        self.ui.processing.setText('Done!')
        
        
        
    
    
############### compelx ground
        
        
    #make ims for mask
        
    def make_imgs_mask_Event (self, indice):
        self.capturing = True
        
        #countours_amostrados=[]

        listas=[]
        
        lista_id=self.ui.thresh_option.currentIndex()
        if lista_id==0: self.thr_option = False
        else: self.thr_option = True  
        
        
        if str(self.ui.start_img.text()) != '':
            try:
                start_img_num = int(self.ui.start_img.text())
            except:
                start_img_num = 1
        else:
            start_img_num = 1
                
        
        cap = cv2.VideoCapture(self.filename)
        
        
            
            
        if not os.path.exists('make_mask_rcnn_data/mask_imgs/'):
            os.makedirs('make_mask_rcnn_data/mask_imgs/')
        
        
        self.filename_backgrounds_mask = QFileDialog.getExistingDirectory(self,
                                                                          "Open a folder",
                                                                          "~/",
                                                                          QFileDialog.ShowDirsOnly
                                                                                )
        
        
        time.sleep(2.0)
        
        
        if str(self.ui.n_ind.text()) != '':
                self.n_ind = int(self.ui.n_ind.text())
                        
        
        if str(self.ui.tresh_value.text()) != '':
            self.tresh_value = int(self.ui.tresh_value.text())
            
        #if str(self.ui.frame_number.text()) != '':
            #self.frame_number = int(self.ui.frame_number.text())
                
        if str(self.ui.max_area.text()) != '':
            self.max_area = float(self.ui.max_area.text())
                
        if str(self.ui.min_area.text()) != '':
            self.min_area = float(self.ui.min_area.text())
                
        if str(self.ui.max_len.text()) != '':
            self.max_len = float(self.ui.max_len.text())
                
        if str(self.ui.min_len.text()) != '':
            self.min_len = float(self.ui.min_len.text())
                
        if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
            self.frame_resolution = int(self.ui.set_frame_resolution.text())
                
        if str(self.ui.distance_crop.text()) != '':
            self.distance = float(self.ui.distance_crop.text())
            
        if str(self.ui.distance_scale.text()) != '':
            self.distance_scale = float(self.ui.distance_scale.text())
            
        if str(self.ui.distance_scale_know.text()) != '':
            self.distance_scale_know = float(self.ui.distance_scale_know.text())
            
        if str(self.ui.interaction_threshold.text()) != '':
            self.interaction_threshold = float(self.ui.interaction_threshold.text())
            
        if str(self.ui.thersh_min_mov.text()) != '':
            self.thersh_min_mov = float(self.ui.thersh_min_mov.text())
            
        if str(self.ui.thersh_max_mov.text()) != '':
            self.thersh_max_mov = float(self.ui.thersh_max_mov.text())
            
        if str(self.ui.max_prop.text()) != '':
            self.max_prop = float(self.ui.max_prop.text())
            
        if str(self.ui.min_prop.text()) != '':
            self.min_prop = float(self.ui.min_prop.text())
                
        try:
            if str(self.ui.video_time_in_frame.text()) != '' and int(self.ui.video_time_in_frame.text()) in range(1,self.total_frame_number+1,1):
                self.video_time_in_frame = int(self.ui.video_time_in_frame.text())
        except:
            reply = QMessageBox.information( self, "Message", "Failed in computer video size. Check video file path", QMessageBox.Ok)    
            if reply == QMessageBox.Ok:
                self.capturing = False
                pass
        
        

        self.total_frame_number = (int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
        
        frames_amostrados = random.sample(range(int(self.total_frame_number-100)), int(self.total_frame_number-100))
        counter=0    
        
        
        while(self.capturing):
            
            fframe=frames_amostrados[counter]
            
            success, frame = cap.read()
            cap.set(1, fframe)
            
            
            
            if not success:
                
                reply = QMessageBox.information( self, "Message", "Failed to read video. Check video file path", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    self.capturing = False
                    pass            
                
            else:
                
                
                
                lista=self.ui.combo_roi.currentIndex()
                shape_crop_list = self.ui.roi_shape_crop.currentIndex()
                
                frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
           
                if lista==1:
                    if shape_crop_list==0:     
                        
                        
                        
                        if self.distance < 10 and self.crop_xyhw_circle == None:
                            reply = QMessageBox.information( self, "Information", "Distance or center not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            try:
                                x,y,h,w = self.crop_xyhw_circle                               
                                
                                
                                try:                                    
                       #             I = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
                        #            mask = np.zeros((I.shape[0], I.shape[1]))
                                    
                         #           cv2.circle(mask, (x+ int(h/2),  y+ int(w/2)), int(self.distance), 255, -1)                                                                       
                                    
                         #           self.mask=mask  
                         #           frame[self.mask == 0] = (0,0,0)
                                    
                                    frame = frame[y:y+w, x:x+h]
                                    
                                except:
                                    reply = QMessageBox.information( self, "Information", "Probably conflict between resolution and roi.", QMessageBox.Ok)    
                                    if reply == QMessageBox.Ok:
                                        self.capturing = False
                                        break
                                        pass
                                
                                
                                
                            except:
                                reply = QMessageBox.information( self, "Information", "Probably the unselected center.", QMessageBox.Ok)    
                                if reply == QMessageBox.Ok:
                                    self.capturing = False
                                    break
                                    pass
                    else:
                        if self.crop_xyhw_rectangle == None:
                            reply = QMessageBox.information( self, "Information", "ROI not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            x,y,h,w = self.crop_xyhw_rectangle
                            frame = frame[y:w, x:h]
                
                
                
               
            segmentedFrame,framegray = video_back_simple.colour_to_thresh(frame, self.tresh_value,self.kernel,self.kernel1,self.thr_option)
                
            if shape_crop_list==0:
                segmentedFrame= cv2.bitwise_and(segmentedFrame, segmentedFrame, mask=self.mask) 
            
                
                    
            self.contours, self.meas_last, self.meas_now = video_back_simple.detect_and_draw_contours(segmentedFrame,self.meas_last, self.meas_now,self.min_area, self.max_area, self.min_len, self.max_len, self.max_prop,self.min_prop)
                
                      
            
                
                
            out = cv2.imread(self.filename_backgrounds_mask+ "/" + str(counter + start_img_num) + ".jpg")

            out = cv2.resize(out,( frame.shape[1], frame.shape[0]))
                        
                
            mask = np.zeros_like(frame) # Create mask where white is what we want, black otherwise
            cv2.drawContours(mask, self.contours, -1, (255,255,255), -1) # Draw filled contour in mask

            out[mask == (255,255,255)] = frame [mask == (255,255,255)]
    
            #out = cv2.resize(out,( 640, 480))
    
            cv2.imwrite("make_mask_rcnn_data/mask_imgs/" + str(counter + start_img_num) + ".jpg", out)
            
            
            regions_acumulada=[]
            for k in range (0,len(self.contours)):
                                
                contornos_especifico = self.contours[k]
        
                y = [j[0,1] for j in contornos_especifico] 
                x = [j[0,0] for j in contornos_especifico] 
                
                regions={str(k):{"shape_attributes":{"name":"polygon",
                                                     "all_points_x":x,
                                                     "all_points_y":y},
                                 "region_attributes":{}}}
                
                if regions[str(k)] is None:
                    pass
                    
                else:            
                    regions_acumulada.append(regions)
                    
                    
            regions_acumulada_dicionario=regions_acumulada[0]
            for t in range(1,len(regions_acumulada)):
                regions_acumulada_dicionario.update(regions_acumulada[t])
                
                
                
            annotation={
                str(counter+start_img_num) + ".jpg" + str(int(np.prod(out.shape[:3]))) :{"base64_img_data":"",
                                                                                         "file_attributes":{},
                                                                                         "filename":str(counter+start_img_num) + ".jpg",
                                                                                         "fileref":"",
                                                                                         "regions":regions_acumulada_dicionario,
                                                                                         "size":int(np.prod(out.shape[:3]))
                                                                                         }}
                
            counter+=1 
                
            
            listas.append(annotation)
    
            listas_dicionario=listas[0]
            for g in range(1,len(listas)):
                listas_dicionario.update(listas[g])    
                
                
                
                
                
                
            completed = int( (counter/int(self.video_time_in_frame))*100)                
            self.ui.video_progressBar.setValue(completed)  
                                
                
            if counter >= self.video_time_in_frame:
                self.capturing = False
                          
            cv2.waitKey(5)
        
        
        df = pd.DataFrame(listas_dicionario)
        df.to_json(path_or_buf='make_mask_rcnn_data/mask_imgs/via_region_data.json')
        
        
        if self.ui.check_end_video.isChecked():
            os.system('play -nq -t alsa synth {} sine {}'.format(self.duration, self.freq))            
        
    
        
        cv2.destroyAllWindows()

            
                
    
    
        
    
    def video_complex_ground_Event (self, indice):
        
        a=1
        
        def get_ax(rows=1, cols=1, size=16):
                    """Return a Matplotlib Axes array to be used in
                    all visualizations in the notebook. Provide a
                    central point to control graph sizes.
                    
                    Adjust the size attribute to control how big to render images
                    """
                    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
                    return ax
                
                
        
        lista_id=self.ui.thresh_option.currentIndex()
        if lista_id==0: self.thr_option = False
        else: self.thr_option = True          
            
              
        self.ui.processing.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                            "color: rgb(30, 30, 255);\n"
                            "")
        self.ui.processing.setText('Processing ...')
        
       
        
        atual_frame_number= -1 
        self.capturing = True
        write_frame= False
        pts = deque(maxlen=360)
        
        
        if self.ui.check_save_data.isChecked():
            self.filename_parameters_cvs= QFileDialog.getSaveFileName(self,"Save data", "","Comma Separated Value Files (*.csv)")
            self.filename_parameters_cvs = self.filename_parameters_cvs[0]              
        
                
        
        cap = FileVideoStream(self.filename).start()
        time.sleep(1.0)
        
        
                  
        
        #cap = cv2.VideoCapture(self.filename)
        
        if self.ui.check_save_video.isChecked():
            
            write_frame= True
            
            
            if str(self.ui.shape_1.text()) != '' and str(self.ui.shape_0.text()) != '':
                self.shape_1 = int(self.ui.shape_1.text())
                self.shape_0 = int(self.ui.shape_0.text())
                       
            
            codec = 'DIVX' 
            
            fourcc = cv2.VideoWriter_fourcc(*codec)
            output_framesize = (self.shape_1,self.shape_0)
            
            self.filename_parameters_video= QFileDialog.getSaveFileName(self,"Save video", "","mp4 Files (*.mp4)")
            self.filename_parameters_video = self.filename_parameters_video[0]
            
            try:
                out = cv2.VideoWriter(filename = self.filename_parameters_video, fourcc = fourcc,
                                  fps = 30.0, frameSize = output_framesize, isColor = True)
            
            except: 
                out = cv2.VideoWriter(filename = "auto_video_saved.mp4", fourcc = fourcc,
                                  fps = 30.0, frameSize = output_framesize, isColor = True)
            
        
        
        
        
        if str(self.ui.n_ind.text()) != '':
                self.n_ind = int(self.ui.n_ind.text())
        
        colours = []
        #t_id = []        
        for i in range (0, self.n_ind ):
             cor=(randint(0, 255), randint(0, 255), randint(0, 255))
             colours.append(cor)
             
        t_id=random.sample(string.ascii_uppercase, self.n_ind)
        #t_id.append(id_letter)
             
                   
                        
        df = []
        #last = 0
            
        lista_id=self.ui.combo_id.currentIndex()
        if lista_id==0: mot = False
        else: mot = True  
                
        if str(self.ui.tresh_value.text()) != '':
            self.tresh_value = int(self.ui.tresh_value.text())
            
        #if str(self.ui.frame_number.text()) != '':
            #self.frame_number = int(self.ui.frame_number.text())
                
        if str(self.ui.max_area.text()) != '':
            self.max_area = float(self.ui.max_area.text())
                
        if str(self.ui.min_area.text()) != '':
            self.min_area = float(self.ui.min_area.text())
                
        if str(self.ui.max_len.text()) != '':
            self.max_len = float(self.ui.max_len.text())
                
        if str(self.ui.min_len.text()) != '':
            self.min_len = float(self.ui.min_len.text())
                
        if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
            self.frame_resolution = int(self.ui.set_frame_resolution.text())
                
        if str(self.ui.distance_crop.text()) != '':
            self.distance = float(self.ui.distance_crop.text())
            
        if str(self.ui.distance_scale.text()) != '':
            self.distance_scale = float(self.ui.distance_scale.text())
            
        if str(self.ui.distance_scale_know.text()) != '':
            self.distance_scale_know = float(self.ui.distance_scale_know.text())
            
        if str(self.ui.interaction_threshold.text()) != '':
            self.interaction_threshold = float(self.ui.interaction_threshold.text())
            
        if str(self.ui.thersh_min_mov.text()) != '':
            self.thersh_min_mov = float(self.ui.thersh_min_mov.text())
            
        if str(self.ui.thersh_max_mov.text()) != '':
            self.thersh_max_mov = float(self.ui.thersh_max_mov.text())
            
        if str(self.ui.max_prop.text()) != '':
            self.max_prop = float(self.ui.max_prop.text())
            
        if str(self.ui.min_prop.text()) != '':
            self.min_prop = float(self.ui.min_prop.text())
                
        try:
            if str(self.ui.video_time_in_frame.text()) != '' and int(self.ui.video_time_in_frame.text()) in range(1,self.total_frame_number+1,1):
                self.video_time_in_frame = int(self.ui.video_time_in_frame.text())
        except:
            reply = QMessageBox.information( self, "Message", "Failed in computer video size. Check video file path", QMessageBox.Ok)    
            if reply == QMessageBox.Ok:
                self.capturing = False
                pass
        
        

            
        time_ini = datetime.now()    
        while(self.capturing and cap.more()):           
            success= True
            frame = cap.read()
            if not success:
                
                reply = QMessageBox.information( self, "Message", "Failed to read video. Check video file path", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    self.capturing = False
                    pass            
                
            else:
                
                
                atual_frame_number += 1
                
                lista=self.ui.combo_roi.currentIndex()
                shape_crop_list = self.ui.roi_shape_crop.currentIndex()
                
                #if self.frame_resolution != 100:
                frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
           
                ######## tampar algo
                
                #cv2.circle(frame, (866, 169), 9, (255,255,255), -1)
                
                if lista==1:
                    if shape_crop_list==0:     
                        
                        
                        
                        if self.distance < 10 and self.crop_xyhw_circle == None:
                            reply = QMessageBox.information( self, "Information", "Distance or center not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            try:
                                x,y,h,w = self.crop_xyhw_circle                               
                                
                                
                                try:                                    
                                    #frame[self.mask == 0] = (255,255,255)
                                    
                                    frame = frame[y:y+w, x:x+h]
                                    
                                except:
                                    reply = QMessageBox.information( self, "Information", "Probably conflict between resolution and roi.", QMessageBox.Ok)    
                                    if reply == QMessageBox.Ok:
                                        self.capturing = False
                                        break
                                        pass
                                
                                
                                
                            except:
                                reply = QMessageBox.information( self, "Information", "Probably the unselected center.", QMessageBox.Ok)    
                                if reply == QMessageBox.Ok:
                                    self.capturing = False
                                    break
                                    pass
                    else:
                        if self.crop_xyhw_rectangle == None:
                            reply = QMessageBox.information( self, "Information", "ROI not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            x,y,h,w = self.crop_xyhw_rectangle
                            frame = frame[y:w, x:h]
                
                
            
                #cv2.imwrite(str(atual_frame_number+1184)+'.jpg', frame)
                
               
#################################################################### mask rcnn
                
                # Load weights                               
                
                frame_copy=frame
                
                results = self.model_mask.detect([frame], verbose=0)
                
                #ax = get_ax(1)
                r = results[0]        
                
                frame = visualize.display_instances(frame, r['rois'], r['masks'], r['class_ids'], 
                                          ['BG', 'bee'], r['scores'], ax=None,
                                          title="Predictions")
                
                
                
                
                #cv2.imwrite(str(atual_frame_number)+'.jpg', frame)
                
                segmentedFrame,framegray = video_back_simple.colour_to_thresh_complex(frame, self.tresh_value,self.kernel,self.kernel1)# aqui eu entraria com a mask rcnn
                
                
######################################### mask                
                
                if shape_crop_list==0: 
                    segmentedFrame= cv2.bitwise_and(segmentedFrame, segmentedFrame, mask=self.mask)
                
                self.contours, self.meas_last, self.meas_now = video_back_simple.detect_and_draw_contours(segmentedFrame,self.meas_last, self.meas_now,self.min_area, self.max_area, self.min_len, self.max_len, self.max_prop,self.min_prop)
                
                
               
                
                if len(self.meas_now) != self.n_ind:
                    
                    try:
                        contours, self.meas_now = video_back_simple.apply_k_means(self.contours, self.n_ind, self.meas_now)
                        
                    except:
                                                
                        self.ui.processing.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                            "color: rgb(255, 5, 5);\n"
                            "")
                        
                        self.ui.processing.setText('Error: No objects detected. Check restrictions')                       
                                               
                        break
                        
                
                row_ind, col_ind = video_back_simple.hungarian_algorithm(self.meas_last, self.meas_now)
                final, self.meas_now, df = video_back_simple.reorder_and_draw(frame_copy, colours, self.n_ind, col_ind, self.meas_now, df, mot, atual_frame_number, int(frame.shape[0]),int(frame.shape[1]),self.video_time_in_frame,t_id,pts,write_frame)
                            # Create output dataframe
                    
                for i in range(self.n_ind):
                    df.append([atual_frame_number, self.meas_now[i][0], self.meas_now[i][1], t_id[i]])           
                                  
                completed = int( (atual_frame_number/int(self.video_time_in_frame))*100)
                
                self.ui.processed_frame_number.display(str(atual_frame_number)) 
                
                self.ui.video_progressBar.setValue(completed)
                            
                if self.ui.check_save_video.isChecked():
                    out.write(final)
                    
                    
                if self.ui.show_video_processing.isChecked():
                    write_frame= True
                    #cv2.putText(final, "Queue Size: {}".format(cap.Q.qsize()),
                               # (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    
                    escala = min(600./frame.shape[0], 600./frame.shape[1]) 
                    largura_window = int(frame.shape[1] * escala)
                    altura_window = int(frame.shape[0] * escala)
                    cv2.namedWindow('Ethoflow', cv2.WINDOW_NORMAL)
                    cv2.resizeWindow('Ethoflow', largura_window, altura_window)
                    cv2.imshow('Ethoflow', final)
                                               
                
                if atual_frame_number >= self.video_time_in_frame:
                    self.capturing = False
                          
                            
                 
                
                #cv2.imshow('Running...',cv2.resize(frame, (0,0), fy= round(520/frame.shape[1],1), fx= round(520/frame.shape[0],1)))
                cv2.waitKey(1)
        #last = atual_frame_number
        cap.stop()
        
        try:           
            
            time_end = datetime.now()
            spent_time = str(time_end-time_ini)
            spent_time=spent_time.split(":")
            self.ui.display_spent_time.setText( str(spent_time[0]) + ":" + str(spent_time[1]) + ":" + str(spent_time[2]) )
            
        except:
            self.ui.display_spent_time.setText(str(1))
        
        
        if self.ui.check_end_video.isChecked():
            
            os.system('play -nq -t alsa synth {} sine {}'.format(self.duration, self.freq))
            
           
        
        df = pd.DataFrame(np.matrix(df), columns = ['frame','pos_x','pos_y', 'id'])
        
        
        
        if self.ui.check_save_data.isChecked():
            
            try: 
                df.to_csv(self.filename_parameters_cvs, sep=',')
                df = pd.read_csv(self.filename_parameters_cvs)
                
                prop = self.distance_scale/self.distance_scale_know
                
                df = pd.read_csv(self.filename_parameters_cvs)     
                df = df.drop(columns=['Unnamed: 0'])
                
                df['dir_x'] = df['pos_x'] - df['pos_x'].shift(self.n_ind)
                df['dir_y'] = df['pos_y'] - df['pos_y'].shift(self.n_ind)
                df['speed'] = np.sqrt(df['dir_x']**2 + df['dir_y']**2)
                df['dir_x'] /= df['speed']
                df['dir_y'] /= df['speed']
                
                df['time'] = df['frame'] / self.fps
                
                df = df.rename(index=str, columns={'speed':'distance_pixel'})
                
                
                #### network
                comb =(combinations(np.array(np.unique(df['id'])), 2) )                
                individuals_pars=[]
                encounters_pars=[]
                for i in (comb): 
                   
                    x_1=np.array(df.loc[df['id']==i[0],'pos_x'])
                    x_2=np.array(df.loc[df['id']==i[1],'pos_x'])
                
                    y_1=np.array(df.loc[df['id']==i[0],'pos_y'])
                    y_2=np.array(df.loc[df['id']==i[1],'pos_y'])
                
                    dist_x = x_1 - x_2
                    dist_y = y_1 - y_2
                
                    dist_between = (np.sqrt(dist_x**2 + dist_y**2))/prop #cm
                        
                    individuals_pars.append(i)
                    encounters_pars.append(len(dist_between[dist_between<= self.interaction_threshold]))
                    
                    
                G = nx.MultiGraph() # permite adicionar mais varias bordas para o mesmo par de borda
                S = nx.Graph()
                for t, ind in enumerate(np.array(np.unique(df['id']))):
                    G.add_node(ind)
                    S.add_node(ind)
                
                for i in range(0, len(encounters_pars)):
                        if encounters_pars[i]>0:
                            S.add_edge(individuals_pars[i][0], individuals_pars[i][1],weights= encounters_pars[i])
                            for j in range (0, encounters_pars[i]):
                                G.add_edge(individuals_pars[i][0], individuals_pars[i][1])
                
                degrees = G.degree()
                group_desity = nx.density(G)
                
                nx.write_gml(S,self.filename_parameters_cvs + '.gml')
                #######
                df['distance'] = df['distance_pixel']/prop # (cm)

                df['instantaneous_speed'] = df['distance'] * self.fps
                df['instantaneous_acceleration'] = df['instantaneous_speed'] - df['instantaneous_speed'].shift(self.n_ind)
                
                rad=(np.arctan2(np.array(df['dir_x']) , np.array(df['dir_y'])))*180                
                df['turning_angle'] = rad /np.pi                
                
                df['stop']=0
                df['mean_movement']=0
                df['fast_movement']=0
                
                df['stop'][df['distance']<self.thersh_min_mov]=1
                df['mean_movement'][ (df['distance'] >=self.thersh_min_mov) & (df['distance'] <= self.thersh_max_mov) ] = 1
                df['fast_movement'][df['distance']>self.thersh_max_mov]=1
                
                ################################# smoothed

                df = df.replace([np.inf, -np.inf], np.nan).dropna(axis=0, how="any")
                
                df['smoothed_distance'] = scipy.signal.savgol_filter(df['distance'], 9, 1)
                df['smoothed_instantaneous_speed'] = scipy.signal.savgol_filter(df['instantaneous_speed'], 9, 1)
                df['smoothed_instantaneous_acceleration'] = scipy.signal.savgol_filter(df['instantaneous_acceleration'], 9, 1)
                df['smoothed_turning_angle'] = scipy.signal.savgol_filter(df['turning_angle'], 9, 1)
                
                
                ################################# mean variables

                for i in (np.unique(df['id'])):
                    
                    df.loc[df['id']==i,'individuals']= i 
                    sum_dist=df.loc[df['id']==i,'distance'].sum()    
                    df.loc[df['id']==i,'tracked_distance']= sum_dist # (cm)
                    
                    # average_speed
                    df.loc[df['id']==i,'mean_speed']= sum_dist /df['time'].max() # (cm/s)
                    # max speed
                    df.loc[df['id']==i,'max_speed']= df.loc[df['id']==i,'instantaneous_speed'].max() # (cm/s)
                    
                    df.loc[df['id']==i,'mean_turn_angle']= abs(df.loc[df['id']==i,'turning_angle']).mean()# (graus)
                    df.loc[df['id']==i,'meandering']= abs(df.loc[df['id']==i,'turning_angle']).sum()/sum_dist # (graus/cm)
                    df.loc[df['id']==i,'number_stops']= df.loc[df['id']==i,'stop'].sum()
                    df.loc[df['id']==i,'resting_time']= df.loc[df['id']==i,'stop'].sum()*(1/self.fps)
                    
                    df.loc[df['id']==i,'number_mean_movement']= df.loc[df['id']==i,'mean_movement'].sum()
                    df.loc[df['id']==i,'mean_movement_time']= df.loc[df['id']==i,'mean_movement'].sum()*(1/self.fps)
                    
                    df.loc[df['id']==i,'number_fast_movement']= df.loc[df['id']==i,'fast_movement'].sum()
                    df.loc[df['id']==i,'mean_fast_time']= df.loc[df['id']==i,'fast_movement'].sum()*(1/self.fps)
                    #variable from network
                    df.loc[df['id']==i,'degree']= degrees[i]       
                
                # group variables from network
                df['group_density_network']= group_desity
                
     ###############     regions
                                
                if self.ui.check_regions.isChecked():
                    
                    df['proportions']= 'non'
                    df['region']= 'non'
                    
                    if self.ui.check_regions_ind.isChecked():
                        
                        df['ind_regions'] = 'non'
                        row_n=0
                        for j in (np.unique(df['id'])):   
                        
                            for i in range(0, len(self.bboxes)):
                                roi = self.bboxes[i]
                                
                                #prop = len(df[( df.loc[df['id']==j,'pos_x']  >  roi[0] ) & ( df.loc[df['id']==j,'pos_x'] < roi[0]+roi[2]) & ( df.loc[df['id']==j,'pos_y'] > roi[1]) & ( df.loc[df['id']==j,'pos_y'] < roi[1]+roi[3])]) / len( df.loc[df['id']==j,'pos_x'] )
                                #prop = len(df.loc[( [df['id']==j,'pos_x']  >  roi[0] ) & ( [df['id']==j,'pos_x'] < roi[0]+roi[2]) & ( [df['id']==j,'pos_y'] > roi[1]) & ( [df['id']==j,'pos_y'] < roi[1]+roi[3])]) / len( df.loc[df['id']==j,'pos_x'] )
                                prop = len( df[ (df['id'] ==j) & (df['pos_x'] >  roi[0]) & (df['pos_x'] < roi[0]+roi[2]) & (df['pos_y'] >  roi[1]) & (df['pos_y'] < roi[1]+roi[3]) ]) / len( df[ (df['id'] ==j)])

                                #print('----- The spent ' + str(prop*100) + '% of its time in the selected region of interest -----')
                                
                                df['proportions'][row_n] = str(round(prop*100,4))
                                df['region'][row_n] = str(i)
                                df['ind_regions'][row_n] = str(j)
                                
                                row_n+=1
                    else:
                        
                        for i in range(0, len(self.bboxes)):
                            roi = self.bboxes[i]
                            
                            prop = len(df[(df['pos_x'] > roi[0]) & (df['pos_x'] < roi[0]+roi[2]) & (df['pos_y'] > roi[1]) & (df['pos_y'] < roi[1]+roi[3])]) / len(df['pos_x'])
                            print('----- The spent ' + str(prop*100) + '% of its time in the selected region of interest -----')
                            
                            df['proportions'][i] = str(round(prop*100,4))
                            df['region'][i] = str(i)
                
                df.to_csv(self.filename_parameters_cvs, sep=',')
                #proportions.to_csv(self.filename_parameters_cvs+'proportions.csv', sep=',')
                self.ui.prop_detection.setText(str(1-len(np.where(df['instantaneous_speed'] > 2*np.percentile (df['instantaneous_speed'],95) )[0]) / len(df['frame']) ))
                
                
            except: 
                df.to_csv("auto_saved_data.csv", sep=',')
                self.ui.prop_detection.setText(str(1-len(np.where(df['instantaneous_speed'] > 2*np.percentile (df['instantaneous_speed'],95) )[0]) / len(df['frame'])))
                      
            
        
        cv2.destroyAllWindows()
        
        self.ui.processing.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                            "color: rgb(10, 255, 10);\n"
                            "")
        self.ui.processing.setText('Done!')
        
        
        
        

#############################################################
        ################################################ behaviour - trof

    def stimates_event(self):        
    
        
        lista_id=self.ui.thresh_option.currentIndex()
        if lista_id==0: self.thr_option = False
        else: self.thr_option = True  
        
        
        self.capturing = True
        
        estimated_proportion=[]
        estimated_len=[]
        estimated_area=[]               
        
        cap = cv2.VideoCapture(self.filename)
        
        if self.ui.check_save_video.isChecked():
            
            
            if str(self.ui.shape_1.text()) != '' and str(self.ui.shape_0.text()) != '':
                self.shape_1 = int(self.ui.shape_1.text())
                self.shape_0 = int(self.ui.shape_0.text())
                       
            
                      
            
            self.filename_parameters_video= QFileDialog.getSaveFileName(self,"Save video", "","mp4 Files (*.mp4)")
            self.filename_parameters_video = self.filename_parameters_video[0]
            
            
            
        
        self.total_frame_number = (int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
        
        
        if str(self.ui.n_ind.text()) != '':
                self.n_ind = int(self.ui.n_ind.text())
        
        colours = []
        #t_id = []        
        for i in range (0, self.n_ind ):
             cor=(randint(0, 255), randint(0, 255), randint(0, 255))
             colours.append(cor)
             
            
        
                
        if str(self.ui.tresh_value.text()) != '':
            self.tresh_value = int(self.ui.tresh_value.text())
            
        #if str(self.ui.frame_number.text()) != '':
            #self.frame_number = int(self.ui.frame_number.text())
                
        if str(self.ui.max_area.text()) != '':
            self.max_area = float(self.ui.max_area.text())
                
        if str(self.ui.min_area.text()) != '':
            self.min_area = float(self.ui.min_area.text())
                
        if str(self.ui.max_len.text()) != '':
            self.max_len = float(self.ui.max_len.text())
                
        if str(self.ui.min_len.text()) != '':
            self.min_len = float(self.ui.min_len.text())
                
        if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
            self.frame_resolution = int(self.ui.set_frame_resolution.text())
                
        if str(self.ui.distance_crop.text()) != '':
            self.distance = float(self.ui.distance_crop.text())
            
        if str(self.ui.max_prop.text()) != '':
            self.max_prop = float(self.ui.max_prop.text())
        if str(self.ui.min_prop.text()) != '':
            self.min_prop = float(self.ui.min_prop.text())
            
                
        try:
            if str(self.ui.n_amostrad_frame.text()) != '' and int(self.ui.n_amostrad_frame.text()) in range(1,self.total_frame_number+1,1):
                self.n_amostrad_frame = int(self.ui.n_amostrad_frame.text())
        except:
            reply = QMessageBox.information( self, "Message", "Failed in computer video size. Check video file path", QMessageBox.Ok)    
            if reply == QMessageBox.Ok:
                self.capturing = False
                pass

        
        
        time_ini = datetime.now()    
        while(self.capturing):           
            success, frame = cap.read()
            if not success:
                
                reply = QMessageBox.information( self, "Message", "Failed to read video. Check video file path", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    self.capturing = False
                    pass            
                
            else:
                
                atual_frame_number = cap.get(1)
                
                
                lista=self.ui.combo_roi.currentIndex()
                shape_crop_list = self.ui.roi_shape_crop.currentIndex()
                
                frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
           
                if lista==1:
                    if shape_crop_list==0:     
                        
                        
                        if self.distance < 10 and self.crop_xyhw_circle == None:
                            reply = QMessageBox.information( self, "Information", "Distance or center not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            try:
                                x,y,h,w = self.crop_xyhw_circle                               
                                
                                
                                try:                                    
                                    
                                    frame = frame[y:y+w, x:x+h]
                                    
                                    
                                except:
                                    reply = QMessageBox.information( self, "Information", "Probably conflict between resolution and roi.", QMessageBox.Ok)    
                                    if reply == QMessageBox.Ok:
                                        self.capturing = False
                                        break
                                        pass
                                
                                
                                
                            except:
                                reply = QMessageBox.information( self, "Information", "Probably the unselected center.", QMessageBox.Ok)    
                                if reply == QMessageBox.Ok:
                                    self.capturing = False
                                    break
                                    pass
                    else:
                        if self.crop_xyhw_rectangle == None:
                            reply = QMessageBox.information( self, "Information", "ROI not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            x,y,h,w = self.crop_xyhw_rectangle
                            frame = frame[y:w, x:h]
                
                
                
               
                
                ######## tentar usar chamando function                  
                
                segmentedFrame,frameGray = video_back_simple.colour_to_thresh(frame, self.tresh_value,self.kernel,self.kernel1,self.thr_option)
                
                if shape_crop_list==0:
                    segmentedFrame= cv2.bitwise_and(segmentedFrame, segmentedFrame, mask=self.mask)
                
                bounding_boxes, miniframes, centroids, \
                        areas, pixels, contours, estimated_body_lengths, countours_got, body_proportions = blob_extractor(segmentedFrame,
                                                                                                        segmentedFrame,
                                                                                                        self.min_area,
                                                                                                        self.max_area,
                                                                                                        self.min_len,
                                                                                                        self.max_len,
                                                                                                        self.max_prop,
                                                                                                        self.min_prop)
            
                for i in range(0,len(contours)):
                    estimated_proportion.append(body_proportions[i])
                
                                                
                
                
                if len(centroids)== self.n_ind:
                    estimated_len.append(estimated_body_lengths)
                    estimated_area.append(areas)
                    
                
                try:
                     
                    self.ui.stimated_len.setText( str(  round(np.median(estimated_len), 2)  ))
                    self.ui.stimated_area.setText( str(  round(np.median(estimated_area),2 ) ))
                    self.ui.stimated_sd_len.setText( str( round(np.std(estimated_len),2) ))
                    self.ui.stimated_sd_area.setText( str( round(np.std(estimated_area),2) ))
                    
                    self.ui.body_prop.setText( str( round(np.median(estimated_proportion) , 2)  ))
                    self.ui.sd_body_prop.setText( str( round(np.std(estimated_proportion),2) ))
                    
                    
                    
                    self.min_len_est = (2* np.median(estimated_len)) - (2* np.std(estimated_len))
                    self.max_len_est = (2* np.median(estimated_len)) + (2* np.std(estimated_len))
                    
                    self.min_area_est = (2* np.median(estimated_area)) - (2* np.std(estimated_area))
                    self.max_area_est = (2* np.median(estimated_area)) + (2* np.std(estimated_area))
                    
                except:
                    reply = QMessageBox.information( self, "Information", "some error.", QMessageBox.Ok)    
                    if reply == QMessageBox.Ok:
                        self.capturing = False
                        break
                        pass 
                
                              
                completed = int( (atual_frame_number/int(self.n_amostrad_frame))*100)                
                self.ui.stimate_progressBar.setValue(completed)
                        
                               
                            
                
                                
                
                if atual_frame_number >= self.n_amostrad_frame:
                    self.capturing = False                          
                            
                 
                
                cv2.waitKey(5)   
               
            
        try:
            
            
            time_end = datetime.now()
            spent_time = str(time_end-time_ini)
            spent_time=spent_time.split(":")
            #print(str(spent_time[0]) + ":" + str(spent_time[1]) + ":" + str(spent_time[2]))
            
                                               
            self.ui.display_spent_time_meansure.setText( str(spent_time[0]) + ":" + str(spent_time[1]) + ":" + str(spent_time[2]) )
            
        except:
            self.ui.display_spent_time_meansure.setText(str(1))
            
        
        cv2.destroyAllWindows()
        
        
        
    def make_imgs_train_behavior_event(self):        
        
        
        lista_id=self.ui.thresh_option.currentIndex()
        if lista_id==0: self.thr_option = False
        else: self.thr_option = True  
        
        
        self.capturing = True
        
        if not os.path.exists('./train_imgs_behaviour/1/'):
            os.makedirs('./train_imgs_behaviour/1/')
            
        if not os.path.exists('./train_imgs_behaviour/2/'):
            os.makedirs('./train_imgs_behaviour/2/')                     
        
        cap = cv2.VideoCapture(self.filename)       
        
            
            
        if str(self.ui.shape_1.text()) != '' and str(self.ui.shape_0.text()) != '':
            self.shape_1 = int(self.ui.shape_1.text())
            self.shape_0 = int(self.ui.shape_0.text())  
            
        
        self.total_frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        #self.total_frame_number
        
        frames_amostrados = random.sample(range(int(self.total_frame_number-100)), int(self.total_frame_number-100))
        counter=0
        beh1_countours=[]
        beh2_countours=[]
        
        if str(self.ui.n_ind.text()) != '':
                self.n_ind = int(self.ui.n_ind.text())   
        
                
        if str(self.ui.tresh_value.text()) != '':
            self.tresh_value = int(self.ui.tresh_value.text())
            
        #if str(self.ui.frame_number.text()) != '':
            #self.frame_number = int(self.ui.frame_number.text())
                
        if str(self.ui.max_area.text()) != '':
            self.max_area = float(self.ui.max_area.text())
                
        if str(self.ui.min_area.text()) != '':
            self.min_area = float(self.ui.min_area.text())
                
        if str(self.ui.max_len.text()) != '':
            self.max_len = float(self.ui.max_len.text())
                
        if str(self.ui.min_len.text()) != '':
            self.min_len = float(self.ui.min_len.text())
                
        if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
            self.frame_resolution = int(self.ui.set_frame_resolution.text())
                
        if str(self.ui.distance_crop.text()) != '':
            self.distance = float(self.ui.distance_crop.text())
            
        if str(self.ui.n_behaviour_1.text()) != '':
            self.n_behaviour_1 = int(self.ui.n_behaviour_1.text())

        if str(self.ui.max_prop.text()) != '':
            self.max_prop = float(self.ui.max_prop.text())
        if str(self.ui.min_prop.text()) != '':
            self.min_prop = float(self.ui.min_prop.text())               
        
        
        
        time_ini = datetime.now()    
        while(self.capturing):
            
            fframe=frames_amostrados[counter]
            
            success, frame = cap.read()
            cap.set(1, fframe)
            if not success:
                
                reply = QMessageBox.information( self, "Message", "Failed to read video. Check video file path", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    self.capturing = False
                    pass            
                
            else:
                                                
                lista=self.ui.combo_roi.currentIndex()
                shape_crop_list = self.ui.roi_shape_crop.currentIndex()
                
                frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
           
                if lista==1:
                    if shape_crop_list==0:     
                        
                        
                        if self.distance < 10 and self.crop_xyhw_circle == None:
                            reply = QMessageBox.information( self, "Information", "Distance or center not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            try:
                                x,y,h,w = self.crop_xyhw_circle                               
                                
                                
                                try:                                    
                                    
                                    frame = frame[y:y+w, x:x+h]
                                    
                                except:
                                    reply = QMessageBox.information( self, "Information", "Probably conflict between resolution and roi.", QMessageBox.Ok)    
                                    if reply == QMessageBox.Ok:
                                        self.capturing = False
                                        break
                                        pass
                                
                                
                                
                            except:
                                reply = QMessageBox.information( self, "Information", "Probably the unselected center.", QMessageBox.Ok)    
                                if reply == QMessageBox.Ok:
                                    self.capturing = False
                                    break
                                    pass
                    else:
                        if self.crop_xyhw_rectangle == None:
                            reply = QMessageBox.information( self, "Information", "ROI not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            x,y,h,w = self.crop_xyhw_rectangle
                            frame = frame[y:w, x:h]
                
                
                
               
                
                ######## tentar usar chamando function
                counter+=1                   
                
                segmentedFrame,frameGray = video_back_simple.colour_to_thresh(frame, self.tresh_value,self.kernel,self.kernel1, self.thr_option)# aqui eu entraria com a mask rcnn
                
                
                if shape_crop_list==0: 
                    segmentedFrame= cv2.bitwise_and(segmentedFrame, segmentedFrame, mask=self.mask)
                
                
                
                
                
                
                bounding_boxes, miniframes, centroids, \
                        areas, pixels, contours, estimated_body_lengths, countours_got, body_proportions = blob_extractor(segmentedFrame,
                                                                                                        frameGray,
                                                                                                        self.min_area,
                                                                                                        self.max_area,
                                                                                                        self.min_len,
                                                                                                        self.max_len,
                                                                                                        self.max_prop,
                                                                                                        self.min_prop)
            
                
                for i in range(0, len(contours)):
                    #estimated_body_lengths[i] >= self.min_len_est and estimated_body_lengths[i] <= self.max_len_est and areas[i] >= self.min_area_est and areas[i] <= self.min_area_est
                    if estimated_body_lengths[i] >= self.min_len_est and estimated_body_lengths[i] <= self.max_len_est and areas[i] >= self.min_area_est and areas[i] <= self.max_area_est:
                              
                        cv2.imwrite('./train_imgs_behaviour/1/' +str(len(beh1_countours))+'.png', miniframes[i])
                        beh1_countours.append(contours[i])
                    else:
                        if len(beh2_countours) < int(self.ui.n_behaviour_2.text()):
                            cv2.imwrite('./train_imgs_behaviour/2/' +str(len(beh2_countours))+'.png', miniframes[i])
                            beh2_countours.append(contours[i])
                    
                                       
               
                                              
                completed = int( (len(beh1_countours)/self.n_behaviour_1)*100)                
                self.ui.stimate_progressBar.setValue(completed)
                
                if len(beh1_countours) >= self.n_behaviour_1:                
                    self.capturing = False                          
                            
                 
                
                cv2.waitKey(5)   
               
            
        try:
            
            
            time_end = datetime.now()
            spent_time = str(time_end-time_ini)
            spent_time=spent_time.split(":")
            #print(str(spent_time[0]) + ":" + str(spent_time[1]) + ":" + str(spent_time[2]))
            
                                               
            self.ui.display_spent_time_meansure.setText( str(spent_time[0]) + ":" + str(spent_time[1]) + ":" + str(spent_time[2]) )
            
        except:
            self.ui.display_spent_time_meansure.setText(str(1))
            
        
        cv2.destroyAllWindows()
        

    def upload_model_event (self):
        self.filename_model= QFileDialog.getOpenFileName(self,"Upload AI file", "","Model instance (*.h5)")
        
        self.filename_model=self.filename_model[0]
        
        self.model = load_model(self.filename_model)
        
        
        
######## run video in network

    def run_behaviour_event(self):    
    
        lista_id=self.ui.thresh_option.currentIndex()
        if lista_id==0: self.thr_option = False
        else: self.thr_option = True  
        
        
        atual_frame_number = 0
        self.capturing = True
        
        trofalax_count=0
        sum_countours=0               
        
        #cap = cv2.VideoCapture(self.filename)
        
        cap = FileVideoStream(self.filename).start()
        time.sleep(1.0)
        
        if self.ui.check_save_video.isChecked():
            
            
            if str(self.ui.shape_1.text()) != '' and str(self.ui.shape_0.text()) != '':
                self.shape_1 = int(self.ui.shape_1.text())
                self.shape_0 = int(self.ui.shape_0.text())
                       
            
                      
            
            self.filename_parameters_video= QFileDialog.getSaveFileName(self,"Save video", "","mp4 Files (*.mp4)")
            self.filename_parameters_video = self.filename_parameters_video[0]
            
            
            
        
        #self.total_frame_number = (int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
        
        
        if str(self.ui.n_ind.text()) != '':
                self.n_ind = int(self.ui.n_ind.text())
        
        colours = []
        #t_id = []        
        for i in range (0, self.n_ind ):
             cor=(randint(0, 255), randint(0, 255), randint(0, 255))
             colours.append(cor)
             
            
        
                
        if str(self.ui.tresh_value.text()) != '':
            self.tresh_value = int(self.ui.tresh_value.text())
            
        #if str(self.ui.frame_number.text()) != '':
            #self.frame_number = int(self.ui.frame_number.text())
                
        if str(self.ui.max_area.text()) != '':
            self.max_area = float(self.ui.max_area.text())
                
        if str(self.ui.min_area.text()) != '':
            self.min_area = float(self.ui.min_area.text())
                
        if str(self.ui.max_len.text()) != '':
            self.max_len = float(self.ui.max_len.text())
                
        if str(self.ui.min_len.text()) != '':
            self.min_len = float(self.ui.min_len.text())
                
        if str(self.ui.set_frame_resolution.text()) != '' and int(self.ui.set_frame_resolution.text()) in range(1,101,1):
            self.frame_resolution = int(self.ui.set_frame_resolution.text())
                
        if str(self.ui.distance_crop.text()) != '':
            self.distance = float(self.ui.distance_crop.text())
            
        if str(self.ui.max_prop.text()) != '':
            self.max_prop = float(self.ui.max_prop.text())
        if str(self.ui.min_prop.text()) != '':
            self.min_prop = float(self.ui.min_prop.text())
            
                
        try:
            if str(self.ui.n_amostrad_frame.text()) != '' and int(self.ui.n_amostrad_frame.text()) in range(1,self.total_frame_number+1,1):
                self.n_amostrad_frame = int(self.ui.n_amostrad_frame.text())
        except:
            reply = QMessageBox.information( self, "Message", "Failed in computer video size. Check video file path", QMessageBox.Ok)    
            if reply == QMessageBox.Ok:
                self.capturing = False
                pass

        
        
        time_ini = datetime.now()
        
        while(self.capturing and cap.more()):           
            success= True
            frame = cap.read()
        
        
        #while(self.capturing):           
         #   success, frame = cap.read()
            if not success:
                
                reply = QMessageBox.information( self, "Message", "Failed to read video. Check video file path", QMessageBox.Ok)    
                if reply == QMessageBox.Ok:
                    self.capturing = False
                    pass            
                
            else:
                
                atual_frame_number += 1
                
                
                lista=self.ui.combo_roi.currentIndex()
                shape_crop_list = self.ui.roi_shape_crop.currentIndex()
                
                
                
                frame = cv2.resize(frame,( int((frame.shape[1] * self.frame_resolution)/100),
                                          int((frame.shape[0] * self.frame_resolution)/100)))
           
                if lista==1:
                    if shape_crop_list==0:     
                        
                        
                        if self.distance < 10 and self.crop_xyhw_circle == None:
                            reply = QMessageBox.information( self, "Information", "Distance or center not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            try:
                                x,y,h,w = self.crop_xyhw_circle                               
                                
                                
                                try:                                    
                                    
                                    frame = frame[y:y+w, x:x+h]
                                    
                                    
                                except:
                                    reply = QMessageBox.information( self, "Information", "Probably conflict between resolution and roi.", QMessageBox.Ok)    
                                    if reply == QMessageBox.Ok:
                                        self.capturing = False
                                        break
                                        pass
                                
                                
                                
                            except:
                                reply = QMessageBox.information( self, "Information", "Probably the unselected center.", QMessageBox.Ok)    
                                if reply == QMessageBox.Ok:
                                    self.capturing = False
                                    break
                                    pass
                    else:
                        if self.crop_xyhw_rectangle == None:
                            reply = QMessageBox.information( self, "Information", "ROI not set correctly", QMessageBox.Ok)    
                            if reply == QMessageBox.Ok:
                                self.capturing = False
                                break
                                pass
                        else:
                            x,y,h,w = self.crop_xyhw_rectangle
                            frame = frame[y:w, x:h]
                
                
                
               
                
               
                
                segmentedFrame,frameGray = video_back_simple.colour_to_thresh(frame, self.tresh_value,self.kernel,self.kernel1,self.thr_option)# aqui eu entraria com a mask rcnn
                
                if shape_crop_list==0:
                    segmentedFrame= cv2.bitwise_and(segmentedFrame, segmentedFrame, mask=self.mask)
                
                bounding_boxes, miniframes, centroids, \
                        areas, pixels, contours, estimated_body_lengths, countours_got, body_proportions = blob_extractor(segmentedFrame,
                                                                                                        segmentedFrame,
                                                                                                        self.min_area,
                                                                                                        self.max_area,
                                                                                                        self.min_len,
                                                                                                        self.max_len,
                                                                                                        self.max_prop,
                                                                                                        self.min_prop)
            
                
                
                sum_countours += len(centroids)
                
                if len(centroids) > 1 and len(centroids) < self.n_ind:
                     for l in range(0,len(contours)):
                         
                         img=cv2.cvtColor(miniframes[l],cv2.COLOR_GRAY2BGR)
                         img = cv2.resize(img, (124, 124))
                         img = img_to_array(img)
                         img = np.array(img, dtype="float") / 255.0
                         img = np.reshape(img,[1,124,124,3])
                        
                         preds = self.model.predict_classes(img)
                         
                         
                         if preds == 0:
                             
                             trofalax_count +=1 
                                                                    
    
                
                completed = int( (atual_frame_number/int(self.n_amostrad_frame))*100)                
                self.ui.stimate_progressBar.setValue(completed)
                        
                               
                            
                
                if atual_frame_number >= self.n_amostrad_frame:
                    self.capturing = False                          
                            
                 
                
                cv2.waitKey(1)   
               
            
        try:
            
            
            time_end = datetime.now()
            spent_time = str(time_end-time_ini)
            spent_time=spent_time.split(":")
            #print(str(spent_time[0]) + ":" + str(spent_time[1]) + ":" + str(spent_time[2]))
            
                                               
            self.ui.display_spent_time_meansure.setText( str(spent_time[0]) + ":" + str(spent_time[1]) + ":" + str(spent_time[2]) )
            
        except:
            self.ui.display_spent_time_meansure.setText(str(1))
            
        
        beha_porc = (trofalax_count/sum_countours)*100
        self.ui.percent_behviour_ocorred.setText(str( round(beha_porc,2 ) ))
        
        cap.stop()
        
        
        os.system('play -nq -t alsa synth {} sine {}'.format(self.duration, self.freq))
        
        cv2.destroyAllWindows()
        
        
        
        
        

#Executa a interface
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())