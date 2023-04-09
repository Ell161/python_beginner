"""Требуется определить, можно ли от шоколадки размером n × m долек
отломить k долек, если разрешается сделать один разлом по прямой
между дольками (то есть разломить шоколадку на два прямоугольника).
Числа вводятся построчно."""

n_size = int(input('Ведите число n: '))
m_size = int(input('Ведите число m: '))
chocolate_parts = int(input('Сколько долек нужно отломить? '))

if chocolate_parts < n_size * m_size and (chocolate_parts % n_size == 0 or chocolate_parts % m_size == 0):
    print('yes')
else:
    print('no')