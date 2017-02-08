#!/usr/bin/python

"""Fits a gamma curve to ld data generated by the pipeline. FILE NAME INPUT REQUIRED"""

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
def GAM(paramsGAM, x, data):
	"""Polynomial function"""
	k = paramsGAM['k']
	t = paramsGAM['t']
	model = np.exp(-x * k) * x**t
	return model - data

#Create parameter set
paramsGAM = Parameters()
paramsGAM.add('k', value=1)
paramsGAM.add('t', value=1)

#Fit with least squares
resultGAM = minimize(GAM, paramsGAM, args=(x,), kws={'data':data})

#Model line
final = data + resultGAM.residual

#Reports
print(fit_report(resultGAM))

#Plot Results
#~ pylab.plot(x, data, 'k+')
#~ pylab.plot(x, final, 'r')
#~ pylab.show()