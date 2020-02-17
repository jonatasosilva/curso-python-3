from datetime import date
anoatual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoatual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, anoatual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}'.format((18 - idade) + anoatual))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(anoatual - (idade - 18)))
else:
    print('Você deve ser alistar IMEDIATAMENTE!')