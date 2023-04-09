# Найдите сумму цифр трехзначного числа.

user_number = int(input('Введите трехзначное число: '))
sum_digits = user_number // 100 + user_number % 100 // 10 + user_number % 10
print(f'Сумма цифр заданного числа равна {sum_digits}')