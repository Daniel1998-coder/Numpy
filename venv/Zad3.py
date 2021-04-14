import numpy as np
def a(n):
    temp = [2**x for x in range(1, n*n+1)]
    tab = np.array(temp)
    tab = tab.reshape((n, n))
    return tab
print(a(4))