"""
só checar todas as condições
"""
A, B, C, D = int(input()), int(input()), int(input()), int(input())
if A == (B + C + D) and (B + C) == D and B == C: print("S")
else: print("N")