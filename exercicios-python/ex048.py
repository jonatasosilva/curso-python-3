m = 0
s = 0
for c in range(1, 501):
    if c % 2 == 0 and c % 3 == 0:
        m += 1
        s += c
print('A soma dos {} valores solicitados é {}'.format(m, s))
