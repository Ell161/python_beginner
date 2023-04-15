"""На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые
нужно перевернуть, чтобы все монетки были повернуты вверх одной и
той же стороной. Выведите минимальное количество монет, которые нужно
перевернуть. С клавиатуры вводятся число монет и сами монеты построчно."""


def input_value_coin(coin):
    try:
        value = int(input(f'{coin + 1}-я монетка: '))
        if value != 0 and value != 1:
            raise ValueError
    except ValueError:
        print('Введено недопустимое значение. Повторите!')
        value = input_value_coin(coin)
    return value


count_coins = int(input('Сколько монеток лежит на столе? '))

heads = 0
tails = 0
print('Введите все значения монеток ("0" - орел, "1" - решка).')

for i in range(count_coins):
    value_coin = input_value_coin(i)
    if value_coin == 0:
        heads += 1
    elif value_coin == 1:
        tails += 1

print(f'Минимальное, количнство моенток, которое нужно перевернуть - {min(heads, tails)}')