i=int(input('Digite um valor de i:'))
a=int(input('Digite um valor de a:'))
b=int(input('Digite um valor de b:'))
c=int(input('Digite um valor de c:'))

if i%2==0:
  media=(a+b+c)/3
  print(f'A média aritmética de a b c é:{media}')
elif i%2!=0 and i>10:
  media=(a+b+c)/3
  ponderada=(a*2+b*3+c*4)/9
  print(f'\nA média aritmética de a b c é:{media}')
  print('A média ponderada é:{:.1f}'.format(ponderada))
else:
  print('\nValor não é par e é menor que 10!')