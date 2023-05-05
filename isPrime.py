def isPrime(num):
    sarea = range(2, num)
    for i in sarea:
        if num % i == 0:
            return False
        return True

num = int(input('Введите число: '))
if isPrime(num):
    print('Число является простым')
else:
    print('Число является составным')