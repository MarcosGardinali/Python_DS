from random import randrange, seed

randrange(0, 11)
seed(10)

notas_matematica = []
for i in range(8):
    notas_matematica.append(randrange(0, 11))
    
print(notas_matematica)