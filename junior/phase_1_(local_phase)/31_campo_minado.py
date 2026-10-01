"""
5
0 1 1 0 1

percorrendo
i=0
esquerda nao existe, base 0, direita 1 (add 1): add 1
i=1
esquerdo 0, base 1 (add 1), direita 1 (add 1): add 2
"""
N = int(input())
campo = []
final = []
for i in range(N): campo.append(int(input()))
for i in range(len(campo)):
    if len(campo) == 1:
        bomba = campo[i]
    elif i == 0:
        bomba = campo[i] + campo[i+1]
    elif i == len(campo)-1:
        bomba = campo[i-1] + campo[i]
    else:
        bomba = campo[i-1] + campo[i] + campo[i+1]
    final.append(bomba)
for i in final:
    print(i)
