#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import random


# In[29]:


def grassfire_propagation(img, mask):
    
    # Binary threshold
    _, imgThresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)   
    
    # Scale of colors
    imgOut = cv.cvtColor(imgThresh, cv.COLOR_GRAY2BGR)
    
    # Apply the grassfire transform to a binary mask array.
    h, w = imgThresh.shape

    # Use uint8 to avoid overflow
    grassfire = np.zeros((h,w), np.uint8)

    # 1st pass
    for x in range(h):
        for y in range(w):
            if (imgThresh [x,y] == 255): # Pixel in contour
               
                # Random color generator
                Blue = random.randint(0,255)
                Green = random.randint(0,255)
                Red = random.randint(0,255)
               
                
                # Color assignment
                cv.floodFill(imgOut, grassfire, (x,y), (Blue, Green, Red), flags = mask)
    return imgOut

    # 2nd pass
    picture = cv.imread('Lenna.png', 0)
    picture1 = picture.grassfire_propagation(picture, 1)
    picture2 = picture.grassfire_propagation(picture, 2)
   
    # Output image resizing
    plt.figure(figsize=(15,15))
    
    # Alignment, ordering and display of the output images
    plt.subplot(3,3,1)
    plt.title("Original image:")
    plt.imshow(picture, cmap = 'gray')
    
    plt.subplot(3,3,2)
    plt.title("Grass fire image1:")
    plt.imshow(picture2, cmap = 'gray')
    
    plt.subplot(3,3,3)
    plt.title("Grass fire image2:")
    plt.imshow(picture4, cmap = 'gray')
    plt.show()
   


# In[ ]:




