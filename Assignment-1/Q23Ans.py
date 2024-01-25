# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:48:39 2024

@author: rites
"""

#Calculate the t scores of 95% confidence interval, 96% confidence interval, 99% confidence interval for sample size of 25

from scipy.stats import norm
import numpy as np
from scipy import stats


#confidence interval-->95%
ci7=stats.t.ppf(0.95,24) #degree of freedom=n-1=25-1=24
print(np.round(ci7,2))
#1.71 


#confidence interval-->96%
ci8=stats.t.ppf(0.96,24)
print(np.round(ci8,2))
#1.83


#confidence interval-->60%
ci9=stats.t.ppf(0.60,24)
print(np.round(ci9,2))
#0.26
























