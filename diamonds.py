# C
k = int(input('Введите высоту для ромба C (нечётное значение): '))
h = int(k / 2 + 1 / 2)
print(h)

for i in range(h):
    for j in range(k):
        if h - 1 - i <= j <= h - 1 + i:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()

for i in range(h + 1, k + 1):
    for j in range(k + 1):
        if j == i - h or j == k + h - i - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()


# D
k = int(input('Введите высоту для ромба D (нечётное значение): '))
h = int(k / 2 + 1 / 2)
for i in range(h):
    for j in range(k):
        if h - 1 - i <= j <= h - 1 + i:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
for i in range(h + 1, k + 1):
    for j in range(k + 1):
        if j == i - h or j == h - 1 or j == k + h - i - 1:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()
