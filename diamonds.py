k = int(input('Введите высоту: '))
h = int(k/2+1/2)
print(h)

for i in range(h):
    for j in range(k):
        if h - 1 - i <= j <= h - 1 + i:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
   
for i in range(h + 1, k):
    for j in range(k + 1):
        if h * 2 <= k:                                                  # в случае, когда введенная высота чётная
            if j == i - h or j == h - 1 or j == k + h - i - 2:
                print('*  ', end='')
            else:
                print('   ', end='')
        elif h * 2 >= k:                                                # в случае, когда введенная высота нечётная
            if j == i - h or j == h - 1 or j == k + h - i - 1:
                print('*  ', end='')
            else:
                print('   ', end='')
    print()
print()
