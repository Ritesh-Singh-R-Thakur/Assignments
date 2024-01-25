# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:10:11 2023

@author: rites
"""

L1=[34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56]
len(L1)
L1.sort()
L1
sum(L1)
avg=sum(L1)/len(L1)
avg

import numpy as np

x1=np.array([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])
np.mean(x1)
np.median(x1)
np.var(x1)
np.std(x1)


import pandas as pd
import scipy as stats
import scipy.stats as binom
import numpy as np

df=pd.read_csv('Cars.csv')
df

np.mean(df['MPG'])
np.min(df['MPG'])
np.max(df['MPG'])
#P(MPG>38)

r1=1-stats.binom.cdf((38,cars.MPG.mean(),cars.MPG.std()))
######################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm


cars=pd.read_csv('Cars.csv')
cars

sns.boxplot(cars.MPG,orient=vars)

# P(MPG>38)
1-stats.norm.cdf(38,cars.MPG.mean(),cars.MPG.std())

###############################################

###Q11###

#mean=200 sd=30

from scipy.stats import norm
nd_p=norm.interval(0.94,200,30)
nd_p

#########################(1-jan-2024)

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















