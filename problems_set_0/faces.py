def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x
def main():
    y = input("Digite algo: ")
    converter = convert(y)
    print(converter)

if __name__ == "__main__":

    main()