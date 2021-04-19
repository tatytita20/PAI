#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np

imagen = cv2.imread('wheel.png')
gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

#Para versiones OpenCV3:
img1,contornos1,hierarchy1 = cv2.findContours(th, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
img2,contornos2,hierarchy2 = cv2.findContours(th, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contornos1, -1, (0,0,255), 2)
print ('len(contornos1[2])=',len(contornos1[2]))
print ('len(contornos2[2])=',len(contornos2[2]))
cv2.imshow('imagen',imagen)
cv2.imshow('th',th)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




