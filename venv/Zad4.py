import numpy as np
def a(b, c):
     y = [b**x for x in range(1, c+1)]
     return y
print(a(2,5))