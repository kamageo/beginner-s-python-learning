number = input('Введите число: ')
m = int(number)
n = int(number[-1])
ending = 'ов'
if m < 5 or m > 20:
    if n == 1:
        ending = ''
    if 1 < n < 5:
        ending = 'a'
print(str(number) + ' компьютер' + ending)
