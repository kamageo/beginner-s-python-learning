numbers = [4, 8, 15, 16, 23, 42]

sum = sum(numbers)

prod = 1
for x in numbers:
    prod = prod * x

print('Сумма: ' + str(sum))
print('Произведение: ' + str(prod))