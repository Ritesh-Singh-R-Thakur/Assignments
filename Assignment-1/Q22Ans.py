# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:29:41 2024

@author: rites
"""


#Calculate the Z scores of 90% confidence interval,94% confidence interval, 60% confidence interval

from scipy import stats
from scipy.stats import norm
import numpy as np

#confidence interval-->90%
ci4=stats.norm.ppf(0.90)
print(np.round(ci4,2))
#1.28

#confidence interval-->94%
ci5=stats.norm.ppf(0.94)
print(np.round(ci5,2))
#1.55

#confidence interval-->60%
ci6=stats.norm.ppf(0.60)
print(np.round(ci6,2))
#0.25

from scipy import stats



