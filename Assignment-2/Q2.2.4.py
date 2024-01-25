# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 00:40:21 2024

@author: rites
"""


#mean=100, sd=20

import numpy as np
from scipy import stats
from scipy.stats import norm


np.round(stats.norm.interval(0.99, loc = 100, scale = 20),1)






