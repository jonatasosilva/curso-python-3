def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO NEGADO.'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
