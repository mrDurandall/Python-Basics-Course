# Задание 7 - Факториал
def fact(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
        yield res


for el in fact(5):
    print(el)
