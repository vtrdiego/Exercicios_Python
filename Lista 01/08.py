lista= []
for i in range(100, 401):
    s = str(i) ----#str serve para convertar um elemento em string?
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        lista.append(s)#append serve para ir adicionando novos elementos num array de forma dinâmica
print(",".join(lista))