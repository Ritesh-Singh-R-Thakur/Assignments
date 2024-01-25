# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:03:43 2024

@author: rites
"""

# Q 24)   A Government company claims that an average light bulb lasts 270 days.
# A researcher randomly selects 18 bulbs for testing. The sampled bulbs last an 
#average of 260 days, with a standard deviation of 90 days. If the CEO's claim 
#were true, what is the probability that 18 randomly selected bulbs would have 
#an average life of no more than 260 days

#h0=mean>260
#h1=mean<=260
#mu=270days, sample=18=n,df=n-1=17, xbar=260days, sd=90days


from scipy import stats
from scipy.stats import norm

# Ho = Avg life of Bulb >= 260 days
# H1 = Avg life of Bulb < 260 days

# find t-scores at xbar=260; t=(s_mean-P_mean)/(s_SD/sqrt(n))
t=(260-270)/(90/18**0.5)
t#=-0.4714045207910317

# Find P(X>=260) 
p_value=1-stats.t.cdf(abs(-0.4714),df=17)
p_value#= 0.32167411684460556

pval=0.3216
alpha=0.05
if pval<alpha:
    print('h0 is rejected and h1 is accepted')
else:
    print('ho is accepted and h1 is rejected')

#ho is accepted and h1 is rejected
















