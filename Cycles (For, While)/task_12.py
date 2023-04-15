"""Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа
X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает
две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа."""


def Petya_value(number):
    try:
        value = int(input(f'{number}-е значение: '))
        if value > 1000 or value < 1:
            raise ValueError
    except ValueError:
        print('Недопустимое значение! Введите натуральное число от 1 до 1000.')
        value = Petya_value(number)
    return value


print('Петя загадывает числа.')
first_think_value = Petya_value(1)
second_think_value = Petya_value(2)

print(f'Сумма загаданных чисел равна {first_think_value + second_think_value}, '
      f'а их произведение {first_think_value * second_think_value}')


print('Катя угадывает числа.')
while True:
    first_guess_value = int(input('1-е значение: '))
    second_guess_value = int(input('2-е значение: '))
    if (first_think_value + second_think_value == first_guess_value + second_guess_value) and \
            (first_think_value * second_think_value == first_guess_value * second_guess_value):
        print('Оба числа угаданы верно!')
        break
    elif (first_guess_value == first_think_value or first_guess_value == second_think_value) or (
            second_guess_value == first_think_value or second_guess_value == second_think_value):
        print('Одно из чисел угадано верно! Попробуй еще раз.')
    else:
        print('Ни одно из чисел не совпадает с загаднаммыи! Попробуй еще раз.')
