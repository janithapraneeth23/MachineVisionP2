import cv2
import numpy as np

img = cv2.imread('E:/Academics/OpenCV/MachineVissionP2/hotel.seq0.png',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)  


dst  = cv2.cornerHarris(img,2,3,0.04)

dst = cv2.dilate(dst,None)

img[dst>0.01 * dst.max()] = [0]

cv2.imshow('image',img)  

cv2.waitKey(0)
cv2.destroyAllWindows()