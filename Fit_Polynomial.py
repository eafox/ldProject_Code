#!/usr/bin/python

"""Fits a polynomial curve to ld data generated by the pipeline. FILE NAME INPUT REQUIRED"""

___author__ = "Emma Fox (e.fox16@imperial.ac.uk)"
__version__ = "0.0.1"


##IMPORTS
import sys
from lmfit import minimize, Minimizer, Parameters, Parameter, report_fit, fit_report
import numpy as np
import matplotlib.pyplot as plt
import pylab

##DATA
ldFile = open(sys.argv[1])

BPDist,r2Pear,D,DPrime,r2GLS=np.loadtxt(ldFile, usecols=(2,3,4,5,6), unpack=True)

x=BPDist
data=r2Pear	

##FUNCTIONS
#Function
def POLY(params, x, data):
	"""Polynomial function"""
	a = params['a']
	b = params['b']
	c = params['c']
	model = a*x**2 + b*x + c
	return model - data

#Create parameter set
params = Parameters()
params.add('a', value=1)
params.add('b', value=1)
params.add('c', value=1)

#Fit with least squares
resultPOLY = minimize(POLY, params, args=(x,), kws={'data':data})

#Model line
final = data + resultPOLY.residual

#Reports
print(fit_report(resultPOLY))

#Plot Results
#~ pylab.plot(x, data, 'k+')
#~ pylab.plot(x, final, 'r')
#~ pylab.show()
