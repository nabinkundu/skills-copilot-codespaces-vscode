import random
import sys

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "player"
    else:
        return "computer"

def main():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Final Scores - You: {player_score}, Computer: {computer_score}")
            sys.exit()

if __name__ == "__main__":
    main()