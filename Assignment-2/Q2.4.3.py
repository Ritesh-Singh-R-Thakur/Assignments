# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:13:03 2024

@author: rites
"""

import numpy as np
from scipy import stats
from scipy.stats import norm

#n=100, Pop(population)Mean=50, Pop SD=40 

# For No investigation  P(45<X<55)
# For Investigation     1-P(45<X<55)

# find z-scores at x=45; z=(s_mean-Pop_mean)/(pop_SD/sqrt(n))
z1=(45-50)/(40/100**0.5)
z1#-1.25


# find z-scores at x=55; z=(s_mean-Pop_mean)/(pop_SD/sqrt(n))
z2=(55-50)/(40/100**0.5)
z2#1.25

# For No investigation P(45<X<55) using z_scores = P(X<50)-P(X<45)
I1=stats.norm.cdf(z2)-stats.norm.cdf(z1)
I1#0.7887004526662893

z=stats.norm.interval(I1,loc=50,scale=40/(100**0.5))
z#(45.00000495667348, 54.99999504332652)

# For Investigation 1-P(45<X<55)
I2=1-I1
I2#0.21130000000000004~24.13%

###########################

#Q4

#n=250, Pop(population)Mean=50, Pop SD=40 

# For No investigation  P(45<X<55)
# For Investigation     1-P(45<X<55)

# find z-scores at x=45; z=(s_mean-Pop_mean)/(pop_SD/sqrt(n))
z1=(45-50)/(40/250**0.5)
z1#-1.976423537605237


# find z-scores at x=55; z=(s_mean-Pop_mean)/(pop_SD/sqrt(n))
z2=(55-50)/(40/250**0.5)
z2#1.976423537605237

# For No investigation P(45<X<55) using z_scores = P(X<50)-P(X<45)
I1=stats.norm.cdf(z2)-stats.norm.cdf(z1)
I1#0.9518931721114805

z=stats.norm.interval(I1,loc=50,scale=40/(100**0.5))
z#(42.09430584957906, 57.90569415042094)

# For Investigation 1-P(45<X<55)
I2=1-I1
I2#0.0481068278885195~4.81%


