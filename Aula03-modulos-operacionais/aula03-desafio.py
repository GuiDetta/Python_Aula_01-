idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Você não pode votar")

elif idade < 18:
    print("Seu voto é opcional")

elif idade < 70:
    print("Seu voto é obrigatorio")

else:
    print("Seu voto é opcional")

