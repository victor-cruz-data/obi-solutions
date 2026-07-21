"""
é só N - qntd_ocorrencias_unicas
"""
N = int(input())
M = int(input())
figs = []
for i in range(M):
    figs.append(int(input()))
figs = list(set(figs))
print(N - len(figs))