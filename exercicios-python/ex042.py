s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR triângulo', end ='')
    if s1 == s2 == s3:
       print(' EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print(' ESCALENO!')
    else:
        print(' ISÓSCELES!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
