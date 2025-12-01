# Prosessing diffrent images that has lanes in them
# Picture's origin from https://github.com/rslim087a/road-image 
# Running the code in terminal: python3 lanes.py

import cv2
import numpy as np

# Program to read the image, grey-scale and display it
image = cv2.imread('test_image.jpg')
lane_image = np.copy(image) # Working inside a copy of the image, not to affect the original one
gray = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY) # Grey-scaling the image

cv2.imshow('result', gray)
cv2.waitKey(0) # Time of the display, zero is infinite