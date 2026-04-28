cp = 0
while cp < 3:
    print(f"Produto{cp}")
    cp += 1

# while decrescente de 4 até 1
i = 4
while i >= 1:
    print (i)
    i -= 1

# como pular com while

x = 0
while x < 10:
    x += 1
    if x == 3 or cp == 5:
        continue

# como parar o programa
    if x == 7:
        break
    print(f"nota{x}")