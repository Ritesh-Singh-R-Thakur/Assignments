# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 23:45:10 2024

@author: rites
"""
#A
#mean=38y,sd=6,sample=400

from scipy.stats import norm
nd1= norm(38,6)#mean,sd

#p(38<x<44)

p1=nd1.cdf(44)-nd1.cdf(38)
p1.round(4)#0.3413(34.13%)

#p(x>44)
p2=1-nd1.cdf(44)
p2.round(4)#0.1587(15.87%)

#From above we can see that ages between 38 to 44 years probability is 34.13% which is more than that of 15.87% of probability of age more than 44years

#B
#P(x<30)
p3=nd1.cdf(30)
p3
0.09121121972586788*400
#36.484487890347154 employees 





