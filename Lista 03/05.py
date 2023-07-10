nota=float(input("Digite a nota do aluno:"))

def conceito(nota):
  if nota<=1.67:
    print("Conceito F")
  if nota>1.67 and nota <=3.34:
    print("Conceito E")
  if nota>3.34 and nota <=5.01:
    print("Conceito D")
  if nota>5.01 and nota <=6.68:
    print("Conceito C")
  if nota>6.68 and nota <=8.35:
    print("Conceito B")
  if nota>8.35 and nota<=10.00:
    print("Conceito A")

conceito(nota)