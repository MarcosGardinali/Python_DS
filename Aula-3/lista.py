idades = [14, 16, 19, 21]
def podeDirigir(idades):
    for idade in idades:
        if idade >= 18:
            print(f'Tem {idade} anos, pode dirigir')
        else:
            print(f'Tem {idade} anos, não pode dirigir')
podeDirigir(idades)
