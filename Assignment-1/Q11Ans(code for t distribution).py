# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:19:18 2024

@author: rites
"""

#Q11) Suppose we want to estimate the average weight of an adult male in Mexico
#We draw a random sample of 2,000 men from a population of 3,000,000 men and weigh them. 
#We find that the average person in our sample weighs 200 pounds, and the standard deviation of the sample is 30 pounds. 
#Calculate 94%,98%,96% confidence interval?

#ANS:because we dont have sd for population we have to use t distribution
#xbar=200 ,sd=30 ,n=2000

from scipy.stats import norm
import numpy as np

#confidence interval-->94% 
ci1=norm.interval(0.94,loc=200,scale=30/2000**0.5)
print('94% confidence interval is',np.round(ci1,2))
#[198.74 201.26]


#confidence interval-->98% 
ci2=norm.interval(0.98,loc=200,scale=30/2000**0.5)
print(np.round(ci2,2))
#[198.44 201.56]

#confidence interval-->96% 
ci3=norm.interval(0.96,loc=200,scale=30/2000**0.5)
print(np.round(ci3,2))
#[198.62 201.38]









