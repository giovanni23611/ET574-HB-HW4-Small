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
        # You can customize these game rules as you like!
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


# Example Usage:
if __name__ == "__main__":
    game = DiceGame()
    
    print("--- Playing 3 Rounds of the Dice Game ---")
    for round_num in range(1, 4):
        v1, v2, tot, res = game.play_round()
        print(f"Round {round_num}: Rolled {v1} and {v2} | Total: {tot} | Result: {res}")
