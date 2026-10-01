"""
todos os alunos e monitores vão usar
capacidade_cabine = 50 (alunos + monitores)
"""
A = int(input())
M = int(input())
if (A+M) <= 50: print("S")
else: print("N")