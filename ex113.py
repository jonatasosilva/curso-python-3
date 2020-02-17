def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digital esse número.')
            return 0
        else:
            return n1


def leiaInt(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digital esse número.')
            return 0
        else:
            return n2


leiaInt('Digite um Inteiro: ')
leiaInt('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
