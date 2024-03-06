months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        i = input("Date: ")
        f = i.split(" ", 1)

        if f[0].isdigit():
            d, ma = f
            m, a = ma.split(',')
            if m.strip() in months:
                month = months.index(m.strip()) + 1
                print(a.strip(), month, d.strip(), sep="-")
            else:
                raise ValueError

        elif " " in i and "," in i:
            ma, d = f
            m, a = ma.split(',')
            if m.strip() in months:
                month = months.index(m.strip()) + 1
                print(a.strip(), month, d.strip(), sep="-")
            else:
                raise ValueError

        else:
            m, d, a = map(int, i.split("/"))
            if 1 <= m <= 12 and 1 <= d <= 31:
                fm = str(m).zfill(2)
                fd = str(d).zfill(2)
                print(f"{a}-{fm}-{fd}")
            else:
                continue
        break

    except ValueError:
        print("Value Error")
