"""
só comparar num_papel_diretora com num_papel_embraer * num_aluno

Na prática, abstraindo, só comparar a quantidade unitária  
"""
C, P, F = [int(x) for x in input().split()]
if P >= C*F: print("S")
else: print("N")
