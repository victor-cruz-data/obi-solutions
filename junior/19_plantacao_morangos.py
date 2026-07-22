"""
formato retangular
o que importa é maior área

"""
H1, L1, H2, L2 = int(input()), int(input()), int(input()), int(input())
if H1*L1 >= H2*L2: print(H1*L1)
else: print(H2*L2)