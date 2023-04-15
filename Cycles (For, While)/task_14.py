# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

user_number = int(input('Введите число: '))

if user_number < 2:
    print('Числового ряда 2^k не существует.')
else:
    current_number = 2
    number_degree = 1
    while current_number ** number_degree < user_number:
        print(current_number ** number_degree, end=' ')
        number_degree += 1
