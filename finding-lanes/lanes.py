# Prosessing diffrent images that has lanes in them
# Picture's origin from https://github.com/rslim087a/road-image 
# Running the code in terminal: python3 lanes.py

import cv2
import numpy as np
import matplotlib.pyplot as plt 

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Grey-scaling the image
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # Optional method - Blurring the image to reduce noise
    canny = cv2.Canny(blur, 50, 150) # Canny method to detect edges in the image with 1:3 ratio
    return canny

# Detecting the correct lane area of the image 
def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(200, height), (1100, height), (550, 250)]
    ])
    mask = np.zeros_like(image) # Creating a mask with zeros
    cv2.fillPoly(mask, polygons, 255) # Filling the mask with white color in the defined polygon area
    masked_image = cv2.bitwise_and(image, mask) # Bitwise AND between the image and the mask: it puts a zero unless both pairs are ones
    return masked_image

# Program to read the image, grey-scale and display it
image = cv2.imread('test_image.jpg')
lane_image = np.copy(image) # Working inside a copy of the image, not to affect the original one
canny = canny(lane_image)
cropped_image = region_of_interest(canny)
plt.imshow(cropped_image)
plt.show()
#cv2.waitKey(0) # Time of the display, zero is infinite