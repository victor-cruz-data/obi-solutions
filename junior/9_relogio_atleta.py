"""
coracao_atual
oxigenio
coracao_repouso

se coracao_atual > 3*coracao_repouso ou oxigenio < 95: diminui
senao se coracao_atual < 2*coracao_repouso e oxigenio > 97: aumentar
senao manter

"""
coracao_repouso = int(input())
coracao_atual = int(input())
oxigenio = int(input())

if coracao_atual > 3*coracao_repouso or oxigenio < 95: print("diminuir")
elif coracao_atual < 2*coracao_repouso and oxigenio > 97: print("aumentar")
else: print("manter")