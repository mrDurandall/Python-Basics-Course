# Задание 3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.

emplSalary = []
print('Список сотрудников:\n\n'
      'Фамилия:    | Оклад:\n'
      '----------------------')

with open('Task-3-file.txt', 'r') as employeesDB:
    for employee in employeesDB:
        print(f'{employee.split()[0][:11]:<12}| {employee.split()[1]}')
        emplSalary.append((employee.split()[0], float(employee.split()[1])))

print('\nСледующие сотрудники имеют оклад менее 20000 р. :')
salarySum = 0
for employee, salary in emplSalary:
    salarySum += salary
    if salary < 20000:
        print(employee)
print(f'\nСредний доход всех сотрудников: {salarySum/len(emplSalary):.2f} р.')

