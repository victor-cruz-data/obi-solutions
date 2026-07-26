"""
vitoria 3 pontos
empate 1 ponto
se empate nos pontos, maior saldo gols
se empate nos pontos e saldo, fica empate
"""
dados = [int(x) for x in input().split()]
pontos_c = 3*dados[0] + dados[1]
saldo_c = dados[2]
pontos_f = 3*dados[3] + dados[4]
saldo_f = dados[5]
if pontos_c > pontos_f: print("C")
elif pontos_f > pontos_c: print("F")
else:
    if saldo_c > saldo_f: print("C")
    elif saldo_f > saldo_c: print("F")
    else: print("=")