"""
Versão melhorada do meu programa. Apliquei a ideia de unpacking diretamente para o caso de o
número de elementos da lista ser conhecido (como eu sei que a leitura é garantida de ser
exatamente 2 valores, não preciso do intermediário d). Ou seja:

N, M = [int(x) for x in input().split()]

Além disso, o programa anterior comia CPU sem necessidade, pois if i == 0: só ocorria
uma vez, mas era avaliado todas as outras. Se o laço rodasse 10.000 vezes, o if i == 0
seria verdadeiro só na primeira, mas essa verificação seria feita nas outras 9.999 vezes.
Para lidar com isso, eu coloquei o valor inf (infinito) na variável menor_tempo_total. Isso
me permite remover a verificação if i == 0 do laço for, pois o inf é necessariamente
maior que qualquer número finito, o que aumenta muito a eficiência. Ficou assim:

menor_tempo_total = float('inf')

Também otimizei a soma dos valores lido. Antes, eu estava criando uma lista só para poder
calcular a soma, e depois a variável se tornava um número. Em vez disso, descobri por meio
de pesquisas a função map.

Ele funciona por meio da expressão map(funcao, colecao), em que ele aplica a funcao a todos
os elementos da colecao, um por um. Ou seja, em vez de:

total = [int(x) for x in input().split()]
total = sum(total)

Eu posso fazer:

total = sum(map(int,input().split()))

A diferença não é só a economia de uma linha. No primeiro caso, eu estava alocando uma lista
na memória. No segundo caso, isso não foi necessário. O map atua apenas como um iterador
eficiente escrito inteiramente em C. Ou seja, consigo obter a soma sem precisar alocar
uma lista na memória. Pensando em um laço for com milhares de execuções, a diferença pode
ser impactante.

OBS: Se for no rigor, o [int(x) for x in input().split()] cria duas listas (uma do
.split() e a outra convertida). Tecnicamente, ao usar o map, eu impedi a criação
da segunda lista. O efeito é o mesmo, mas só pra deixar claro que o resultado não é
"zero listas", pois uma lista acaba sendo alocada por causa do input().split())

"""
N, M = [int(x) for x in input().split()]
menor_tempo_total = float('inf')
for i in range(N):
    total = sum(map(int,input().split()))
    if total < menor_tempo_total:
        menor_tempo_total = total
        corredor = i + 1
print(corredor)
