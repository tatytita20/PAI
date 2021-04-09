#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Import libraries
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# In[12]:


# Load input image in grayscale
img = cv.imread('coffee_grains.jpg')
imageGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, imgThresh = cv.threshold(imageGray,127,255,cv.THRESH_BINARY)
kernel = np.ones((3,3), np.uint8) 

# Functions
imgOpenedandClosed = cv.morphologyEx(cv.morphologyEx(imgThresh, cv.MORPH_OPEN, kernel, iterations=1),cv.MORPH_CLOSE, kernel, iterations=7)
imgDilate = cv.dilate(imgOpenedandClosed, kernel, iterations=6)
imgClosed = cv.morphologyEx(imgDilate,cv.MORPH_CLOSE, kernel, iterations=2)

# Output image resizing
plt.figure(figsize=(15,15))

# Alignment, ordering and display of the output images
plt.subplot(4,4,1)
plt.title("Original image:")
plt.imshow(img, cmap = 'gray');

plt.subplot(4,4,2)
plt.title("Image opening and closing:")
plt.imshow(imgOpenedandClosed, cmap = 'gray')

plt.subplot(4,4,3)
plt.title("Image dilation:")
plt.imshow(imgDilate, cmap = 'gray')

plt.subplot(4,4,4)
plt.title("Close up image:")
plt.imshow(imgClosed, cmap = 'gray')
plt.show()


# In[ ]:




