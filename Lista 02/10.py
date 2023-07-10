vetor = [5.3,8,9.7,4,2,4.58,74,68,53.79]
media=(sum(vetor))/len(vetor)
menos=0
menorMe=99999999
menorMa=99999999
flag=0
flagi=0

for i in range(len(vetor)):
  if vetor[i]<=media:
    menos=media-vetor[i]
    if menos<menorMe:
      menorMe=menos
      flag=i
  if vetor[i]>=media:
    menos=vetor[i]-media
    if menos<menorMa:
      menorMa=menos
      flagi=i

print('\n',media)
if menorMe<menorMa:
  print(f'\nO valor mais próximo é: {vetor[flag]}')
else:
  print(f'\nO valor mais próximo é: {vetor[flagi]}')