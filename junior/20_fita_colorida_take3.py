"""
Maior abstração, sem precisar controlar a ultima posição do zero,
considerando apenas a distancia

Máximo tempo usado = 0,033 s
Máxima memória usada = 4.81 MB
"""

N = int(input())
a = [int(x) for x in input().split()]
# esquerda pra direita
distancia = 10001
for i in range(len(a)):
    if a[i] == 0: distancia = 0
    else: distancia += 1
    a[i] = distancia

#direita pra esquerda
distancia = 10001
for i in range(len(a)-1, -1, -1):
    if a[i] == 0: distancia = 0
    else: distancia += 1
    a[i] = min(a[i], distancia, 9)
print(*a)