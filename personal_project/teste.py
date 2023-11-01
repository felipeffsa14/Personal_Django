palavras = ['@', '$', '%', '!', '#', '&', '*']
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


username = 'feli4p$7'


for palavra in palavras:
    if palavra in username:
        print(palavra)


for numero in numeros:
    if str(numero) in username:
        print(numero)

