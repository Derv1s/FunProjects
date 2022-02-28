# Rock-Paper-Scissors Game
import random as rd

player_score = 0
computer_score = 0
round_number = 0

while player_score < 3 and computer_score < 3:

    round_number += 1
    print("-"*30)
    print(f"{round_number}. Round!")
    
    options = ["Rock", "Paper", "Scissors"]
    print(options)

    computer = rd.choice(options)
    player = input("Your choice: ").lower().capitalize()

    if not player in options:
        print("!"*30)
        print("You missed a letter or did something wrong!")
        print("Please just enter one of the options 'Rock', 'Paper', 'Scissors'.")
        print("!"*30)
    
    print(f"Computer: {computer}")

    if player == computer:
        print(f"Draw!\nPlayer: {player_score}\nComputer: {computer_score}")
        
    elif player == "Paper":
        if computer == "Scissors":
            computer_score += 1
            print(f"You Lose!\nPlayer: {player_score}\nComputer: {computer_score}")
        else:
            player_score += 1
            print(f"You Win!\nPlayer: {player_score}\nComputer: {computer_score}")
        
    elif player == "Scissors":
        if computer == "Paper":
            player_score += 1
            print(f"You win!\nPlayer: {player_score}\nComputer: {computer_score}")
        else:
            computer_score += 1
            print(f"You Lose!\nPlayer: {player_score}\nComputer: {computer_score}")

    elif player == "Rock":
        if computer == "Scissors":
            player_score += 1
            print(f"You win!\nPlayer: {player_score}\nComputer: {computer_score}")
        else:
            computer_score += 1
            print(f"You Lose!\nPlayer: {player_score}\nComputer: {computer_score}")