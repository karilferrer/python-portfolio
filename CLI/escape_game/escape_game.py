import random

def start_game():
    print("=========================================")
    print("             🤠 ESCAPE GAME 🤠             ")
    print("=========================================")
    print("You are trapped in a pitch-black 3x3 mine.")
    print("Find the hidden EXIT before your flashlight battery dies!")
    print("Controls: W (up), S (down), A (left), D (right)\n")

    # 1. Setup coordinates (Grid size is 0 to 2 for both X and Y)
    # 0,0 is top-left, 2,2 is bottom-right
    player_x = 0
    player_y = 0
    
    # 2. Randomly place the exit somewhere else on the grid
    exit_x = random.randint(0, 2)
    exit_y = random.randint(0, 2)
    
    # Make sure the exit isn't exactly where the player starts
    while exit_x == player_x and exit_y == player_y:
        exit_x = random.randint(0, 2)
        exit_y = random.randint(0, 2)

    # 3. Game constraints
    battery = 6  # The player has 6 moves to find the exit

    # 4. Main Game Loop
    while True:
        print(f"📍 Current Position: (X: {player_x}, Y: {player_y})")
        print(f"🔋 Flashlight Battery: {battery} moves left")
        
        # Win condition check
        if player_x == exit_x and player_y == exit_y:
            print("\n🎉 SUCCESS! You found the ladder and escaped the mine alive! 🎉")
            break
            
        # Lose condition check
        if battery == 0:
            print("\n💀 CLICK... Your flashlight died. You are trapped in the dark forever. 💀")
            print(f"The exit was at (X: {exit_x}, Y: {exit_y})")
            break

        move = input("Enter direction (W/A/S/D) or 'quit': ").lower().strip()

        if move == "quit":
            print("\nYou gave up and abandoned the mine.")
            break

        # 5. Handle Movement & Boundary Limits
        # Moving UP decreases Y, Moving DOWN increases Y
        # Moving LEFT decreases X, Moving RIGHT increases X
        if move == "w":
            if player_y > 0:
                player_y -= 1
                battery -= 1
            else:
                print("💥 OUCH! You walked straight into a solid rock wall!")
                
        elif move == "s":
            if player_y < 2:
                player_y += 1
                battery -= 1
            else:
                print("💥 OUCH! You walked straight into a solid rock wall!")
                
        elif move == "a":
            if player_x > 0:
                player_x -= 1
                battery -= 1
            else:
                print("💥 OUCH! You walked straight into a solid rock wall!")
                
        elif move == "d":
            if player_x < 2:
                player_x += 1
                battery -= 1
            else:
                print("💥 OUCH! You walked straight into a solid rock wall!")
                
        else:
            print("✖ Invalid command! Use W, A, S, or D to move.")
            
        print("-" * 40)

if __name__ == "__main__":
    start_game()