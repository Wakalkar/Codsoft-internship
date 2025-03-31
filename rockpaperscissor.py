import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def display_score(user_score, computer_score):
    """Display the current score."""
    print("\n--- Scoreboard ---")
    print(f"You: {user_score} | Computer: {computer_score}")
    print("------------------\n")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions:")
    print(" - Type 'rock', 'paper', or 'scissors' to make your choice.")
    print(" - Type 'exit' to quit the game.\n")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        display_score(user_score, computer_score)

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Final Score:")
            display_score(user_score, computer_score)
            break

if __name__ == "__main__":
    main()
