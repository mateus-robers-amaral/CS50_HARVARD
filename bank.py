    # defino o input p/ receber a saudação
x = input("Greeting: ")

x = x.lower().strip()

    # crio a condicional se x = hello, ganha $0
if x == "hello" or x.startswith("hello"):
    print("$0")

    # crio a condicional se x começar com h ganha $20
elif x.lower().startswith("h"):
    print("$20")

    # se for qualquer outra coisa, ganha $100
else:
    print("$100")

    # como faço para obter uma resposta simples e não pagar $20?
