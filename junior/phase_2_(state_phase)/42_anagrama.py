"""
Há algumas maneiras de resolver...

A primeira coisa que penso é contar a quantidade de cada tipo de caractere. Consigo
fazer com complexidade O(N), dado que eu percorro cada string uma vez, cada uma sendo
complexidade O(N) (e entende-se que a complexidade final é igual à maior complexidade).

Ou posso só percorrer N e acessar as duas listas simultaneamente pelo índice.

Ou posso extrair os elementos únicos e percorrer essa lista. Essa extração será <= N (N caso
todos os caracteres sejam únicos, ou menor se houver caracteres repetidos, sendo que
quanto menor, melhor). Vou tentar esse, extraindo os elementos únicos via set.

Exemplo:

porta coral
p = 1
o = 2
r = 2
t = 1
a = 2
c = 1
l = 1

clar tra
p = 1
o = 2
r = 2
"""
import string
N = int(input())
A, B = input(), input()
unicos = list(set(A))
alfabeto = string.ascii_lowercase + string.ascii_uppercase
valido = True
for caractere in unicos:
    if caractere in alfabeto:
        if A.count(caractere) != B.count(caractere):
            print("N")
            valido = False
            break
if valido: print("S")