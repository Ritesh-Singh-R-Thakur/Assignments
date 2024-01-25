# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 17:28:07 2023

@author: rites
"""

import pandas as pd

df_b=pd.read_csv('Q9_b.csv')
df_b

df_b.dtypes

df_b['SP'].hist()
df_b['SP'].skew()
df_b['SP'].kurt()


df_b['WT'].hist()
df_b['WT'].skew()
df_b['WT'].kurt()

df_b.skew()
df_b.kurt()
