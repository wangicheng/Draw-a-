import numpy as np
import matplotlib.pyplot as plt
from math import pi,e

x = np.linspace(0, 3, 200)



y = (x)*(1.5*x-3.5)
y2= x*(x-2)



plt.figure(figsize=(8,8), dpi=100)
plt.title(("R.G.Bun"), size=30)
ax = plt.gca()
ax.set_facecolor('#ffaa00')
plt.plot(x,y, c='#2222aa', lw=4)
plt.plot(x,y2, c='#2222aa', lw=4)

        
        
plt.show()