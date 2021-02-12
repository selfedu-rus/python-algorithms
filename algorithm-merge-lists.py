#-------------------------------------------------
# Метод слияния двух списков
#-------------------------------------------------

a = [1, 4, 10, 11]
b = [2, 3, 3, 4, 8]
c = []

N = len(a)
M = len(b)

i = 0
j = 0
while i < N and j < M:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

c += a[i:] + b[j:]

# if i < N:
#     for k in range(i, N):
#         c.append(a[k])
# elif j < M:
#     for k in range(j, M):
#         c.append(b[k])

print(c)
