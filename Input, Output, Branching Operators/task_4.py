"""Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
чем Петя и Сережа вместе?"""

cranes = int(input('Введите количество сделанных журавликов: '))

if cranes % 6 != 0 or cranes < 1:
    print('Нельзя определить')
else:
    crane_child = cranes // 6
    print(f'Петя и Сережа сделали по {crane_child} журавликов, Катя сделала {4 * crane_child} журавликов')