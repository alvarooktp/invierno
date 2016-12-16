#! /usr/bin/env python
#encoding: utf-8

import sys
import numpy as np
import cv2
from remoteFrame import *
from miejemplo2 import *
import espino
import time

port = 8888
address = '192.168.1.7'
ip = '192.168.1.13'
Mask = None

argc = len (sys.argv)
if argc > 1:
    address = sys.argv[1]
    if argc > 2:
        port = int(sys.argv[2])
        if argc > 3:
            Mask = cv2.imread(sys.argv[3])
Mask = cv2.imread('Maze1.png')
#rF=remoteFrame(address, port, Mask)

cv2.namedWindow('MyWindow')
imagen = cv2.imread('miMaze1.png')
#imagen = cv2.imread('prueba2.png')
while cv2.waitKey(1) == -1:
    #imagen = rF.getFrame()
    ang,d,bandera,suma = calculaAngulo(imagen)
    print suma
    cv2.imshow('MyWindow', imagen)
    cv2.imwrite('error.png',imagen)
