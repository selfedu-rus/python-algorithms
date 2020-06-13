import numpy as np

def getL(y1, m1_F, m1_M, d1):
    res = 1/(2*d1)*((y1-m1_F)**2 - (y1-m1_M)**2)
    return res

def getL0(p0, p1):
    return np.log(p0/p1)

m1_F = 60   # средний вес женщин (кг)
m1_M = 85   # средний вес мужчин (кг)

d1 = 9     # дисперсия разброса веса (кг^2)

p0 = 0.48   # вероятность для женщин
p1 = 0.52   # вероятность для мужчин

N = 100     # число экспериментов

L0 = getL0(p0, p1)

nM = 0
for i in range(N):
    y1 = np.random.normal(m1_F, d1)

    L = getL(y1, m1_F, m1_M, d1)

    if(L >= L0):
        print("Мужчина", y1)
        nM += 1
    else:
        print("Женщина", y1)

error = nM/N*100
print(f"Ошибка: {np.round(error, 2)}%")