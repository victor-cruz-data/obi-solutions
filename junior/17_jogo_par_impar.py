"""
basicamente checar se soma é par
P é quem gritou par (0 alice, 1 bob)
"""
P, D1, D2 = int(input()), int(input()), int(input())
if (D1+D2)%2 == 0: print(P)
else:
    if P == 0: print(1)
    else: print(0)