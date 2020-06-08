n = int(input('Digite um número: '))
ndivisoes = 0
for c in range(1, n+1, 1):
    if n % c == 0:
        print('\033[1;33m', end = '')
        ndivisoes += 1
    else:
        print('\033[1;31m', end = '')
    print(c, end=' ')
print('\n\33[mO número {} foi divisível {} vezes'.format(n, ndivisoes))
if ndivisoes == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')