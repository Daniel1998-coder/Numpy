import numpy as np
def a(n):
    tab = np.diag([b for b in range(n, 0, -1)], 2)
    return tab
print(a(5))