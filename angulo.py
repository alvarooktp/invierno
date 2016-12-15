#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def angulo(y,x):

	if y == 0:
		if x > 0:
			tetha = 0
		else:
			tetha = 180
	else:
		if y > 0:
			if x == 0:
				tetha = 90
			else:
				if x > 0:
					tetha = math.degrees(math.atan(y/x))
				else:
					tetha = math.degrees(math.atan(y/x)) + 180
		else:
			if x == 0:
				tetha = 270
			else:
				if x > 0:
					tetha = math.degrees(math.atan(y/x))+360
				else:
					tetha = math.degrees(math.atan(y/x))+180

	return tetha
