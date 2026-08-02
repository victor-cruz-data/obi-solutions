"""
Se x latas > y copos, quebrou y copos
"""
N = int(input())
qntd_copos_quebrados = 0
for i in range(N):
    L, C = [int(x) for x in input().split()]
    if L > C: qntd_copos_quebrados += C
print(qntd_copos_quebrados)