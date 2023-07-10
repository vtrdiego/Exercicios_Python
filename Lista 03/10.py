n=int(input("Digite um valor:"))

def binario(n):
  lista=[]
  resp=n
  r=0
  while resp>=2:
    r=int(resp%2)
    resp=int(resp/2)
    lista.append(r)
    if(resp>=1 and resp<2):
      lista.append(resp)
  lista.reverse()
  print(lista)

binario(n)
