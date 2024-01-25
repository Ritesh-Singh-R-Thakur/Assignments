# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:56:37 2023

@author: rites
"""

import pandas as pd

df_a=pd.read_csv('Q9_a.csv')
df_a

df_a.dtypes

df_a['speed'].hist()
df_a['speed'].skew()
df_a['speed'].kurt()


df_a['dist'].hist()
df_a['dist'].skew()
df_a['dist'].kurt()

df_a.skew()
df_a.kurt()
