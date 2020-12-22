# Задание 4, 5, 6
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.

from sys import exit


class EquipmentStore:

    def __init__(self, name):
        self.store = {}
        self.name = name

    def supply(self, code, quantity, base):
        if code in self.store.keys():
            self.store[code] += quantity
        else:
            self.store.update({code: quantity})
        print(f'На склад {self.name} добавлен {base[code - 1]} в количестве {quantity} шт.')

    def manual_supply(self, base):
        code = input('Введите код техники: ')
        if int(code) > len(base):
            print('Ошибка! Товар с данным кодом отсусттвует в базе!')
            return None
        _ = True
        while _:
            quantity = input('Введите количество полученных единиц: ')
            if not quantity.isdecimal():
                print('Количество должно быть целым числом. Повторите ввод!')
            else:
                quantity = int(quantity)
                _ = False
        self.supply(int(code), int(quantity), base)

    def store_info(self, base):
        print(f'На складе {self.name} имеется:')
        for code, quant in self.store.items():
            print(f'{base[code - 1]} - {quant} шт.')

    def send(self, code, quantity, department, base):
        if code not in self.store.keys():
            print('Ошибка! Товар с данным кодом на складе отсутствует!')
        elif quantity > self.store[code]:
            print('Ошибка! На складе недостаточно товара!')
        else:
            print(f'Товар {base[code - 1]} в количестве {quantity} шт. передан в отдел {department}')
            self.store[code] -= quantity

    def manual_send(self, base):
        code = input('Введите код техники: ')
        if int(code) > len(base):
            print('Ошибка! Товар с данным кодом отсусттвует в базе!')
            return
        _ = True
        while _:
            quantity = input('Введите количество переданных единиц: ')
            if not quantity.isdecimal():
                print('Количество должно быть целым числом. Повторите ввод!')
            else:
                quantity = int(quantity)
                _ = False
        department = input('Введите название отдела: ')
        self.send(int(code), int(quantity), department, base)


class Equipment:
    __next_code = 1

    def __init__(self, name, etype, brandname):
        self.__code = Equipment.__next_code
        Equipment.__next_code += 1
        self.properties = {'Название': name,
                           'Вид': etype,
                           'Брэнд': brandname}

    def __str__(self):
        return f'Код: {self.__code},' \
               f' Тип: {self.properties.get("Вид")},' \
               f' Брэнд: {self.properties.get("Брэнд")},' \
               f' Название: {self.properties.get("Название")}'

    @property
    def getinfo(self):
        print(f'Код товара: {self.__code}. Характеристики:')
        for prop in self.properties.items():
            print(prop[0], ':', prop[1])
        return self.properties


class Printer(Equipment):

    def __init__(self, name, brandname, way, color, etype='Принтер'):
        super().__init__(name, etype, brandname)
        self.properties.update({'Способ печати': way,
                                'Цвет печати': color})


class Monitor(Equipment):
    def __init__(self, name, brandname, resolution, size, etype='Монитор'):
        super().__init__(name, etype, brandname)
        self.properties.update({'Разрешение': resolution,
                                'Дагональ (")': size})


class Computer(Equipment):
    def __init__(self, name, brandname, cpu, gpu, etype='Компьютер'):
        super().__init__(name, etype, brandname)
        self.properties.update({'Процессор': cpu,
                                'Видеокарта': gpu})


def eq_base_print(eq_base):
    print('Список закодированной техники:')
    for i in eq_base:
        print(i)


equipmentBase = []  # Список в который по порядку добавляются все создаваемые виды техники

# заполняем список несколькими элементами разных классов
equipmentBase.append(Printer('OfficeJet Pro 6230', 'HP', 'Струйный', 'Цветной'))
equipmentBase.append(Printer('Laser 107r', 'HP', 'Лазерный', 'ч/б'))
equipmentBase.append(Monitor('24mq', 'HP', '2k', 23.8))
equipmentBase.append(Monitor('UF270I', 'DEXP', '4k', 27))
equipmentBase.append(Computer('Super123', 'SuperPC', 'Intel i7', 'RTX 3070'))
equipmentBase.append(Computer('So-So-One', 'So-So PC', 'Intel i3', 'GTX 760'))
eq_base_print(equipmentBase)

store1 = EquipmentStore('Главный склад')
store1.supply(1, 2, equipmentBase)
store1.supply(2, 2, equipmentBase)
store1.supply(3, 5, equipmentBase)
store1.supply(4, 5, equipmentBase)
store1.supply(5, 5, equipmentBase)
store1.supply(6, 5, equipmentBase)
store1.store_info(equipmentBase)
store1.supply(1, 3, equipmentBase)
store1.store_info(equipmentBase)


while True:
    print(f'\nВыполняется работа со складом {store1.name}. Выберите действие:\n'
          f'ТОВАРЫ - для получения данных о базе товаров\n'
          f'ДАННЫЕ - для получения характеристик конкретного товара\n'
          f'СКЛАД - для получения данных о товарах на складе\n'
          f'ПОСТАВКА - для ввода данных о поставке на склад новой техники\n'
          f'ПЕРЕДАЧА - для передачи техники в подразделение компании\n'
          f'ВЫХОД - для заверщения работы')
    command = input('\n')
    if command.strip().upper() == 'ТОВАРЫ':
        eq_base_print(equipmentBase)
    elif command.strip().upper() == 'СКЛАД':
        store1.store_info(equipmentBase)
    elif command.strip().upper() == 'ДАННЫЕ':
        try:
            n = int(input('Введите код товара: ').strip())
            equipmentBase[n-1].getinfo
        except ValueError:
            print('Ошибка! Код товара должен быть целым положительным числом!')
    elif command.strip().upper() == 'ПОСТАВКА':
        store1.manual_supply(equipmentBase)
    elif command.strip().upper() == 'ПЕРЕДАЧА':
        store1.manual_send(equipmentBase)
    elif command.strip().upper() == 'ВЫХОД':
        print('Работа завершена! До свидания!')
        exit()
    else:
        print('Функция отсутствует или еще не реализована :(')
