import random
dado=[]
perc=0

for i in range(50):
  valor=random.randint(1,6)
  dado.append(valor)
  if valor==6:
    perc+=1

perc=(perc*50)/100

print(dado)
print(f'\nO percentual do valor 6 é %{perc}')