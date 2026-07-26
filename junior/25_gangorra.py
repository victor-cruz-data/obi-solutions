"""
- não é simétrica
"""
dados = [int(x) for x in input().split()]
M1, M2 = dados[0]*dados[1], dados[2]*dados[3]
if M1 == M2: print(0)
elif M1 > M2: print(-1)
else: print(1)