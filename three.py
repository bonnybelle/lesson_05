k = int(input('Введите высоту: '))
h = int(k/2)
print(h)
for i in range(h):
    for j in range(k):
        if j == h - 1 - i or j == h - 1 + i:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()
for i in range(h + 1, k):
    for j in range(k - 1):
        if j == i - h or j == k - i + 3:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
print()
