"""
é literalmente contar quantas mudanças ocorrem
- considerando o primeiro valor como uma mudança tambem
"""
N = int(input())
sequencia = []
for i in range(N): sequencia.append(int(input()))
atual, qntd_mudancas = sequencia[0], 1
for num in sequencia:
    if num != atual:
        atual = num
        qntd_mudancas += 1
print(qntd_mudancas)