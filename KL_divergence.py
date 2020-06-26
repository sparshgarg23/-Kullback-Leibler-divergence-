#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:05:57 2020

@author: vkchlt0297
"""

from matplotlib import pyplot
from math import log2
import numpy as np
#Define event
events=['red','green','blue']
p=[0.10,0.40,0.50]
q=[0.80,0.15,0.05]
print('p=%.3f q=%.3f' % (sum(p),sum(q)))
pyplot.subplot(2,1,1)
pyplot.bar(events, p)
# plot second distribution
pyplot.subplot(2,1,2)
pyplot.bar(events, q)
# show the plot
pyplot.show()

def kl_divergence(p,q):
    return sum(p[i]*log2(p[i]/q[i]) for i in range(len(p)))

def js_divergence(p, q):
	m = 0.5 * (p + q)
	return 0.5 * kl_divergence(p, m) + 0.5 * kl_divergence(q, m)


kl_pq = kl_divergence(p, q)
#Note directly using p and q to calculate JS_DIVERGENCE RESULTS IN AN ERROR
#The issue here is the multiply operation by list is treated as creating N copies
#for example [1]*5 results in a list with1 being duplicated 5 times.
#Now when I do [1]*0.5 an error will pop up
#can't multiply sequence by non-int of type 'float'
#So you can either convert it into a numpy array(Smart and efficient)

 

p = np.asarray([0.10, 0.40, 0.50])
q = np.asarray([0.80, 0.15, 0.05])

js_pq=js_divergence(p,q)
print('KL(P || Q): %.3f bits' % kl_pq)
print('JS(P || Q): %.3f bits' % js_pq)
# calculate (Q || P)
kl_qp = kl_divergence(q, p)
js_qp=js_divergence(q,p)
print('KL(Q || P): %.3f bits' % kl_qp)
print('JS(Q || P): %.3f bits' % js_qp)
