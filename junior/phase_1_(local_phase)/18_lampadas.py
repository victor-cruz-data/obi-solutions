"""
2 lampadas (A e B)
2 interruptores (I1, I2)
se aperta I1, A troca de estado
se aperta I2, ambas trocam de estado
ambas começam apagadas

TEMPO MÁXIMO USADO: 0,059 s
MEMÓRIA USADA: 5.23 MB
"""
def inverte(num):
    retorno = 0
    if num == 0:
        retorno = 1
    return retorno

N = int(input())
lamp = [0, 0]
leitura_str = input().split(" ")

for i in leitura_str:
    if i == "1": lamp[0] = inverte(lamp[0])
    else:
        lamp[0] = inverte(lamp[0])
        lamp[1] = inverte(lamp[1])

for i in lamp: print(i)