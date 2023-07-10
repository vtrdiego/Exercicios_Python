lista=[1,2,-3,5,6,6,-2,8,9,-1]
positivos=[]
unicos=[]

lista.sort()

for i in range(10):
  if lista[i]>0:
    positivos.append(lista[i])

for i in range(len(positivos)):
  if i<(len(positivos)-1):
    if positivos[i]!=positivos[i+1]:
      unicos.append(positivos[i])
  else:
      unicos.append(positivos[i])

print(lista)
print(positivos)
print(unicos)