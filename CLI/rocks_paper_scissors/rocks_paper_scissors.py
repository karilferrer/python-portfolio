import random

choices = ("r", "p", "s")
user_pick = input("Rock, paper, or scissors? (r,p,s) ").lower()

if user_pick not in choices:
    print("Invalid Choice! Please run the program again and choose r, p, or s.")
else:
    computer_pick = random.choice(choices)
    print(f'You chose: {user_pick}')
    print(f'Computer chose: {computer_pick}')

    if user_pick == computer_pick:
        print("It's a tie!")
    elif (user_pick == "r" and computer_pick == "s") or \
         (user_pick == "p" and computer_pick == "r") or \
         (user_pick == "s" and computer_pick == "p"):
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖")