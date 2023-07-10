somapar=0
somaimp=0
quadrado=0
somaquad=0
digNum=0

for n in range(1,101):
    if n%2==0:
        somapar+=n
    if n<100:
        quadrado=n*n
        somaquad+=quadrado
    if n%2!=0:
        somaimp+=n

print(f'A soma dos pares é:{somapar}\nA soma dos quadrados é:{somaquad}\nA soma dos ímpares é:{somaimp}')

n=int(input('Digite o valor de n:'))

u=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
um=n//10000%10

vet=[u,d,c,m,um]

for r in range(len(vet)):
  if vet[r]%2!=0:
    digNum+=vet[r]
print(digNum)