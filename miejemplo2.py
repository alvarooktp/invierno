
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import math
from angulo import *
import time
def sumarMatriz (matriz):
	suma = 0
	dim1, dim2 = matriz.shape
	for i in range (0,dim1):
	    for j in range (0,dim2):
			suma = suma + matriz[i][j]
			if suma>=1:
				return 1
	return suma
def calculaAngulo(imagen):

	bandera = 1
	yc = 0
	xc = 0
	suma = 0
	mensaje = 'No encontre '
	final2 = imagen.copy()
	imSz = imagen.shape
	hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

	rojo_bajos = np.array([168,100,100])
	rojo_altos = np.array([188,255,255])

	amarillo_bajos = np.array([20,100,100])
	amarillo_altos = np.array([40,255,255])

	azul_bajos = np.array([110,100,100])
	azul_altos = np.array([130,255,255])

	magenta_bajos = np.array([140,100,100])
	magenta_altos = np.array([160,255,255])

	rojomask = cv2.inRange(hsv, rojo_bajos, rojo_altos)
	amarillomask = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
	azulmask = cv2.inRange(hsv, azul_bajos, azul_altos)
	magentamask = cv2.inRange(hsv, magenta_bajos, magenta_altos)

	ret,thresh = cv2.threshold(rojomask,127,255,0)
	contours,hierarchy = cv2.findContours(thresh, 1, 2)

	if len(contours) != 0:
		cnt = contours[0]
		(xr,yr),radius = cv2.minEnclosingCircle(cnt)
		cv2.rectangle(imagen, (int(xr), int(yr)), (int(xr)+2, int(yr)+2),(0,0,255), 2)
	else:
		bandera = 0
		mensaje = mensaje + 'rojo '

	ret,thresh = cv2.threshold(amarillomask,127,255,0)
	contours,hierarchy = cv2.findContours(thresh, 1, 2)

	if len(contours) != 0:
		cnt = contours[0]
		(xa,ya),radius = cv2.minEnclosingCircle(cnt)
		cv2.rectangle(imagen, (int(xa), int(ya)), (int(xa)+2, int(ya)+2),(0,0,255), 2)
	else:
		bandera = 0
		mensaje = mensaje + 'amarillo '

	if bandera == 1:
		xc = (xr+xa)/2
		yc = (yr+ya)/2
		cv2.rectangle(imagen, (int(xc), int(yc)), (int(xc)+2, int(yc)+2),(0,0,255), 2)

	ret,thresh = cv2.threshold(magentamask,127,255,0)
	contours,hierarchy = cv2.findContours(thresh, 1, 2)

	if len(contours) != 0:
		cnt = contours[0]
		(xm,ym),radius = cv2.minEnclosingCircle(cnt)
		cv2.rectangle(imagen, (int(xm), int(ym)), (int(xm)+2, int(ym)+2),(0,0,255), 2)
		dim1, dim2,dim3 = imagen.shape
		#fondo = np.zeros((dim1,dim2))
		fondo = 0*imagen
		cv2.line(fondo,(int(xm),int(ym)),(int(xc),int(yc)),(0,255,0),2)
		cv2.imshow('Linea',fondo)

		suma = sumarMatriz(np.multiply(fondo[:,:,1],azulmask))
		#print suma
	else:
		bandera = 0
		mensaje = mensaje + 'magenta '
	if bandera == 1:
		yr=imSz[0]-yr
		ya=imSz[0]-ya
		yc=imSz[0]-yc
		ym=imSz[0]-ym

		vectorcarro=[xr-xa,yr-ya]
		vectordestino=[xm-xc,ym-yc]

		angulocarro = angulo(vectorcarro[1],vectorcarro[0])
		angulodestino = angulo(vectordestino[1],vectordestino[0])
		angulodesv = angulocarro - angulodestino
		if angulodesv > 180:
				angulodesv = angulodesv - 360
		if angulodesv < -180:
				angulodesv = 360 + angulodesv

		d = np.sqrt((xm-xc)**2 + (ym-yc)**2)

		return angulodesv,d,bandera,suma
	else:
		print mensaje
		return 0,0,bandera,-1
