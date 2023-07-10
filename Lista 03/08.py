ano=int(input("Digite o ano para saber se � bissexto:"))

def bi(ano):
  if ano%4==0 or ano%400==0 and ano%100!=0:
    return True
  else:
    return False

print(bi(ano))