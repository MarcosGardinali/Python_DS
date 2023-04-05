import matplotlib.pyplot as plt
from random import randrange, seed

randrange(0, 11)
seed(10)

notas_matematica = []
for i in range(8):
    notas_matematica.append(randrange(0, 11))
    
print(notas_matematica)

x = list(range(1, 9))
y = notas_matematica

plt.plot(x, y, marker='o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()