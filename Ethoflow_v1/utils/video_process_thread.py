"""
See readme for information about this file.
Ethoflow: computer vision and artificial intelligence-based software for automatic behavior analysis
v 1.0

DOI: 10.1101/2020.07.23.218255
LicenseCC BY-NC-ND 4.0

@developer: Rodrigo Cupertino Bernardes
https://www.researchgate.net/profile/Rodrigo_Cupertino_Bernardes
"""
import numpy as np
import cv2
from threading import Thread
from queue import Queue
from utils import video_back_simple

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
                                        
                        cv2.circle(mask, (self.x+ int(self.h/2),  self.y+ int(self.w/2)), self.distance, 255, -1)                                                                       
                                        
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
