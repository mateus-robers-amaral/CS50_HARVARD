def troca(n):

    n1 = n.replace(".", "/")

    # "image..." deve aparecer na tela ao invés do input
    if n.endswith(".gif") or n.endswith(".jpg") or n.endswith(".jpeg") or n.endswith(".png"):
        return n1.replace(n, "image")

    # "aplication..." deve aparecer na tela ao invés do input
    elif n.endswith(".pdf") or n.endswith(".txt") or n.endswith(".zip"):
        return n1

    else:
       return "application/octet-stream"

x = input("File name: ")
x = x.strip().lower()
r = troca(x)
print(r)

troca(x)
