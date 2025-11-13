#comparativo3GPT
nome = input(("Digite o nome do conta: "))
senha = int(input("Digite sua senha: "))

if nome=="admin":
    print("O nome está correto")
    if senha==1234:
        print("A senha está correta")
        print("Login realizado com sucesso!")
    else:
        print("A senha está incorreta.")
else:
    print("o nome está inexistente.")

