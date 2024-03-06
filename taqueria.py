cardapio = {

    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
    }

conta = 0
while True:
    try:
        item = input("Item: ")
        if item.lower() in cardapio:
            conta += cardapio[item.lower()]
            print("${:.2f}".format(conta), sep = "")
            continue

    except EOFError:
        break
