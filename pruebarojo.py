#! /usr/bin/env python
#encoding: utf-8

import numpy as np
import cv2
import math
from angulo import *
from miejemplo2 import *

imagen = cv2.imread('prueba3.png')

ang,d = calculaAngulo(imagen)

cv2.imshow('Window',imagen)
cv2.waitKey(0)
