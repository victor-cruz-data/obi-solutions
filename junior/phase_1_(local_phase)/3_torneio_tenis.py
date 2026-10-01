"""
cada partc jogou 6
tres grupos
5, 6 -> 1
3, 4 -> 2
1, 2 -> 3
0 -> fora
"""
resultados = []
for i in range(6):
    resultados.append(input())
vit = resultados.count("V")
if vit in (5, 6): print(1)
elif vit in (3, 4): print(2)
elif vit in (1, 2): print(3)
else: print(-1)