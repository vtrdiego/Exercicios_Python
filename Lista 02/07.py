idade=[]
altura=[]

for i in range(1,6):
  idade.append(int(input(f'Digite a idade da pessoa {i}:')))
  altura.append(float(input(f'Digite a altura da pessoa {i}:')))
  print('\n')

idade.reverse()
altura.reverse()

print('\n')
print(idade)
print(altura)