#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# In[12]:


img = cv.imread('hitchcock.png', 0)
kernel = np.ones((5,5), np.uint8)  

imgEroded = cv.erode(img, kernel)
imgDilate = cv.dilate(img, kernel)
imgOpened = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
imgClosed = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

Contour1 = img - imgEroded
Contour2 = imgDilate - img

plt.figure(figsize=(10,10))

plt.subplot(5,5,1)
plt.title("Original image:")
plt.imshow(img, cmap = 'gray')

plt.subplot(5,5,2)
plt.title("Eroded image:")
plt.imshow(imgEroded, cmap = 'gray')

plt.subplot(5,5,3)
plt.title("Dilated image:")
plt.imshow(imgDilate, cmap = 'gray')

plt.subplot(5,5,4)
plt.title("Image outline1:")
plt.imshow(Contour1, cmap = 'gray')

plt.subplot(5,5,5)
plt.title("Image outline2:")
plt.imshow(Contour2, cmap = 'gray')



# In[ ]:





# In[ ]:




