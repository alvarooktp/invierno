import numpy as np
import cv2

imagen = cv2.imread('prueba.png')
gray_image = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_image',gray_image)
imR = imagen[:,:,0]
imG = imagen[:,:,1]
imB = imagen[:,:,2]
final = imR - imG - imB
dim1, dim2 = final.shape
for i in range (0,dim1):
    for j in range (0,dim2):
        if final[i,j]<200:
            final[i,j]=0

parte1 = final[:dim1/2,:dim2/2]
parte3 = final[:dim1/2,dim2/2:]
parte2 = final[dim1/2:,:dim2/2]
parte4 = final[dim1/2:,dim2/2:]
cv2.imshow('Final',final)
cv2.imshow('parte1',parte1)
cv2.imshow('parte2',parte2)
cv2.imshow('parte3',parte3)
cv2.imshow('parte4',parte4)
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()
