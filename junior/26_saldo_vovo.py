dados = [int(x) for x in input().split()]
N, S = dados[0], dados[1]
movimentacoes = []
for i in range(N): movimentacoes.append(int(input()))
saldo, menor_saldo = S, S
for i in movimentacoes:
    saldo += i
    if saldo < menor_saldo: menor_saldo = saldo
print(menor_saldo)