import random


def play():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Type 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit.\n")

    user_score, computer_score, ties = 0, 0, 0

    while True:
        user = input("Enter your choice (r, p, s, or q to quit): ").lower()

        if user == 'q':
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
            break

        if user not in ['r', 'p', 's']:
            print("Invalid input! Please enter 'r', 'p', or 's'.")
            continue

        computer = random.choice(['r', 'p', 's'])

        choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        print(f"\nYou chose {choices[user]}, Computer chose {choices[computer]}.")

        if user == computer:
            print("It's a tie! 🤝")
            ties += 1
        elif is_win(user, computer):
            print("You won! 🎉")
            user_score += 1
        else:
            print("You lost! 😔")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer | Ties: {ties}\n")

def is_win(player, opponent):
    """Returns True if the player wins, otherwise False"""
    win_conditions = {
        'r': 's',
        's': 'p',
        'p': 'r'
    }
    return win_conditions[player] == opponent


print(play())









# Welcome to Rock, Paper, Scissors!
# Type 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit.

# Enter your choice (r, p, s, or q to quit): r

# You chose Rock, Computer chose Rock.
# It's a tie! 🤝
# Score: You 0 - 0 Computer | Ties: 1

# Enter your choice (r, p, s, or q to quit): s

# You chose Scissors, Computer chose Paper.
# You won! 🎉
# Score: You 1 - 0 Computer | Ties: 1

# Enter your choice (r, p, s, or q to quit): s

# You chose Scissors, Computer chose Rock.
# You lost! 😔
# Score: You 1 - 1 Computer | Ties: 1

# Enter your choice (r, p, s, or q to quit): s

# You chose Scissors, Computer chose Paper.
# You won! 🎉
# Score: You 2 - 1 Computer | Ties: 1

# Enter your choice (r, p, s, or q to quit): s

# You chose Scissors, Computer chose Rock.
# You lost! 😔
# Score: You 2 - 2 Computer | Ties: 1

# Enter your choice (r, p, s, or q to quit): 
# Invalid input! Please enter 'r', 'p', or 's'.
# Enter your choice (r, p, s, or q to quit): s

# You chose Scissors, Computer chose Paper.
# You won! 🎉
# Score: You 3 - 2 Computer | Ties: 1

# Enter your choice (r, p, s, or q to quit): s

# You chose Scissors, Computer chose Rock.
# You lost! 😔
# Score: You 3 - 3 Computer | Ties: 1

# Enter your choice (r, p, s, or q to quit): 
# Invalid input! Please enter 'r', 'p', or 's'.
# Enter your choice (r, p, s, or q to quit): 
# Enter your choice (r, p, s, or q to quit): 
# Invalid input! Please enter 'r', 'p', or 's'.
# Enter your choice (r, p, s, or q to quit): 
# Invalid input! Please enter 'r', 'p', or 's'.
# Invalid input! Please enter 'r', 'p', or 's'.
# Enter your choice (r, p, s, or q to quit): s

# You chose Scissors, Computer chose Scissors.
# It's a tie! 🤝