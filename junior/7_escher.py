"""
lista + lista_inversa -> todos os elementos somados dao o mesmo valor
N = qnt numeros na sequencia

input
6
7 2 3 9 10 5


lista = 7 2 3 9 10 5
inversa = 5 10 9 3 2 7
soma = 12 12 12 12 12
pega primeiro elemento, conta qnts desse tem na lista soma, deve ser igual a N

"""
N = int(input())
entradas_str = input().split(" ")
entradas_int = []
entradas_int_reversa = []
for i in entradas_str:
    entradas_int.append(int(i))
    entradas_int_reversa.append(int(i))
entradas_int_reversa.reverse()
soma = []
for i in range(N):
    soma.append(entradas_int[i]+entradas_int_reversa[i])
if soma.count(soma[0]) == N: print("S")
else: print("N")