import numpy as np
import cv2
b = np.zeros([800,800],dtype = 'uint8')

i=0
flag=0
while i<=800:
    j=0
    if flag == 0:
        while j<=800:
            b[j:j+100,i:i+100] = 255
            flag=1
            j=j+200
    else:
        while j<=800:
            b[j+100:j+200,i:i+100] = 255
            flag=0
            j=j+200
    i=i+100

cv2.imshow('Checkerboard 8 * 8 ',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
