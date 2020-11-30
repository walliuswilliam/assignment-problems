import matplotlib.pyplot as plt
import math


plt.style.use('bmh')
plt.plot([i for i in range(5)], [(1/(1+math.e**(-0.69*j+2.2))) for j in range(5)]) # plot line segments
plt.plot([1, 2, 3], [0.2, 0.25, 0.5], 'ro') # plot red ('r') circles ('o')
plt.savefig('33-1graph.png')