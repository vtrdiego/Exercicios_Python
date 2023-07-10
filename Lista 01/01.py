a=1
b=1
proximo=0;

n=int(input('Digite o número:'))

for i in range(n):
  proximo=a+b
  a=b
  b=proximo
  print(a)