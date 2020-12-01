# Задание 4 - возведение в отрицательную степень.
print('Задание 4 - Возведение в отрицательную степень')
def exponentation1(base, power):
    """Решение через **
    просто возводим основание base в степень power"""
    return base ** power

def exponentation2(base, power):
    """Решение без использования **
    возведение n в степень -m - это умножение 1/n само на себя m раз"""
    res = 1
    for i in range(0, power, -1):
        res = res * 1/base
    return res

print(f'{exponentation1(6, -2):.4e}')
print(f'{exponentation2(6, -2):.4e}')