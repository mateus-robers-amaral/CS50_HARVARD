def main():

    t = input("What time is it? ")
    con = convert(t)

    if 7.0 <= con <= 8.0:
        print("breakfast time")
    elif 12.0 <= con <= 13.0 :
        print("lunch time")
    elif 18.0 <= con <= 19.0 :
        print("dinner time")

def convert(time):

    #map(int()) define todos os valores da função como números inteiros
    #split(":") divide os valores entre antes do : e depois do :
    h, m = map(int, time.split(":"))

    time = h + m / 60.0

    return time

if __name__ == "__main__":
    main()