import cv2 
import numpy as np 
#import image 
image = cv2.imread('led1.jpg')

#grayscale 
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
#cv2.imshow('gray', gray) 

#binary 
ret,thresh = cv2.threshold(gray,235,255,cv2.THRESH_BINARY_INV) 
cv2.imshow('second', thresh) 


#dilation 
'''
kernel = np.ones((1,1), np.uint8) 
img_dilation = cv2.dilate(thresh, kernel, iterations=1) 
cv2.imshow('dilated', img_dilation) '''

__,thresh1 = cv2.threshold(gray,230,255,cv2.THRESH_BINARY)
cv2.imshow('binary',thresh1)
