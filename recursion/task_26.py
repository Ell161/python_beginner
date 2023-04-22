"""Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии."""


def number_degree(number: int, degree: int) -> int:
    if degree == 0:
        return 1
    return number * number_degree(number, degree - 1)


user_number = int(input('Введите число: '))
degree = int(input('Степень числа: '))
print(number_degree(user_number, degree))
