x = input("Expression: ")
n = x.split()
n1 = float(n[0])
sinal = n[1]
n2 = float(n[2])

try:
    if sinal == "+":
        print(n1 + n2)
    elif sinal == "-":
        print(n1 - n2)
    elif sinal == "*":
        print(n1 * n2)
    elif sinal == "/":
        print(n1 / n2)
except ValueError:
    print("Operação não suportada.")