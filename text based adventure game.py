import time

class Player:
    def __init__(self):
        self.inventory = []
        self.progress = 0

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def update_progress(self, value):
        self.progress += value

def intro():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a adventure land...")
    time.sleep(1)
    print("Your journey starts now!\n")

def make_choice(options):
    print("Choose your action:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def game_over():
    print("Game ended. Thanks for playing!")

def ending_one():
    print("Congratulations! You have reached Ending 1.")

def ending_two():
    print("Congratulations! You have reached Ending 2.")

def main():
    intro()

    player = Player()

    print("You come across a fork in the road.")
    choice = make_choice(["Take the left path", "Take the right path"])

    if choice == 1:
        print("You find a magic sword!")
        player.add_to_inventory("invisble knife")
        player.update_progress(10)
    else:
        print("You encounter a friendly wizard.")
        player.update_progress(5)

    print(f"Your progress: {player.progress}")
    print(f"Your inventory: {player.inventory}")

    print("\nYou continue your journey...")

    print("You arrive at a adventure cave.")
    choice = make_choice(["Enter the cave", "Ignore the cave"])

    if choice == 1:
        print("Inside the cave, you find a treasure chest!")
        player.add_to_inventory("Treasure Chest")
        player.update_progress(15)
    else:
        print("You decide to continue your journey.")

    print(f"Your progress: {player.progress}")
    print(f"Your inventory: {player.inventory}")

    print("\nYou reach the end of your adventure.")
    if player.progress >= 20:
        ending_one()
    else:
        ending_two()

    game_over()

if __name__ == "__main__":
    main()
