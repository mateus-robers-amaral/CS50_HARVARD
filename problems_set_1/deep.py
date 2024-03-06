x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")


if x.strip().lower() == "forty-two":
    print("Yes")

elif x.strip().lower() == "forty two":
   print("Yes")

elif x.strip() < "42" or x.strip() > "42":
    print("No")

else:
    print("Yes")
