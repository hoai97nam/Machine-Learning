import numpy as np
from math import pi

x=np.array([1,4,5,2])

y=pi/2-x
print(y)
z=np.cos(x) -np.sin(y)
print(z[3])

for i in range(4):
    res = z[i]+res

