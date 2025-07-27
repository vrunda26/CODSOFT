import random
def generate_computer_move():
    return random.choice(["rock", "paper", "scissors"])
def determine_game_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif (player_move == "rock" and computer_move == "scissors") or  (player_move == "paper" and computer_move == "rock") or (player_move == "scissors" and computer_move == "paper"):
        return "player"
    else:
        return "computer"
def show_round_result(player_move, computer_move, result):
    print(f"\nYou chose: {player_move}")
    print(f"Computer chose: {computer_move}")
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win!")
    else:
        print("Computer wins!")

def run_rock_paper_scissors_game():
    player_score = 0
    computer_score = 0
    print(" Welcome to Rock-Paper-Scissors!")

    while True:
        print("\nChoose one: rock, paper, scissors")
        player_choice = input("Your choice: ").strip().lower()

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.")
            continue
        computer_choice = generate_computer_move()
        result = determine_game_winner(player_choice, computer_choice)
        show_round_result(player_choice, computer_choice, result)
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        print(f"\nScore -> You: {player_score} | Computer: {computer_score}")
        play_more = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_more != "yes":
            print("Thanks for playing!")
            break
run_rock_paper_scissors_game()
