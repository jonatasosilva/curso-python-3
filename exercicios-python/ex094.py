galera = list()
pessoa = dict()
idadetotal = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    idadetotal += pessoa['idade']
    galera.append(pessoa.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper()
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
idademedia = idadetotal / len(galera)
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {idademedia:5.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print(f'\nD) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= idademedia:
        print('   ', end='')
        for k, v in p.items:
            print(f'{k} = {v}', end=' ')
        print()
print('<<< ENCERRADO >>>')
