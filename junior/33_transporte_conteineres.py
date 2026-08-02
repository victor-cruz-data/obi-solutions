"""
Todos os conteineres sao iguais
    A = largura conteiner
    B = comprimento conteiner
    C = altura conteiner

Navio
    X = largura navio
    Y = comprimento navio
    Z = altura navio

Necessariamente a comparação é largura com largura
e comprimento com comprimento

Seria só divisao_inteira(X/A) * divisao_inteira(Y/B) * divisao_inteira(Z/C)

Divisao inteira porque é preciso saber quantos conteineres cabem; se X é 7 metros
e A é 2 metros, teríamos 7/2 = 3,5; ou seja, cabem 3 conteineres nessa dimensão.

Divisão inteira nesse caso é o truncamento, que em Python seria via int() ou
via // (divisao inteira)
"""
A, B, C = [int(x) for x in input().split()]
X, Y, Z = [int(x) for x in input().split()]
qntd_conteiner = (X//A) * (Y//B) * (Z//C)
print(qntd_conteiner)

