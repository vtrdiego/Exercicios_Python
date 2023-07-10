lista=[]
diferente=0

for i in range(10):
  valor=int(input('Digite o valor:'))
  lista.append(valor)

lista.sort()

for i in range(10):
  if i<9:
    if lista[i]!=lista[i+1]:
      diferente+=1

if diferente!=0:
  diferente+=1
  
print('\n')
print(lista)
print(f'Existem {diferente} valores diferentes!')