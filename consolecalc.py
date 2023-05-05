from modulecalc import *

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
op = input('Введите необходимое для выполнения действие: ')

if op == 'Сложение':
    print('Сумма равна', sum(a, b))

elif op == 'Вычитание':
    print('Разность равна', dif(a, b))

elif op == 'Умножение':
    print('Произведение равно', mult(a, b))

elif op == 'Деление':
    print('Частное равно', div(a, b))

else:
    print('Ошибка.')