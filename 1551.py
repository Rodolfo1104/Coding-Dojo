N = int(input())
letras = 'abcdefghijklmnopqrstuvwxyz'
for i in range(N):
    frase = input().lower()
    count = 0
    for letra in letras:
        if letra in frase:
            count += 1
    

    if (count  == 26):
        print("frase completa")
    elif(count >= 13):
        print("frase quase completa")
    else:
        print("frase mal elaborada")
    
