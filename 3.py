"""
@File    : 3.py
@Date    : 2024-07-07
@Author  : ThreeThreeLiu
@Software : learn_opencv
draw lines on an image
"""
import cv2
import numpy as np

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)