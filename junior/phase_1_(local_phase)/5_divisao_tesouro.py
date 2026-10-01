"""
moedas identicas
cada marinheiro = x
capitao = 2x
a divisão é garantida de ser perfeita
A = total moedas
N = total marinheiros

input
14
5

marinheiros = x cada
capitao = 2x
14 = marinheiros + capitao
14 = 5x + 2x
14 = 7x
2 = x

capitao = 2x = 4

"""
A = int(input())
N = int(input())
print(int(A/(N+2)*2))