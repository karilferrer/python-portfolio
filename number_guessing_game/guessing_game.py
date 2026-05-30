import random

# 1. Welcome Message and Rules
print("==================================================")
print("🎯 Welcome to the Number Guessing Game! 🎯")
print("==================================================")
print("Rules:")
print("1. I am thinking of a number between 1 and 100.")
print("2. You need to choose a difficulty level for your chances.")
print("3. I will tell you if your guess is too high or too low.\n")

# 2. Computer randomly selects a number between 1 and 100
secret_number = random.randint(1, 100)

# 3. User selects the difficulty level
print("Select your difficulty level:")
print("- Type 'easy' for 10 chances")
print("- Type 'medium' for 5 chances")
print("- Type 'hard' for 3 chances")

difficulty = input("Enter difficulty: ")
difficulty = difficulty.lower()  # Converts input to lowercase to prevent typos

# Set the number of chances based on difficulty
if difficulty == "easy":
    chances = 10
elif difficulty == "medium":
    chances = 5
elif difficulty == "hard":
    chances = 3
else:
    print("Invalid choice! Defaulting to 'easy' mode (10 chances).")
    chances = 10

print("\nGreat! You have " + str(chances) + " chances to guess the secret number. Let's start!\n")

# Keep track of how many attempts the user has made
attempts = 0
game_won = False

# 4. The Game Loop (runs as long as you have chances left and haven't won)
while attempts < chances:
    attempts = attempts + 1
    
    # Calculate how many chances are remaining
    remaining = chances - attempts
    
    # Get the user's guess
    guess_input = input("Attempt " + str(attempts) + " - Enter your guess: ")
    guess = int(guess_input)  # Convert the text input into a whole number
    
    # 5. Check if the guess is correct, too high, or too low
    if guess == secret_number:
        print("\n🎉 Congratulations! You guessed the correct number!")
        print("It took you " + str(attempts) + " attempt(s) to win!")
        game_won = True
        break  # Exit the loop immediately since the user won
        
    elif guess < secret_number:
        print("❌ Too low! The secret number is greater than your guess.")
        if remaining > 0:
            print("Chances left: " + str(remaining) + "\n")
            
    else:
        print("❌ Too high! The secret number is less than your guess.")
        if remaining > 0:
            print("Chances left: " + str(remaining) + "\n")

# 6. Game Over check (if they ran out of chances and didn't win)
if not game_won:
    print("\n💀 Game Over! You ran out of chances.")
    print("The secret number was: " + str(secret_number) + ". Better luck next time!")