import random
import json

# Global variables
player_gold = 0

def show_intro():
    print("Welcome to The Game of Choices!")
    print("You find yourself in a mysterious room with three doors.")
    print("Your goal is to explore and collect as much gold as you can.")
    print("Be careful; wrong choices can lead to danger!")

def start_game():
    global player_gold
    while True:
        print(f"\nYou currently have {player_gold} gold.")
        print("\nOptions:")
        print("1. Enter Door 1")
        print("2. Enter Door 2")
        print("3. Enter Door 3")
        print("4. Save Game")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            player_gold += enter_door()
        elif choice == '2':
            player_gold += enter_door()
        elif choice == '3':
            player_gold += enter_door()
        elif choice == '4':
            save_game()
        elif choice == '5':
            quit_game()
        else:
            print("Invalid choice. Please try again.")

def enter_door():
    random_choice = random.randint(1, 3)
    
    if random_choice == 1:
        gold_found = random.randint(10, 50)
        print(f"You enter a door and find {gold_found} gold!")
        return gold_found
    elif random_choice == 2:
        print("You enter a door and fall into a pit!")
        gold_lost = random.randint(1, 5)
        print(f"You died and lost {gold_lost} gold...")
        if gold_lost > player_gold:
            gold_lost = player_gold
        return -gold_lost
    elif random_choice == 3:
        print("You enter a door and encounter a friendly merchant.")
        print("The merchant gives you 30 gold as a reward!")
        return 30

def save_game():
    global player_gold
    player_data = {"gold": player_gold}
    with open("saved_game.json", "w") as save_file:
        json.dump(player_data, save_file)
    print(f"Game saved! You currently have {player_gold} gold.")

def load_game():
    global player_gold
    try:
        with open("saved_game.json", "r") as save_file:
            player_data = json.load(save_file)
            player_gold = player_data.get("gold", 0)
        print(f"Game loaded! You currently have {player_gold} gold.")
    except FileNotFoundError:
        print("No saved game found.")

def quit_game():
    print("Thank you for playing The Game of Choices!")
    exit()

if __name__ == "__main__":
    show_intro()
    load_game()  # Attempt to load a saved game

    while True:
        start_game()  # Start the game loop
