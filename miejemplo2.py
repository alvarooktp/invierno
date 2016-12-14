#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

imagen = cv2.imread('prueba.png')
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

verde_bajos = np.array([49,50,50])
verde_altos = np.array([80, 255, 255])

mask = cv2.inRange(hsv, verde_bajos, verde_altos)

cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
