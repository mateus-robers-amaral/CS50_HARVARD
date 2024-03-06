# defino os valores aceitos
aceitos = [5, 10, 25]

# defino o valor que falta
falta = 50

# defino o loop para mostrar a quantia que falta até ser igual a zero
while falta > 0:

    # printo o quanto falta
    print("Amount Due:", falta)

    # defino o input para dizer quanto vai ser depositado
    inserir = int(input("Insert Coin: "))

    # se o valor inserido pertencer aos aceitos
    if inserir in aceitos:
        # atualizo o valor que falta
        falta -= inserir

    if falta <= 0:


        print("Change Owed:", abs(falta))
        break
