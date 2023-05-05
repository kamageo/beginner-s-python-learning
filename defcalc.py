def sum(a, b):
    return a + b

def dif(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
opt = input('Выберите знак(+, -, *, /): ' )
if opt == '+':
    print('Сумма равна', sum(a, b))
elif opt == '-':
    print('Разность равна', dif(a, b))
elif opt == '*':
    print('Произведение равно', mult(a, b))
elif opt == '/':
    print('Частное равно', div(a, b))
else:
    print('Неверный выбор.')