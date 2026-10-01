"""

Essa solução foi 51% mais eficiente em termos de tempo de execução.
0,059 s -> 0,029 s

2 lampadas (A e B)
2 interruptores (I1, I2)
se aperta I1, A troca de estado
se aperta I2, ambas trocam de estado
ambas começam apagadas

a percepção é que a ordem das trocas não importa, e duas trocas iguais se anulam
0 pra 1 não precisa de função própria, usa o not

"""
N = int(input())
lamp = [0, 0]
leitura_str = input().split(" ")
qntd_1 = leitura_str.count("1")
qntd_2 = leitura_str.count("2")
if qntd_1 % 2 != 0: lamp[0] = 1
if qntd_2 % 2 != 0:
    lamp[0], lamp[1] = int(not(lamp[0])), 1
for i in lamp: print(i)