idade = int(input("Digite sua idade: "))

def verificaIdade(idade):    
    if idade < 18:
        print(f'Você é menor de idade, tem {idade} anos e não pode dirigir')
    else:
        print(f'Você é maior de idade, tem {idade} anos e já pode dirigir')

verificaIdade(idade)