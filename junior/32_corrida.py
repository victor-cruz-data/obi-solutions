"""
Basicamente soma os tempos e vê qual foi o menor.
É garantido que não há dois competidores com o mesmo tempo final.
Máximo tempo usado 	0,027 s
Máxima memória usada 	4.2 MB

"""
d = [int(x) for x in input().split()]
N, M = d[0], d[1]
menor_tempo_total = 0
for i in range(N):
    total = [int(x) for x in input().split()]
    total = sum(total)
    if i == 0:
        menor_tempo_total = total
        corredor = i + 1
    else:
        if total < menor_tempo_total:
            menor_tempo_total = total
            corredor = i + 1
print(corredor)
