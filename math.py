class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        print("Производится сложение...")
        return self.a + self.b

    def dif(self):
        print("Производится вычитание...")
        return self.a - self.b

    def mult(self):
        print("Производится умножение...")
        return self.a * self.b

    def div(self):
        print("Производится деление...")
        return self.a / self.b


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
calc = Calc(a, b)
opt = input('Выберите знак(+, -, *, /): ')
if opt == '+':
    print('Сумма равна', calc.sum())
elif opt == '-':
    print('Разность равна', calc.dif())
elif opt == '*':
    print('Произведение равно', calc.mult())
elif opt == '/':
    print('Частное равно', calc.div())
else:
    print('Неверный выбор')