while True:
    try:
        senha = input()
        alp = False
        min = False
        mai = False
        num = False

        if senha.isalnum():
            alp = True

        for letter in senha:
            if letter.isupper():
                mai = True
            if letter.islower():
                min = True
            if letter.isnumeric():
                num = True

        if alp and min and mai and num:
            print("Senha valida.")
        else:
            print("Senha invalida.")

    except EOFError:
        break