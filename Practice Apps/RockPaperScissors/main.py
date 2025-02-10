from random import choice


def display_game_help():
    print("Rock - Paper - Scissors game instructions")
    print("1. rock beats scissors")
    print("2. scissors beats paper")
    print("3. paper beats rock")
    print("")
    print("how many rounds would you like to play?")

def get_game_rounds():
    rounds = input("Rounds: ")
    return int(rounds)

def get_player_choice():
    player_choice = input("Enter rock, paper or scissors: ")
    return player_choice

def get_computer_choice():
    computer_choice = choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")
    return computer_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == 'rock' and computer_choice == 'scissors':
        print('You win !')
        return 'player'
    elif player_choice == 'rock' and computer_choice == 'paper':
        print('Computer wins !')
        return 'computer'
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('You win !')
        return 'player'
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print('Computer wins !')
        return 'computer'
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print('Computer wins !')
        return 'computer'
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('You win !')
        return 'player'
    elif player_choice == computer_choice:
        print('Tie')

def display_winner(player_score, computer_score):
    if player_score > computer_score:
        print("You won !!!")
    elif computer_score > player_score:
        print("Computer won !!!")
    elif player_score == computer_score:
        print("Game is tie !")

def main():
    player_score = 0
    computer_score = 0
    display_game_help()
    rounds = get_game_rounds()
    for idx in range(rounds):
        print(f"************** Round: {idx+1} ****************")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        if winner == 'player':
            player_score += 1
        elif winner == 'computer':
            computer_score += 1
    print(f"************** ALL ROUNDS ({rounds}) COMPLETED ****************")
    print(f"Your score: {player_score} | Computer score: {computer_score}")
    display_winner(player_score, computer_score)


main()