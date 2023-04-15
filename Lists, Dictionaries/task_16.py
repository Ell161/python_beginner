"""Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X"""

import random

lenght_list = int(input('Задайте длину массива: '))
number_list = [random.randint(0, 10) for _ in range(lenght_list)]
print('Список чисел: ', *number_list)

desired_number = int(input('\nВведите число для поиска: '))
count_desired_number = number_list.count(desired_number)
if count_desired_number == 0:
    print('\nЗаданного значения нет в массиве')
else:
    print(f'\nЗаданное число встречается в массиве {count_desired_number} раз(а)')
