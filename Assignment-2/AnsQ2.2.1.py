# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 23:23:13 2024

@author: rites
"""

from scipy.stats import norm
nd= norm(45,8) #mean=45min sd=8min  P[x>50]

#P(x>50)
p=1-nd.cdf(50)
p.round(4)































