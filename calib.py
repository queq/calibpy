#! /usr/bin/env python

"""Camera calibration functions and utilities."""

import glob
import os
import re
import sys
import traceback
import time as t

import cv2
import cv2.cv as cv
import numpy as np

CRITERIA = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def nothing():
    pass

def createStereoPair(id1, id2):
    try:
        return cv2.VideoCapture(id1), cv2.VideoCapture(id2)
    except:
        print traceback.format_exc()
        return None, None

def captureFromStereo(cam1, cam2):
    _, frame1 = cam1.read()
    _, frame2 = cam2.read()
    return frame1, frame2

def cameraSideSwap(frame1, frame2, swap):
    return (swap and np.concatenate((frame2, frame1), axis=1) or np.concatenate((frame1, frame2), axis=1))

def releaseStereoPair(cam1, cam2):
    cam1.release()
    cam2.release()

def createChessboard(gridSize, squareSize):
    objectPoints = np.zeros((gridSize[0]*gridSize[1],3), np.float32)
    objectPoints[:,:2] = np.mgrid[0:gridSize[0],0:gridSize[1]].T.reshape(-1,2) * squareSize
    return objectPoints

def
