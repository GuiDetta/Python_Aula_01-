lista_frutas = ["Morango", "Abacaxi", "Maracujá"]

#lista_frutas[0] = "Morango"
#lista_frutas[1] = "Abacaxi"
#lista_frutas[2] = "Maracujá"
print(lista_frutas[1])

lista_frutas.append("Banana")
print(lista_frutas[3])

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for frutas in lista_frutas:
    print(frutas)