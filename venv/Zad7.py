import numpy as np
from math import *
def a(n):
     tab = [x*2 for x in range(1, n+1)]
     temp = []
     for x in range(0, n):
        for y in range(0, n):
             temp.append(tab[abs(x-y)])
     wyn = np.array(temp)
     wyn = wyn.reshape((n,n))
     return wyn
print(a(10))