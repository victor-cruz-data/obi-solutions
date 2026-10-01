"""
Minha primeira solução foi:
N = int(input())
todos = [int(x) for x in input().split()]
M = int(input())
sairam = [int(x) for x in input().split()]

for i in sairam: todos.remove(i)
print(*todos)

Porém, ela estourou o tempo máximo de execução em alguns casos. Busquei entender,
e foi porque o laço for tem complexidade O(M x N). O .remove é de ordem N (pois
percorre toda a lista para encontrar o elemento), e faz cada vez que é solicitado (M vezes).

De maneira mais detalhada, o "x in lista" e o "lista.remove()" fazem uma busca linear sequencial.
Isso significa que, no pior caso, precisarão testar da posição de índice 0 até índice N-1. Portanto,
no máximo, N passagens. Complexidade O(N).

Ao fazer "for i in sairam: todos.remove(i)", a busca ("i in sairam") tem complexidade O(M), e para
cada caso encontrado, a remoção ("todos.remove(i)") tem complexidade O(N). Como N está aninhado em M,
a complexidade é O(M x N). Como  1 ≤ N ≤ 50000 e 1 ≤ M ≤ 50000, o pior cenário exige
2.500.000.000 (2 bilhões 500 milhões) verificações até chegar no resultado final.


--------------

Na minha solução abaixo, a que passou no teste, eu utilizei um set.

Como o set é implementado por meio de uma tabela hash (hash table), as buscas "x in conjunto" e
"x not in conjunto" têm complexidade média de O(1), ou seja, um tempo constante, independentemente
de quantos milhares de itens existam no conjunto.

Ao fazer "sairam = {int(x) for x in input().split()}", inserir M elementos em um set
custa O(M).

Em
for i in todos:
    if i not in sairam:
        final.append(i)

"for i in todos" é executado N vezes O(N). Dentro dele, tem-se "if i not in sairam"
(busca em hash -> O(1)) e "final.append(i)" (inserção no final do array -> O(1))

Como as fases do código estão separadas (e não aninhadas), a complexidade final
é a soma de cada parte.

Construção do set: O(M)
Laço de filtragem: O(N)
Total (por serem sequenciais e não aninhados): O(M) + O(N) = O(M + N)

Como  1 ≤ N ≤ 50000 e 1 ≤ M ≤ 50000, no pior cenário, ocorrerão 100.000 (100 mil)
verificações. Ou seja, essa solução é 25.000 (25 mil) vezes mais eficiente que a anterior
(em termos de tempo de execução).

"""
N = int(input())
todos = [int(x) for x in input().split()]
M = int(input())
sairam = {int(x) for x in input().split()}
final = []
for i in todos:
    if i not in sairam:
        final.append(i)
print(*final)