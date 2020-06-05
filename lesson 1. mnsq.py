import numpy as np
import matplotlib.pyplot as plt

N = 100     # число экспериментов
sigma = 3   # стандартное отклонение наблюдаемых значений
k = 0.5     # теоретическое значение параметра k
b = 2       # теоретическое значение параметра b

x = np.array(range(N))
f = np.array([k*z+b for z in range(N)])
y = f + np.random.normal(0, sigma, N)

# вычисляем коэффициенты
mx = x.sum()/N
my = y.sum()/N
a2 = np.dot(x.T, x)/N
a11 = np.dot(x.T, y)/N

kk = (a11 - mx*my)/(a2 - mx**2)
bb = my - kk*mx
ff = np.array([kk*z+bb for z in range(N)])

plt.scatter(x, y, s=2, c='red')
plt.plot(f)
plt.plot(ff, c='red')
plt.grid(True)
plt.show()
