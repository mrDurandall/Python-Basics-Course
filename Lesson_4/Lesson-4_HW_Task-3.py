# Задание 3 - Найти числа кратные 20 и 21 среди чисел от 20 до 240
print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])
