import random

lista=[]
valores=[]

for i in range(10):
  valor=random.randint(1,6)
  lista.append(valor)

lista.sort()

for i in range(1,7):
  valores.append(lista.count(i))
  
print(lista)
print(valores)