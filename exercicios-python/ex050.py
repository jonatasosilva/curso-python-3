s = 0
cc = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        s += n
        c += 1
print('Você informou {} números e a soma foi{}'.format(cc, s))