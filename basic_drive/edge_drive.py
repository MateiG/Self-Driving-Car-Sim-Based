import time
import cv2
import numpy as np
from screen_grab import record
from get_keys import key_check
from utility import sliding_window, get_curve
import cv2
import numpy as np
import time
import os
from PIL import ImageGrab
from matplotlib import pyplot as plt

def nothing():
    pass

# cv2.namedWindow('frame')
# cv2.createTrackbar('lower','frame',0,500,nothing)
# cv2.createTrackbar('upper','frame',0,500,nothing)
# l = cv2.getTrackbarPos('lower','frame')
# u = cv2.getTrackbarPos('upper','frame')


# lower = np.array([ 14,  35, 205])
# upper = np.array([34,  55, 285])
# mask = cv2.inRange(frame, lower, upper)

p1 = np.float32([[200,200], [450, 200], [0, 400], [640, 400]])
p2 = np.float32([[0, 0], [400, 0], [0, 640], [400, 640]])
matrix = cv2.getPerspectiveTransform(p1, p2)

def get_hist(img):
    hist = np.sum(img[img.shape[0]//2:,:], axis=0)
    return hist

while True:
    # frame =  cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0, 37, 640, 437))), cv2.COLOR_BGR2HSV)
    
    # warp = cv2.warpPerspective(frame, matrix, (400, 640))
    frame = cv2.VideoCapture('C:/AutonomousCar/basic_driving/challenge_video.mp4')

    blur = cv2.blur(frame, (5,5))
    edges = cv2.Canny(blur, 139, 267)
    out_img, curves, lanes, ploty = sliding_window(edges)
    curverad = get_curve(edges, curves[0],curves[1])
    cv2.imshow('frame', out_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break