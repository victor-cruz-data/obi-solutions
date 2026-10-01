"""
Solução com outra abordagem, utilizei um algoritmo de varredura dupla pela primeira vez
"""

N = int(input())
fita_str = input().split(" ")
a = []
for i in fita_str: a.append(int(i))
posicao_ultimo_zero = -1
# esquerda pra direita
for i in range(len(a)):
    if a[i] == 0:
        posicao_ultimo_zero = i
        continue
    if posicao_ultimo_zero == -1:
        a[i] = 10001
        continue
    else:
        a[i] = min(i-posicao_ultimo_zero, 9)
#direita pra esquerda
posicao_ultimo_zero = -1
for i in range(len(a)-1, -1, -1):
    if a[i] == 0:
        posicao_ultimo_zero = i
        continue
    if posicao_ultimo_zero == -1: continue
    else:
        a[i] = min(a[i], posicao_ultimo_zero-i, 9)
print(*a)