lista=["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
cont=0

print('Responda com sim ou não:\n')
for i in range(5):
  print(lista[i])
  resp=input().upper()
  if resp=="SIM":
    cont=cont+1

if cont==2:
  print('\nA pessoa é suspeita!')
elif cont==3 or cont==4:
  print('\nA pessoa é cúmplice!')
elif cont==5:
  print('\nA pessoa é a assassina!')
elif cont==0 or cont==1:
  print('\nA pessoa é inocente!')