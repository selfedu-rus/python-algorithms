#-------------------------------------------------
# Быстрая сортировка Хоара через рекурсию
#-------------------------------------------------
import random


def quick_sort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a)-1)]      # случайное пороговое значение (для разделения на малые и большие)
        low = [u for u in a if u < x]
        eq = [u for u in a if u == x]
        hi = [u for u in a if u > x]
        a = quick_sort(low) + eq + quick_sort(hi)

    return a


a = [9, 5, -3, 4, 7, 8, -8]
a = quick_sort(a)

print(a)
