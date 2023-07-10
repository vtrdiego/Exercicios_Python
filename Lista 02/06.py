lista=[]
soma=0
mult=1

for i in range(5):
  numero=int(input('Digite o valor:'))
  lista.append(numero)
  soma+=numero
  mult*=numero

print(f'\nOs números são {lista}\nA soma deles é:{soma}\nE a multiplicação é:{mult}')