lista=[1,8,5,7,3]
lista.sort()

def maior(lista):
  cont=0
  n=int(input("Digite o valor limite:"))
  for i in range(len(lista)):
    if lista[i]>n:
      return lista[i]
    else:
      cont=i+1
      if cont==(len(lista)):
        return -1
  
print(maior(lista))