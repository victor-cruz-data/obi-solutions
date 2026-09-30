num = input()
convertido = ""
tabela_conversao = {
    "-": "-",
    ("A", "B", "C"): "2",
    ("D", "E", "F"): "3",
    ("G", "H", "I"): "4",
    ("J", "K", "L"): "5",
    ("M", "N", "O"): "6",
    ("P", "Q", "R", "S"): "7",
    ("T", "U", "V"): "8",
    ("W", "X", "Y", "Z"): "9"
}

for caractere in num:
    if caractere in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        convertido += caractere
    else:
        for i in tabela_conversao:
            if caractere in i:
                convertido += tabela_conversao[i]
                break

print(convertido)
    