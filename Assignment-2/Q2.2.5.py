# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 00:52:58 2024

@author: rites
"""



import numpy as np
from scipy import stats
from scipy.stats import norm

#p=95%,mean=5+7=12*45=RS 540, sd=squrt(9+16)=5*45=RS 225

#Q5A p=95%

 
Rs1=(stats.norm.interval(0.95, loc =540 , scale =225))
Rs1#(99.00810347848784, 980.9918965215122)

#p=99.7%
Rs2=(stats.norm.interval(0.997, loc =540 , scale =225))
Rs2#(-127.74103320190125, 1207.7410332018985)


#Q5C

# Probability of Division 1 making a loss P(X<0)

Rs3=stats.norm.cdf(0,5,3)
Rs3#0.0477903522728147

# Probability of Division 2 making a loss P(X<0)

Rs4=stats.norm.cdf(0,7,4)
Rs4#0.040059156863817086

#Division 1 has 4.77% probability of making no profit which is higher than division 2=4% probability

