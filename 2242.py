vogais = 'aeiou'

frase = input()
lista = []

for letter in frase:
    if letter in vogais:
        lista.append(letter)

tam = len(lista)
eng = True

for i in range(tam):
    if lista[i] != lista[tam - i - 1]:
        print("N")
        eng = False
        break

if (eng):
    print("S")