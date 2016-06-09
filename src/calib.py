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
FRAME_INTERVAL = 3
MAX_FRAMES = 10

def nothing():
    pass

def createStereoPair(id1, id2):
    try:
        return (cv2.VideoCapture(id1), cv2.VideoCapture(id2))
    except:
        print traceback.format_exc()
        return (None, None)

def captureFromStereo(cam):
    _, frame1 = cam[0].read()
    _, frame2 = cam[1].read()
    return [frame1, frame2]

def combineStereoFrames(frames, swap=False):
    return np.concatenate((frames[1], frames[0]), axis=1) if swap else np.concatenate((frames[0], frames[1]), axis=1)

def releaseStereoPair(cam):
    cam[0].release()
    cam[1].release()

def createChessboard(gridSize, squareSize):
    iObjPoints = np.zeros((gridSize[0]*gridSize[1], 3), np.float32)
    iObjPoints[:, :2] = np.mgrid[0:gridSize[0], 0:gridSize[1]].T.reshape(-1, 2) * squareSize
    return iObjPoints

def findChessboardCorners(frames, nChessFrames, gridSize, iObjPoints, objPoints, imgPoints, append=False, draw=True):
    gray1, gray2 = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY), cv2.cvtColor(frames[1], cv2.COLOR_BGR2GRAY)
    ret1, corners1 = cv2.findChessboardCorners(gray1, gridSize)
    ret2, corners2 = cv2.findChessboardCorners(gray2, gridSize)
#    print ret1, ret2
    if ret1 and ret2 is True:
        cv2.cornerSubPix(gray1, corners1, (11,11), (-1,-1), CRITERIA)
        cv2.cornerSubPix(gray2, corners2, (11,11), (-1,-1), CRITERIA)
        if append is True:
            print "Frame {} appended".format(nChessFrames)
            objPoints.append(iObjPoints)
            imgPoints[0].append(corners1)
            imgPoints[1].append(corners2)
            nChessFrames += 1
        if draw is True:
            cv2.drawChessboardCorners(frames[0], gridSize, corners1, ret1)
            cv2.drawChessboardCorners(frames[1], gridSize, corners2, ret2)

    return frames, nChessFrames, objPoints, imgPoints
