import random

rollAgain = "Y"

while rollAgain == "Y" or "y":

    D4 = range(1, 4)
    D6 = range(1, 6)
    D8 = range(1, 8)
    D10 = range(1, 10)
    D12 = range(1, 12)
    D20 = range(1, 20)

    Input = input(" please choose from one of the dice. D4, D6, D8, D10, D12, D20: ")

    if Input == "D4" or "d4":
        print(random.randint(1, 4))

    elif Input == "D6" or "d6":
        print(random.choice(D6))

    elif Input == "D8" or "d8":
        print(random.choice(D8))

    elif Input == "D10" or "d10":
        print(random.choice(D10))

    elif Input == "D12" or "d12":
        print(random.randrange(1, 12))

    elif Input == "D20" or "d20":
        print(random.randint(1, 20))

    print("Roll again?")
    rollAgain = input("y or n: ")

else:
    print("Goodbye")