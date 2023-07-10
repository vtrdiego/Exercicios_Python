n=int(input("Digite um valor:"))

def soma(n):
  resposta=0
  for i in range(0,n+1):
    if i<=n:
      resposta+=i
  print(resposta)

soma(n)