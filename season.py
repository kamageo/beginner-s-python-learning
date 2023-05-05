month = input('Введите порядковый номер месяца: ')
month = int(month)
if month == 12:
    if 0 < month <= 2:
        print('зима')
if month >= 3:
    if month <= 5:
        print('весна')
if month >= 6:
    if month <=8:
        print('лето')
if month >= 9:
    if month <= 11:
        print('осень')