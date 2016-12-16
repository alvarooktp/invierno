#! /usr/bin/env python
#encoding: utf-8

import sys
import numpy as np
import cv2
from remoteFrame import *
from miejemplo3 import *
import espino
import time

port = 8888
address = '192.168.1.6'
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
rF=remoteFrame(address, port, Mask)

cv2.namedWindow('MyWindow')

imagen=rF.getFrame()
ang, d, bandera, suma = calculaAngulo(imagen)
if suma == 0:
	llegaRecto()
else:
	llegaPaso()

def llegaRecto():
	flag = 0
	while cv2.waitKey(1) == -1 and flag == 0:
		imagen = rF.getFrame()
		ang,d,bandera,suma = calculaAngulo(imagen)
		tiempo = ang*(13)
		if bandera == 1:
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
				print 'esperando'
				time.sleep(3)
				cv2.imshow('MyWindow', imagen)
