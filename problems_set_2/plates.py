def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha():
        return False

    for x in s:
        if x in [".", " ", "!", "?"]:
            return False

    i = 0
    while i < len(s):

        if not s[i].isalpha():
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    fn = False
    for c in s[1:]:

        if c.isdigit():
            fn = True
        elif not c.isalpha() or fn:
            return False

    return True

main()
