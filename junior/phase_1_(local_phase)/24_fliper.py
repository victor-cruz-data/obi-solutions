entrada = [int(x) for x in input().split()]
P, R = entrada[0], entrada[1]
if P == 0: print("C")
else:
    if R == 1: print("A")
    else: print("B")