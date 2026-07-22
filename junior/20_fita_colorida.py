"""
A primeira solução que montei que passou em todos os testes. Primeira vez que
apliquei de maneira prática a ideia de bissect.

Máximo tempo usado = 0,036 s
Máxima memória usada = 4.89 MB
"""

import bisect

N = int(input())
L_str = input().split()
indices_zero = []
for i in range(len(L_str)):
    if L_str[i] == "0": indices_zero.append(i)
final = []
for i in range(len(L_str)):
    insere = bisect.bisect_left(indices_zero, i)
    if insere == 0:
        final.append(min(abs(i-indices_zero[insere]), 9))
    elif insere < len(indices_zero):
        final.append(min(abs(i-indices_zero[insere]), abs(i-indices_zero[insere-1]), 9))
    else:
        final.append(min(abs(i-indices_zero[-1]), 9))
print(*final)