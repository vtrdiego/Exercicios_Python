a=int(input('Digite o valor de A:'))
b=int(input('Digite o valor de B:'))
limite=int(input('Digite o valor do limite:'))

def valores(a,b,limite):
  if a > limite and b > limite:
    print(2)
  elif a > limite or b > limite:
    print(1)
  else:
    print(0)

valores(a,b,limite)