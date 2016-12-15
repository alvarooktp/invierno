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
address = '192.168.1.15'
ip = '192.168.1.13'

argc = len (sys.argv)
if argc > 1:
	address = sys.argv[1]
	if argc > 2:
		port = int(sys.argv[2])

rF=remoteFrame(address, port)

cv2.namedWindow('MyWindow')

while cv2.waitKey(1) == -1: 

	imagen = rF.getFrame()	
	ang,d = calculaAngulo(imagen)
	cv2.imshow('MyWindow', imagen)
