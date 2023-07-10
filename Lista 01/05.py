salario=int(input('Digite o valor do salário:'))
gastos=int(input('Digite o valor dos gastos:'))

if gastos>salario:
    print('Orçamento estourado!')
elif gastos<salario:
    print('Gastos dentro do orçamento!')