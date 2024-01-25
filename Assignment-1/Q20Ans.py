# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:32:46 2024

@author: rites
"""

import pandas as pd 
df=pd.read_csv('Cars.csv')
df

df['MPG']
mean=df['MPG'].mean()
sd=df['MPG'].std()
mean
sd
from scipy.stats import norm

pd=norm(mean,sd) 

#P(MPG>38)

p1=1-pd.cdf(38)
p1#=0.34759392515827137

#P(MPG<40)

p2=pd.cdf(40)
p2#=0.7293498762151609

#P (20<MPG<50)

p3=pd.cdf(50)-pd.cdf(20)
p3#=0.8988689169682047



