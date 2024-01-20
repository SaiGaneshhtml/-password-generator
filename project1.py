import random

exit_game = False
user_points = 0
computer_points = 0

while not exit_game:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors, or exit: ").lower()
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        print("You won a total score of " + str(user_points) + " and the computer total score is " + str(computer_points))
        exit_game = True

    elif user_input in ["rock", "paper", "scissors"]:
        if user_input == "rock":
            if computer_input == "rock":
                print("Your input is rock\ncomputer input is rock\nIt's a tie!")
            elif computer_input == "paper":
                print("Your input is rock\ncomputer input is paper\nComputer wins!")
                computer_points += 1
            elif computer_input == "scissors":
                print("Your input is rock\ncomputer input is scissors\nYou win!")
                user_points += 1

        elif user_input == "paper":
            if computer_input == "rock":
                print("Your input is paper\ncomputer input is rock\nYou win!")
                user_points += 1
            elif computer_input == "paper":
                print("Your input is paper\ncomputer input is paper\nIt's a tie!")
            elif computer_input == "scissors":
                print("Your input is paper\ncomputer input is scissors\nComputer wins!")
                computer_points += 1

        elif user_input == "scissors":
            if computer_input == "rock":
                print("Your input is scissors\ncomputer input is rock\nComputer wins!")
                computer_points += 1
            elif computer_input == "paper":
                print("Your input is scissors\ncomputer input is paper\nYou win!")
                user_points += 1
            elif computer_input == "scissors":
                print("Your input is scissors\ncomputer input is scissors\nIt's a tie!")

    else:
        print("Invalid Input")

