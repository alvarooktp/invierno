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

argc = len (sys.argv)
if argc > 1:
	address = sys.argv[1]
	if argc > 2:
		port = int(sys.argv[2])

rF=remoteFrame(address, port)

cv2.namedWindow('MyWindow')
flag = 0
while cv2.waitKey(1) == -1 and flag == 0: 
#	imagen = cv2.imread('prueba3.png')
	imagen = rF.getFrame()
	ang,d = calculaAngulo(imagen)
	print ang
	tiempo = ang*(15)
	if d < 50:
		flag = 1
	else:
		if ang < 20 and ang > -20:
			espino.avanzar(ip,400,500)
		else:
			if ang < 0:
				tiempo = -tiempo
				espino.izquierda(ip,150,tiempo)
			else:
				espino.derecha(ip,150,tiempo)
	cv2.imshow('MyWindow', imagen)
	
espino.avanzar(ip,400,500)
