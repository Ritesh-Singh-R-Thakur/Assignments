# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 18:14:02 2024

@author: rites
"""

#Q1:find the outliers and find out  μ,σ,σ^2


import pandas as pd

df=pd.read_excel('Q1.xlsx')
df

df['Measure'].mean()#33.27133333333333
df['Measure'].std()#16.945400921222028
df['Measure'].var()#287.1466123809524

#Histogram
df['Measure'].hist()

df.dtypes

#scatterplot
df.plot.scatter(x='Measure',y='Name of company')

#Boxplot
df.boxplot(column=['Measure'],vert=False)

#piechart
import matplotlib.pyplot as plt
plt.pie(x=df['Measure'],labels=df['Name of company'])
plt.show()

#from Pie chart we can see that morgan stanley is the outlier
