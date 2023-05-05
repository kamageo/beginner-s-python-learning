a = float(input(''))
b = float(input(''))
def square(a, b):
    area1 = int(a * b)
def perimeter(a, b):
    area2 = int((a + b) * 2)
opt = int(input(''))
if opt != 1 and opt != 2:
    print('')
if opt == 1:
    print('', square(a,b))
if opt == 2:
    print('', perimeter(a,b))