import numpy as np
import matplotlib.pyplot as plt

N = 30         # число наблюдений
dNoise = 0.01     # дисперсия шума
en = 0.01     # дисперсия изменения сигнала
a = 0.9        # корреляция между соседними отсчетами
x0 = 76         # начальная масса
ex = en/(1-a*a) # дисперсия сигнала (относительно нуля)

# моделируем изменение веса
x = np.zeros(N)
x[0] = 0
for i in range(1, N):
    x[i] = a*x[i-1] + np.random.normal(0, en)

x += x0

# формируем наблюдения
z = x + np.random.normal(0, dNoise, N)

#формируем вспомогательные матрицы
R = np.array([[a**np.abs(i-j) for j in range(N)] for i in range(N)])
V = np.eye(N)*dNoise
RVinv = np.linalg.inv(R+V/ex)

# построение оценок
mz = z.mean() # среднее значение наблюдений
xx = np.zeros(N)
for k in range(N):
    alfa = np.dot(R[:, k], RVinv)
    xx[k] = np.dot(alfa, (z-mz)) + mz

# отображение результатов
fig, ax = plt.subplots()
ax.plot(x)
ax.plot(xx)
ax.plot(z)

ax.grid(True)
plt.show()
