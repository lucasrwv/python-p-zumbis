#programa login
while True:
    usu = input("digite um nome de usuário ")
    senha = input("digite uma senha ")
    if usu != senha:
        break
    else:
        print("Erro o nome de usuário e a senha sao iguais isso nao é seguro")
