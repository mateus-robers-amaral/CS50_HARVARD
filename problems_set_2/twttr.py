# defino o input
name = input("Input: ")
name = name[0:]

# defino a lista de vogais
i = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# loop de lista chegar cada elemento da lista
for v in i:
    # trocar qualquer vogal da lista i por vazio
    name = name.replace(v, "")

print("Output:", name)
