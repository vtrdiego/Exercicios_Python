n=int(input("Digite um valor:"))

def potencia(n):
  resp=0
  for i in range(1,n+1):
    if i<=n:
      resp=i*i
      print(resp)

potencia(n)