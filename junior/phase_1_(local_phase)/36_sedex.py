"""
Bola
    N = diametro

Caixa
    A = Altura
    L = largura
    P = profundidade

"S" se cabe, "N" se não cabe

A bola cabe na caixa se:
N <= A and N <= L and N <= P

OU

N <= min(A, L, P)

"""
N = int(input())
A, L, P = [int(x) for x in input().split()]
if N <= A and N <= L and N <= P: print("S")
else: print("N")