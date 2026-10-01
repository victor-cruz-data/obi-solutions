"""
caixa = formato tijolo
drone faz uma entrega por vez, entrando pela janela
janelas sempre retangulares e abertas
drone consegue rotacionar caixa

A, B, C = dimensões da caixa em cm
H, L = altura e largura da janela

ordena abc crescente
compara menor com menor, maior com maior
"""
A, B, C, H, L = int(input()), int(input()), int(input()), int(input()), int(input())
caixa, janela = [A, B, C], [H, L]
caixa.sort()
janela.sort()
if caixa[0] <= janela[0] and caixa[1] <= janela[1]: print("S")
else: print("N")