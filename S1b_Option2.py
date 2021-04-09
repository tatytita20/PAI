#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import random


# In[ ]:


mask = cv.imread('particles.png', 0)

def grassfire_transform(mask):
    #   Apply the grassfire transform to a binary mask array.
    h, w = mask.shape
    # Use uint32 to avoid overflow
    grassfire = np.zeros_like(mask, dtype=np.uint32)

    # 1st pass
    # Left to right, top to bottom
    for x in range(w):
        for y in range(h):
            if imgGray[y, x] != 0: # Pixel in contour
                north = 0 if y == 0 else grassfire[y - 1, x]
                west = 0 if x == 0 else grassfire[y, x - 1]
                if x == 3 and y == 3:
                    print(north, west)
                grassfire[y, x] = 1 + min(west, north)

    # 2nd pass
    # Right to left, bottom to top
    for x in range(w - 1, -1, -1):
        for y in range(h - 1, -1, -1):
            if gf[y, x] != 0: # Pixel in contour
                south = 0 if y == (h - 1) else grassfire[y + 1, x]
                east = 0 if x == (w - 1) else grassfire[y, x + 1]
                grassfire[y, x] = min(grassfire[y, x],
                    1 + min(south, east))
    return grassfire

  
    # Output image resizing
    plt.figure(figsize=(15,15))
    
    # Alignment, ordering and display of the output images
    plt.subplot(3,3,1)
    plt.title("Original image:")
    plt.imshow(mask, cmap = 'gray')
    
    plt.subplot(3,3,2)
    plt.title("Opened image:")
    plt.imshow(imgGray, cmap = 'gray')
    
    plt.subplot(3,3,3)
    plt.title("Contour image:")
    plt.imshow(gf, cmap = 'gray')
    plt.show()
   


# In[ ]:




