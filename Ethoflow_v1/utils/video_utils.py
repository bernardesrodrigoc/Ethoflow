"""
See readme for information about this file.
Ethoflow: computer vision and artificial intelligence-based software for automatic behavior analysis
v 1.0

DOI: 10.1101/2020.07.23.218255
LicenseCC BY-NC-ND 4.0

@developer: Rodrigo Cupertino Bernardes
https://www.researchgate.net/profile/Rodrigo_Cupertino_Bernardes
"""

from __future__ import absolute_import, division, print_function
import os
import sys
import numpy as np
import multiprocessing
import cv2
from joblib import Parallel, delayed


def sum_frames_for_bkg_per_episode_in_single_file_video(starting_frame,
                                                        ending_frame,
                                                        video_path, bkg):
   
    cap = cv2.VideoCapture(video_path)
    logger.debug('Adding from starting frame %i to background' %starting_frame)
    number_of_frames_for_bkg_in_episode = 0
    frameInds = range(starting_frame,ending_frame, BACKGROUND_SUBTRACTION_PERIOD)
    for ind in frameInds:
        logger.debug('Frame %i' %ind)
        cap.set(1,ind)
        ret, frameBkg = cap.read()
        if SIGMA_GAUSSIAN_BLURRING is not None:
            frameBkg = cv2.GaussianBlur(frameBkg, (0, 0), SIGMA_GAUSSIAN_BLURRING)
        if ret:
            gray = cv2.cvtColor(frameBkg, cv2.COLOR_BGR2GRAY)
            gray = np.true_divide(gray,np.mean(gray))
            bkg = bkg + gray
            number_of_frames_for_bkg_in_episode += 1

    cap.release()
    return bkg, number_of_frames_for_bkg_in_episode

def sum_frames_for_bkg_per_episode_in_multiple_files_video(video_path, bkg):
    
    logger.debug('Adding video %s to background' % video_path)
    cap = cv2.VideoCapture(video_path)
    counter = 0
    numFrame = int(cap.get(7))
    number_of_frames_for_bkg_in_episode = 0
    frameInds = range(0,numFrame, BACKGROUND_SUBTRACTION_PERIOD)
    for ind in frameInds:
        cap.set(1,ind)
        ret, frameBkg = cap.read()
        if SIGMA_GAUSSIAN_BLURRING is not None:
            frameBkg = cv2.GaussianBlur(frameBkg, (0, 0), SIGMA_GAUSSIAN_BLURRING)
        if ret:
            gray = cv2.cvtColor(frameBkg, cv2.COLOR_BGR2GRAY)
            gray = np.true_divide(gray,np.mean(gray))
            bkg = bkg + gray
            number_of_frames_for_bkg_in_episode += 1

    return bkg, number_of_frames_for_bkg_in_episode

def cumpute_background(video):
    
    # This holds even if we have not selected a ROI because then the ROI is
    # initialized as the full frame
    bkg = np.zeros((video.original_height, video.original_width))
    num_cores = multiprocessing.cpu_count()
    if NUMBER_OF_CORES_FOR_BACKGROUND_SUBTRACTION is not None:
        try:
            logger.info('NUMBER_OF_CORES_FOR_BACKGROUND_SUBTRACTION set to a value different than the default')
            assert NUMBER_OF_CORES_FOR_BACKGROUND_SUBTRACTION <= multiprocessing.cpu_count()
            num_cores = NUMBER_OF_CORES_FOR_BACKGROUND_SUBTRACTION
        except:
            logger.info('NUMBER_OF_CORES_FOR_BACKGROUND_SUBTRACTION > multiprocessing.cpu_count(). Setting NUMBER_OF_CORES_FOR_BACKGROUND_SUBTRACTION set to 1')
            num_cores = 1

    set_mkl_to_single_thread()
    if video.paths_to_video_segments is None: # one single file
        logger.debug('one single video, computing bkg in parallel from single video')
        output = Parallel(n_jobs=num_cores)(delayed(
                    sum_frames_for_bkg_per_episode_in_single_file_video)(
                    starting_frame, ending_frame, video.video_path, bkg)
                    for (starting_frame, ending_frame) in video.episodes_start_end)
        logger.debug('Finished parallel loop for bkg subtraction')
    else: # multiple video files
        logger.debug('multiple videos, computing bkg in parallel from every episode')
        output = Parallel(n_jobs=num_cores)(delayed(
                    sum_frames_for_bkg_per_episode_in_multiple_files_video)(
                    videoPath,bkg) for videoPath in video.paths_to_video_segments)
        logger.debug('Finished parallel loop for bkg subtraction')
    set_mkl_to_multi_thread()

    partialBkg = [bkg for (bkg,_) in output]
    totNumFrame = np.sum([numFrame for (_,numFrame) in output])
    bkg = np.sum(np.asarray(partialBkg),axis=0)
    bkg = np.true_divide(bkg, totNumFrame)
    return bkg.astype('float32')

def check_background_substraction(video, old_video, use_previous_background):
    
    bkg = None
    if video.subtract_bkg:
        if use_previous_background and old_video.bkg is not None:
            bkg = old_video.bkg
        else:
            bkg = cumpute_background(video)

    return bkg

def segment_frame(frame, min_threshold, max_threshold, bkg, ROI, useBkg):
    
    if useBkg:
        frame = cv2.absdiff(bkg,frame) #only step where frame normalization is important, because the background is normalised
        # frame = bkg - frame
        frame = 255 - frame * (255.0/frame.max())
        frame_segmented = cv2.inRange(frame, min_threshold, max_threshold) #output: 255 in range, else 0
    elif not useBkg:
        frame_segmented = cv2.inRange(frame * (255.0/frame.max()), min_threshold, max_threshold) #output: 255 in range, else 0
    frame_segmented_and_masked = cv2.bitwise_and(frame_segmented,frame_segmented, mask=ROI) #Applying the mask
    return frame_segmented_and_masked



def filter_contours_by_area(contours, min_area, max_area, min_body_len, max_body_len,max_prop,min_prop):
    

    good_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        x,y,w,h = cv2.boundingRect(contour)
        body_len = int(np.ceil(np.sqrt(w**2 + h**2)))
        body_prop = area/body_len
        if area > min_area and area < max_area and body_len > min_body_len and body_len < max_body_len and body_prop > min_prop and body_prop < max_prop:
            good_contours.append(contour)
    return good_contours

def cnt2BoundingBox(cnt,bounding_box):
    
    return cnt - np.asarray([bounding_box[0][0],bounding_box[0][1]])

def get_bounding_box(cnt, width, height, crossing_detector = False):
    
    x,y,w,h = cv2.boundingRect(cnt)
    original_diagonal = int(np.ceil(np.sqrt(w**2 + h**2)))
    n = 45 if not crossing_detector else 55
    if x - n > 0: # We only expand the
        x = x - n
    else:
        x = 0
    if y - n > 0:
        y = y - n
    else:
        y = 0
    if x + w + 2*n < width:
        w = w + 2*n
    else:
        w = width - x
    if y + h + 2*n < height:
        h = h + 2*n
    else:
        h = height - y
    return ((x, y),(x + w, y + h)), original_diagonal

def getCentroid(cnt):
    
    M = cv2.moments(cnt)
    x = M['m10']/M['m00']
    y = M['m01']/M['m00']
    return (x,y)

def get_pixels(cnt, width, height):
    
    cimg = np.zeros((height, width))
    cv2.drawContours(cimg, [cnt], -1, color=255, thickness = -1)
    pts = np.where(cimg == 255)
    return np.asarray(list(zip(pts[0],pts[1])))

def get_bounding_box_image(frame, cnt):
    
    height = frame.shape[0]
    width = frame.shape[1]
    bounding_box, estimated_body_length = get_bounding_box(cnt, width, height) # the estimated body length is the diagonal of the original bounding_box
    bounding_box_image = frame[bounding_box[0][1]:bounding_box[1][1],
                            bounding_box[0][0]:bounding_box[1][0]]
    contour_in_bounding_box = cnt2BoundingBox(cnt,bounding_box)
    pixels_in_bounding_box = get_pixels(contour_in_bounding_box,
                            np.abs(bounding_box[0][0] - bounding_box[1][0]),
                            np.abs(bounding_box[0][1] - bounding_box[1][1]))
    pixels_in_full_frame = pixels_in_bounding_box + \
                            np.asarray([bounding_box[0][1], bounding_box[0][0]])
    pixels_in_full_frame_ravelled = np.ravel_multi_index(
                                    [pixels_in_full_frame[:,0], pixels_in_full_frame[:,1]],
                                    (height,width))
    return bounding_box, bounding_box_image, pixels_in_full_frame_ravelled, estimated_body_length

def get_blobs_information_per_frame(frame, contours):
    
    bounding_boxes = []
    bounding_box_images = []
    centroids = []
    areas = []
    pixels = []
    estimated_body_lengths = []
    countours_got = []
    body_prop= []

    for i, cnt in enumerate(contours):
        bounding_box, \
        bounding_box_image, \
        pixels_in_full_frame_ravelled, \
        estimated_body_length = get_bounding_box_image(frame, cnt)
        #bounding boxes
        bounding_boxes.append(bounding_box)
        # bounding_box_images
        bounding_box_images.append(bounding_box_image)
        # centroids
        centroids.append(getCentroid(cnt))
        areas.append(cv2.contourArea(cnt))
        # pixels lists
        pixels.append(pixels_in_full_frame_ravelled)
        # estimated body lengths list
        estimated_body_lengths.append(estimated_body_length)
        # get the countours
        countours_got.append(cnt)
        
        body_prop.append(float(cv2.contourArea(cnt))/float(estimated_body_length))
        #print(cv2.contourArea(cnt))
        #print(estimated_body_length)
    return bounding_boxes, bounding_box_images, centroids, areas, pixels, estimated_body_lengths, countours_got, body_prop

def blob_extractor(segmented_frame, frame, min_area, max_area, min_body_len, max_body_len,max_prop,min_prop):
    
   
    contours, hierarchy = cv2.findContours(segmented_frame,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours by size
    good_contours_in_full_frame = filter_contours_by_area(contours,min_area, max_area, min_body_len, max_body_len,max_prop,min_prop)
    # get contours properties
    bounding_boxes, bounding_box_images, \
    centroids, areas, pixels, \
    estimated_body_lengths, countours_got, body_prop = get_blobs_information_per_frame(frame, good_contours_in_full_frame)

    return bounding_boxes, bounding_box_images, centroids, areas, pixels, good_contours_in_full_frame, estimated_body_lengths, countours_got, body_prop
