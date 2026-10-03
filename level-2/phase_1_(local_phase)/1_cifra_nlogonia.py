"""
cada consoante é substituida por tres letras

-> pela propria consoante (repete)
-> vogal mais perto da consoante no alfabeto (se mesma distancia,
prioridade para a vogal que vem primeiro na ordem alfabetica)
-> consoante seguinte de acordo com o alfabeto

é garantido que a entrada sao letras minusculas e sem acento
"""
palavra = input()
cifrada = ""
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
vogais = ["a", "e", "i", "o", "u"]

for letra in palavra:
    # adiciona a própria letra, seja vogal ou consoante
    cifrada += letra
    if letra not in vogais:
        # encontra a vogal mais perto
        menor_distancia = 9999
        posicao_consoante_alfabeto = alfabeto.index(letra)
        vogal_mais_perto = ""
        for vogal in vogais:
            distancia = abs(alfabeto.index(vogal)-posicao_consoante_alfabeto)
            if distancia < menor_distancia:
                vogal_mais_perto = vogal
                menor_distancia = distancia
        cifrada += vogal_mais_perto
        # encontra e adiciona a consoante seguinte
        letra_seguinte = ""
        if posicao_consoante_alfabeto == 23:
            letra_seguinte = "z"
            cifrada += letra_seguinte
        else:
            for i in range(posicao_consoante_alfabeto+1, 24):
                letra_seguinte = alfabeto[i]
                if letra_seguinte not in vogais:
                    cifrada += letra_seguinte
                    break
print(cifrada)