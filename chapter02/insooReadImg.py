import numpy as np
import cv2
import matplotlib.pyplot as plt
#%matplotlib inline  # if you are running this code in Jupyter notebook

# reads image 'opencv-logo.png' as grayscale
img = cv2.imread('MyPic.png', 0) 
plt.imshow(img, cmap='winter')
