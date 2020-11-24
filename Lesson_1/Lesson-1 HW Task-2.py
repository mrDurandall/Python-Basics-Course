# Задание 2 - время из секунд в ЧЧ:ММ:СС
print('Задание 2 - время из секунд в ЧЧ:ММ:СС')
time = int(input('Введите время в секундах:'))
seconds = time % 60
hours = time // 3600
minutes = time % 3600 // 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
