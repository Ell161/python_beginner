"""Требуется найти в массиве A[1..N] самый близкий по величине
элемент к заданному числу X. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X.
Если таких значений больше одного, вывести первый найденный."""

import random

lenght_list = int(input('Задайте длину массива: '))
number_list = [random.randint(0, 100) for _ in range(lenght_list)]
print('Список чисел: ', *number_list)
user_number = int(input('\nВведите число: '))
difference = abs(user_number - number_list[0])
desired_element = number_list[0]

for i in range(1, lenght_list - 1):
    if difference > abs(user_number - number_list[i]):
        difference = abs(user_number - number_list[i])
        desired_element = number_list[i]

print(f'Наиболее близкий по значению элемент к заданному {desired_element}')
