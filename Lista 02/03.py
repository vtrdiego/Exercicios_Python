lista=[]
pares=[]

for i in range(4):
  valor=int(input('Digite o valor da lista:'))
  lista.append(valor)
  if valor%2==0:
    pares.append(valor)


print('\n')
print(lista)
print(f'O número 9 aparece {lista.count(9)} vezes')
print(f'A primeira repetição do 3 aparece na coluna {lista.index(3)}')
print(f'Os pares da lista são {pares}')