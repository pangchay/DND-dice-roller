import random

rollAgain = "y"

while rollAgain == "y" or rollAgain == "Y":

    D4 = range(1, 4)
    D6 = range(1, 6)
    D8 = range(1, 8)
    D10 = range(1, 10)
    D12 = range(1, 12)
    D20 = range(1, 20)

    Input = input(" please choose from one of the dice. D4, D6, D8, D10, D12, D20: ")

    if Input == "D4" or Input == "d4":
        print(random.choice(D4))
    elif Input == "D6" or Input == "d6":
        print(random.choice(D6))
    elif Input == "D8" or Input == "d8":
        print(random.choice(D8))
    elif Input == "D10" or Input == "d10":
        print(random.choice(D10))
    elif Input == "D12" or Input == "d12":
        print(random.choice(D12))
    elif Input == "D20" or Input == "d20":
        print(random.choice(D20))
        print("Roll again?")

    rollAgain = input("y or n: ")

else:
    print("Goodbye")
