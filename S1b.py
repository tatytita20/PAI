#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import random


# In[2]:


def grassfire_propagation(image, mask):
   
    # Binary threshold
    _, imageThresh = cv.threshold(image, 127, 255, cv.THRESH_BINARY)   
    
    # Scale of colors
    imageOut = cv.cvtColor(imageThresh, cv.COLOR_GRAY2BGR)
    
    # Apply the grassfire transform to a binary mask array.
    h, w = imageThresh.shape

    # Use uint8 to avoid overflow
    grassfire = np.zeros((h+2,w+2), np.uint8)

    # 1st pass
    for x in range(h):
        for y in range(w):
            if imageThresh[x, y] == 255: # Pixel in contour
               
                # Random color generator
                Blue = random.randint(0,255)
                Green = random.randint(0,255)
                Red = random.randint(0,255)
               
                
                # Color assignment
                cv.floodFill(imageOut, grassfire, (x,y), (Blue, Green, Red), flags = mask)
    return imageOut

    # 2nd pass
    TestImg = ['Lenna.png', 'particles.png'] 
    for NameImg in TestImg:
        print(NameImg.title ())
        picture = cv.imread(+NameImg, cv.IMREAD_GRAYSCALE)
        picture2 = grassfire_propagation(picture, 2)
        picture4 = grassfire_propagation(picture, 4)
        plt.figure(figsize=(10,10));
        plt.subplot(1,3,1);
        plt.title('Original image: ' + NameImg);
        plt.imshow(picture, cmap = 'gray');
        plt.subplot(1,3,2);
        plt.title("Grass fire image:");
        plt.imshow(picture2, cmap = 'gray');
        plt.subplot(1,3,3);
        plt.title("Grass fire image:");
        plt.imshow(picture4, cmap = 'gray');
        plt.show()


# In[ ]:




