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
#import pandas as pd
import cv2
from sklearn.cluster import KMeans
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
from scipy import ndimage
#from collections import deque

backSub = cv2.createBackgroundSubtractorMOG2()

def colour_to_thresh(frame,threshold,kernel,kernel1,thr_option):
    
    #B, G, R = cv2.split(frame)
    
    XYZ=cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
    
    x, y, z = cv2.split(XYZ)
    
    
   # R=cv2.equalizeHist(x)
    #R=x
    gray=x
    
    gray_nor=((gray.copy()/np.mean(gray)))

    gray_nor=(gray_nor-gray_nor.min())/(gray_nor.max()-gray_nor.min())*255
    gray_nor = np.uint8(gray_nor)
                
    R=cv2.medianBlur(gray_nor,5)
    #R = cv2.blur( R,(21,17))
    
    
    
    if thr_option == False:
        ret1, R_bin_otsu = cv2.threshold(R,threshold,255,cv2.THRESH_BINARY_INV)
    else:
        ret1, R_bin_otsu = cv2.threshold(R,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
                  
     
    otsu_fechada=cv2.morphologyEx(R_bin_otsu,cv2.MORPH_CLOSE,kernel)
    #otsu_semborda=otsu_fechada
    otsu_gradiente = cv2.morphologyEx(otsu_fechada,cv2.MORPH_GRADIENT,kernel1)     
    otsu_semborda = otsu_fechada -otsu_gradiente
                
    otsu_semborda = np.uint8(otsu_semborda) 
    otsu_semborda=cv2.morphologyEx(otsu_semborda,cv2.MORPH_ERODE,kernel1)
    
               ###########################################################
    


    
    segmentedFrame = otsu_semborda

           
	
    return segmentedFrame ,gray
    



def colour_to_thresh_backsubtract(frame,threshold,kernel,kernel1,thr_option):
    
    #B, G, R = cv2.split(frame)
    
    XYZ=cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
    
    x, y, z = cv2.split(XYZ)
    
    
   # R=cv2.equalizeHist(x)
    R=x
    gray=R
    
    gray_nor=((gray.copy()/np.mean(gray)))

    gray_nor=(gray_nor-gray_nor.min())/(gray_nor.max()-gray_nor.min())*255
    gray_nor = np.uint8(gray_nor)
                
    R=cv2.medianBlur(gray_nor,5)
    
    
    
    
    if thr_option == False:
        ret1, R_bin_otsu = cv2.threshold(R,threshold,255,cv2.THRESH_BINARY_INV)
    else:
        ret1, R_bin_otsu = cv2.threshold(R,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
                  
     
    otsu_fechada=cv2.morphologyEx(R_bin_otsu,cv2.MORPH_CLOSE,kernel)
    #otsu_semborda=otsu_fechada
    otsu_gradiente = cv2.morphologyEx(otsu_fechada,cv2.MORPH_GRADIENT,kernel1)     
    otsu_semborda = otsu_fechada -otsu_gradiente
                
    otsu_semborda = np.uint8(otsu_semborda) 
    otsu_semborda=cv2.morphologyEx(otsu_semborda,cv2.MORPH_ERODE,kernel1)
    
               ###########################################################
    fgMask = backSub.apply(x)
    
    ret1, fgMask =cv2.threshold(fgMask,190,255,cv2.THRESH_BINARY)

    #thresh= (otsu_semborda+fgMask)/2
    #segmentedFrame = np.uint8(thresh)
    #segmentedFrame = otsu_semborda

           
	
    # return segmentedFrame ,gray
    return fgMask ,gray




def colour_to_thresh_complex(frame,threshold,kernel,kernel1):
    
    
    
   
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
    ret1, binary = cv2.threshold(gray,253,255,cv2.THRESH_BINARY)
    
    fgMask = backSub.apply(binary)
    
    #cv2.imwrite('subback.jpg', fgMask)
    
    Is=binary+ fgMask
    
    Is=(Is-Is.min())/(Is.max()-Is.min())*255
    Is = np.uint8(Is)
    
    
    
    #cv2.imwrite('soma.jpg', Is)
    segmentedFrame = Is
    
	
    return segmentedFrame ,gray




def detect_and_draw_contours(thresh, meas_last, meas_now, min_area, max_area, min_body_len, max_body_len, max_prop,min_prop):
    
    
    # Detect contours and draw them based on specified area thresholds
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #img = cv2.cvtColor(thresh.copy(), cv2.COLOR_GRAY2BGR)

    #final = frame.copy()

    i = 0
    meas_last = meas_now.copy()
    del meas_now[:]
    while i < len(contours):
        area = cv2.contourArea(contours[i])
        
        x,y,w,h = cv2.boundingRect(contours[i])
        body_len = int(np.ceil(np.sqrt(w**2 + h**2)))
        
        body_proportion= area/body_len
        
        if area < min_area or area > max_area or body_len < min_body_len or body_len > max_body_len or body_proportion < min_prop or body_proportion > max_prop:
            del contours[i]
        else:
            #cv2.drawContours(final, contours, i, (0,0,255), 1)
            M = cv2.moments(contours[i])
            if M['m00'] != 0:
            	cx = M['m10']/M['m00']
            	cy = M['m01']/M['m00']
            else:
            	cx = 0
            	cy = 0
            meas_now.append([cx,cy])
            i += 1
    return contours, meas_last, meas_now

def apply_k_means(contours, n_inds, meas_now):
    
    del meas_now[:]
    # Clustering contours to separate individuals
    myarray = np.vstack(contours)
    myarray = myarray.reshape(myarray.shape[0], myarray.shape[2])

    kmeans = KMeans(n_clusters=n_inds, random_state=0, n_init = 50).fit(myarray)
    l = len(kmeans.cluster_centers_)

    for i in range(l):
        x = int(tuple(kmeans.cluster_centers_[i])[0])
        y = int(tuple(kmeans.cluster_centers_[i])[1])
        meas_now.append([x,y])
    return contours, meas_now

def hungarian_algorithm(meas_last, meas_now):
    
    meas_last = np.array(meas_last)
    meas_now = np.array(meas_now)
    if meas_now.shape != meas_last.shape:
        if meas_now.shape[0] < meas_last.shape[0]:
            while meas_now.shape[0] != meas_last.shape[0]:
                meas_last = np.delete(meas_last, meas_last.shape[0]-1, 0)
        else:
            result = np.zeros(meas_now.shape)
            result[:meas_last.shape[0],:meas_last.shape[1]] = meas_last
            meas_last = result

    meas_last = list(meas_last)
    #print('meas_last: ',meas_last)
    meas_now = list(meas_now)
    #print('meas_now: ',meas_now) 
    cost = cdist(meas_last, meas_now)
    #print('cost: ',cost) 
    row_ind, col_ind = linear_sum_assignment(cost)
    #print('col_ind: ',col_ind)
    return row_ind, col_ind

def reorder_and_draw(final, colours, n_inds, col_ind, meas_now, df, mot, fr_no,shape_0,shape_1,tot_frames,t_id,pts,write_frame):
    
    
    equal = np.array_equal(col_ind, list(range(len(col_ind))))
    if equal == False:
        current_ids = col_ind.copy()
        reordered = [i[0] for i in sorted(enumerate(current_ids), key=lambda x:x[1])]
        meas_now = [x for (y,x) in sorted(zip(reordered,meas_now))]

    # Draw centroids
    if mot == False:
        for i in range(len(meas_now)):
            cv2.circle(final, tuple([int(x) for x in meas_now[i]]),  5  , (255,255,255), -1, cv2.LINE_AA)
    else:
        for i in range(n_inds):
            #cv2.circle(final, tuple([int(x) for x in meas_now[i]]), 5 , colours[i%n_inds], -1, cv2.LINE_AA)
            
                       
            cv2.putText(final, str(t_id[i%n_inds]), tuple([int(x) for x in meas_now[i]]), cv2.FONT_HERSHEY_SIMPLEX, 2,colours[i%n_inds], 2   , cv2.LINE_AA)
            pts.appendleft(tuple([int(x) for x in meas_now[i]]))
            
            for j in np.arange(0, len(pts),n_inds):
                thickness = int(np.sqrt(6 / float(j + 2)) *20)
                cv2.line(final, pts[j], pts[j], colours[i%n_inds], thickness)
    
    # add frame number
    if write_frame == True: 
        #font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(final, str(int( (fr_no/int(tot_frames))*100  ))+ " %", ( int(  (int(shape_0) *1)/100) , int((int(shape_1)*11.5)/100)),  cv2.FONT_HERSHEY_SIMPLEX,  (int(shape_1)* 0.3)/181, (0,0,0), 2, cv2.LINE_AA)
        cv2.putText(final, str(fr_no), ( int(  (int(shape_0) *1)/100) , int((int(shape_1)*18.5)/100)),  cv2.FONT_HERSHEY_SIMPLEX, (int(shape_1)* 0.3)/181, (0,0,0), 2, cv2.LINE_AA)
        cv2.putText(final, 'UFV - Ethoflow', (int((int(shape_0) *6)/100) , int((int(shape_1)*4.5)/100)),  cv2.FONT_HERSHEY_SIMPLEX, (int(shape_1)* 0.2)/181, (0,0,255), 2, cv2.LINE_AA)
        cv2.putText(final, 'Developer: Rodrigo C. Bernardes', (int((int(shape_0) *4.5)/100) , int((int(shape_1)*97)/100)),  cv2.FONT_HERSHEY_SIMPLEX, (int(shape_1)* 0.2)/181, (0,0,0), 2, cv2.LINE_AA)
	        
    return final, meas_now, df

def reject_outliers(data, m):
    
    d = np.abs(data - np.nanmedian(data))
    mdev = np.nanmedian(d)
    s = d/mdev if mdev else 0.
    return np.where(s < m)
