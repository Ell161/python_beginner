"""Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
return sum(a, b) + 1 - такое использовать нельзя"""


def sum_numbers(number1, number2):
    if number1 < 0 or number2 < 0:
        raise 'Числа должны быть не отрицательными!'
    elif number1 == 0:
        return number2
    else:
        return sum_numbers(number1 - 1, number2 + 1)


first_number = int(input('Первое число: '))
second_number = int(input('Второе число: '))
print(sum_numbers(first_number, second_number))