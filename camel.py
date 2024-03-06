camelCase = input("camelCase: ")
camelCase = camelCase[0].lower() + camelCase[1:]

for i in camelCase:
    if i.isupper():
        camelCase = camelCase.replace(i, f"_{i.lower()}")
print("snake_case:", camelCase)
