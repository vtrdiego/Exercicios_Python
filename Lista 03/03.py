a=int(input('Digite o valor de A:'))
b=int(input('Digite o valor de B:'))
limite=int(input('Digite o valor do limite:'))

def valores(a,b,limite):
  if a+b>limite:
    print('\nTrue')
  else:
    print('\nFalse')

valores(a,b,limite)