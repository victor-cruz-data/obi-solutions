N = int(input())
acessos = []
for i in range(N): acessos.append(int(input()))
soma = 0
for i in range(len(acessos)):
    soma += acessos[i]
    if soma >= 1000000:
        print(i+1)
        break