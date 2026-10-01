"""
a leitura é sempre

NUM + ESPAÇO + OPERADOR + ESPAÇO + NUM


"""

N = int(input())
num1, operador, num2 = input().split()
resultado = 0
if operador == "*":
    resultado = int(num1) * int(num2)
elif operador == "+":
    resultado = int(num1) + int(num2)
if resultado > N: print("OVERFLOW")
else: print("OK")