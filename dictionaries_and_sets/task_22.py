"""Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств."""

lenght_first_set = int(input('Количество элементов первого множества: '))
lenght_second_set = int(input('Количество элементов второго множества: '))
count_sets_elements = {}

print('Задайте значения элементов первого множества.')
for i in range(lenght_first_set):
    element = int(input(f'{i + 1} число: '))
    dict_element = count_sets_elements.get(element)
    if dict_element is None:
        count_sets_elements[element] = 1
    else:
        count_sets_elements[element] += 1

print('Задайте значения элементов второго множества.')
for i in range(lenght_second_set):
    element = int(input(f'{i + 1} число: '))
    dict_element = count_sets_elements.get(element)
    if dict_element is None:
        count_sets_elements[element] = 1
    else:
        count_sets_elements[element] += 1

repeated_elements = []
for key, value in count_sets_elements.items():
    if value > 1:
        repeated_elements.append(key)

repeated_elements.sort()
print(*repeated_elements)