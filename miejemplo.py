import numpy as np
import cv2

imagen = cv2.imread('prueba.png')
gray_image = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_image',gray_image)
print imagen.shape
print gray_image.shape
imR = imagen[:,:,0]
imG = imagen[:,:,1]
imB = imagen[:,:,2]
final = imR - imG - imB
final2 = final.copy
for i in range (0,480):
    for j in range (0,640):
        if final[i,j]<200:
            final[i,j]=0
#final = final >=255
cv2.imshow('Final',final)
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()
