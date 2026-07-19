"""
A B C
A < B -> A cabe dentro de B
A + B < C -> A e B cabem juntas dentro de B

entrada é garantida de ser na ordem crescente
"""
A = int(input())
B = int(input())
C = int(input())

if (A+B) < C: print(1)
elif A < B < C: print(1)
elif A < B or B < C or A < C: print(2)
else: print(3)