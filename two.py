rows = int(input('Введите высоту: '))
for i in range(rows):
    for j in range(rows * 2 - 1):
        if j == rows - 1 - i or j == rows - 1 + i or i == rows - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()

