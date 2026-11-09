import random

class Die:
    def __init__(self, max_side=6):
        """Initializes a die with a default of 6 sides."""
        self.max_side = max_side

    def roll(self):
        """Returns a random integer from 1 to the number of sides."""
        return random.randint(1, self.max_side)


class DiceGame:
    def __init__(self):
        """Creates two Die objects."""
        self.die1 = Die()
        self.die2 = Die()

    def evaluate_roll(self, total):
        """Determines the outcome based on the total."""
        if total in (7, 11):
            return "Win"
        elif total in (2, 3, 12):
            return "Loss"
        else:
            return "Point (Roll again)"

    def play_round(self):
        """Rolls both dice and returns the two values, total, and result."""
        val1 = self.die1.roll()
        val2 = self.die2.roll()
        total = val1 + val2
        result = self.evaluate_roll(total)
        
        return val1, val2, total, result


def main():
    """Implements a simple console menu to play the dice game."""
    game = DiceGame()
    
    while True:
        print("\n--- Dice Game Menu ---")
        print("1. Play a round")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == '1':
            val1, val2, total, result = game.play_round()
            print(f"\nDice Rolled: {val1} and {val2}")
            print(f"Total: {total}")
            print(f"Result: {result}")
        elif choice == '2':
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
