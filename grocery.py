itens = []

while True:
    try:
        item = input().upper()
        #append é uma função embutida que joga o elemento para a lista
        itens.append(item)

    except EOFError:
        d = {}
        for ingrediente in itens:
            d[ingrediente] = d.get(ingrediente, 0) + 1

        for ingrediente in sorted(d.keys()):
            quantidade = d[ingrediente]
            print(quantidade, ingrediente)
        break
