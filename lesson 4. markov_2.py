import numpy as np
import matplotlib.pyplot as plt

N = 1000
sigma = 5
r = 0.99
en = np.sqrt((1-r*r)*sigma*sigma)

fSignal = np.zeros(N)
fSignal[0] = np.random.normal(0, sigma)
for i in range(1, N):
    fSignal[i] = r*fSignal[i-1] + np.random.normal(0, en)

plt.plot(fSignal)
plt.grid(True)
plt.show()
