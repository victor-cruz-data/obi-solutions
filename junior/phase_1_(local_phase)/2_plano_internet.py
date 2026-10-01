"""
X megabytes
se nao usa X, X-usado é adicionado
Nunca usa mais de X


Se X=200

Atual = 0
Mes 1 -> +200
Atual = 200
Gastou 150
Atual = 200 - 150 = 50

Mes 2 -> +200
Atual = 50 + 200 = 250
Gastou 220
Atual = 250 - 220 = 30

Mes 3 -> +200
Atual = 230
"""
X = int(input())
N = int(input())
uso_mes = []
for i in range(N):
    uso_mes.append(int(input()))
print((len(uso_mes)+1)*X - sum(uso_mes))
"""
Entrada
100
2
50
120

->
+100
-50
+100
-120
+100
= 130

"""