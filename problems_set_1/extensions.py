def troca(n):

    if n.endswith(".gif"):
        print("image/gif")

    elif n.endswith(".jpg"):
        print("image/jpeg")

    elif n.endswith(".jpeg"):
        print("image/jpeg")

    elif n.endswith(".png"):
        print("image/png")

    elif n.endswith(".pdf"):
        print("application/pdf")

    elif n.endswith(".txt"):
        print("text/plain")

    elif n.endswith(".zip"):
         print("application/zip")

    else:
       print("application/octet-stream")

x = input("File name: ")
x = x.strip().lower()

troca(x)