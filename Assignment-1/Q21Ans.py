# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:44:41 2024

@author: rites
"""

import pandas as pd 
df=pd.read_csv('Cars.csv')
df

#Q21a)	Check whether the MPG of Cars follows Normal Distribution 

df['MPG'].hist()
#from the histogram graph we can say that data is norammly distributed

#Q21b)Check Whether the Adipose Tissue (AT) and Waist Circumference (Waist) from wc-at data set follows Normal Distribution 

df1=pd.read_csv('wc-at.csv')
df1

df1['Waist'].hist()
#from waist histogram it seems to be following noraml distribution

df1['AT'].hist()
#from AT histogram it seems to be following positive skewed 
