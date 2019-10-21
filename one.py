rows = int(input('Введите высоту: '))
for i in range(rows):
    for j in range(rows * 2):
        if rows - 1 - i <= j <=  rows - 1 + i:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()

