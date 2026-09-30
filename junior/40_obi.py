entrada = [int(x) for x in input().split()]
N, P = entrada[0], entrada[1]
qntd_aprovados = 0
for i in range(N):
    pontucacao_candidato = [int(x) for x in input().split()]
    if sum(pontucacao_candidato) >= P: qntd_aprovados += 1
print(qntd_aprovados)