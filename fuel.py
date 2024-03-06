while True:
    try:
        f = str(input("Fraction: "))

        x, y = map(int, f.split("/"))

        f = x/y * 100
        f = round(f)

        if f <= 1:
            print("E")
            break
        elif f == 99 or f == 100:
            print("F")
            break
        elif f > 100:
            continue
        else:
            f = int(f)
            print(f"{f}%")
            break

    except ValueError:
        print("Valor digitado não é valido")
        continue
    except ZeroDivisionError:
        print("Divisão por 0 não é possível")
        continue
