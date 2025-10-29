import random

# Define snakes and ladders
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}

ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69
}

# Player positions
player_pos = {"Player 1": 0, "Player 2": 0}


def roll_dice():
    return random.randint(1, 6)


def move_player(player):
    dice = roll_dice()
    print(f"\n{player} rolled a {dice}")
    pos = player_pos[player] + dice

    if pos > 100:
        print(f"{player} needs {100 - player_pos[player]} to win. Try again next turn.")
        return

    # Check for ladders
    if pos in ladders:
        print(f"🎉 {player} climbed a ladder from {pos} to {ladders[pos]}!")
        pos = ladders[pos]

    # Check for snakes
    elif pos in snakes:
        print(f"🐍 {player} got bitten by a snake from {pos} to {snakes[pos]}!")
        pos = snakes[pos]

    player_pos[player] = pos
    print(f"{player} is now on square {pos}")

    if pos == 100:
        print(f"\n🏆 {player} wins the game!")
        return True
    return False


def play_game():
    print("🎲 Welcome to Snake and Ladder! 🎲")
    print("First to reach 100 wins!\n")

    while True:
        for player in player_pos.keys():
            input(f"{player}, press Enter to roll the dice...")
            if move_player(player):
                return


if __name__ == "__main__":
    play_game()
