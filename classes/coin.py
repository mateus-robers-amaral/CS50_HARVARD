import random
# coin = random.choice(["cara", "coroa"])
# print(coin)

# number = random.randint(1, 10)
# print(number)

baralho = ["1","2","3","4","5","6","7","8","9","10","valete","rei","dama","joker"]
random.shuffle(baralho)
for i in baralho:
    print(i)