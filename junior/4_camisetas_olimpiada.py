"""
pequeno e medio
total_camisa >= total_aluno (garantido)
1 = pequeno
2 = médio
P = num pequeno
M = num medio
"""
N = int(input())
tamanhos_str = input().split(" ")
P = int(input())
M = int(input())
if tamanhos_str.count("1") >= P and tamanhos_str.count("2") >= M: print("S")
else: print("N")