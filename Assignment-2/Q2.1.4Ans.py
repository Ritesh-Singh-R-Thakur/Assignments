# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:36:56 2024

@author: rites
"""

#p=1/200, q=1-1/200=199/200, n=5, r=1

1/200
1/5

from scipy.stats import binom

bi=binom(n=5,p=1/200)#n,p

#p(r=1)

z=bi.pmf(1) 
z
z.round(4)#0.0245











