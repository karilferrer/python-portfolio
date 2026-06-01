import random

while True:
    answer = input("Roll the dice? (y/n): ").lower()
    if answer == "y":
        die= random.randint(1,6)
        print(f"{die}")
    elif answer == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")