lista_nomes = ["Caio", "Ana", "Yan", "Carol"]
for i in range(len(lista_nomes)):
    for j in range(i + 1,len(lista_nomes)):
        print(f"{lista_nomes[i]} - {lista_nomes[j]}")