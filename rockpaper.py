'''
Let's see how long you can go before the computer beats you in a game of Rock, Paper, Scissors!
This program will add 1 to your streak every time you win. If you tie, nothing is added to your streak but you continue to play.
If you lose, game over!
Author: conn301
'''


from random import randint

game_streak = 0 # initializing a game streak
game_over = 0

while game_over == 0:

    choice = input("SELECT | Rock (r), Paper (p), or Scissors (s): ").lower() #
    cpu_choice = randint(1, 3) # Generates random number between between 1 and 3

    if cpu_choice == 1:
        cpu_choice = "r" # Associates number with choice (rock)

    elif cpu_choice == 2:
        cpu_choice = "p" # Associates number with choice (paper)

    if cpu_choice == 3:
        cpu_choice = "s" # Associates number with choice (scissors)

    if choice == "r" and cpu_choice == "r":
            print("You chose Rock! The Computer chose rock!")
            print("Tie Game!")

    elif choice == "r" and cpu_choice == "p":
            print("You chose Rock! The Computer chose paper!")
            print("Computer wins!")
            game_over = 1 # ends game because of loss to computer

    elif choice == "r" and cpu_choice == "s":
            print("You chose Rock! The Computer chose scissors!")
            print("You win!")
            game_streak += 1 # adds 1 win to the game streak

    elif choice == "p" and cpu_choice == "r":
            print("You chose paper! The Computer chose rock!")
            print("You win!")
            game_streak += 1

    elif choice == "p" and cpu_choice == "p":
            print("You chose paper! The Computer chose paper!")
            print("Tie Game!")

    elif choice == "p" and cpu_choice == "s":
            print("You chose paper! The Computer chose scissors!")
            print("Computer wins!")
            game_over = 1

    elif choice == "s" and cpu_choice == "r":
            print("You chose scissors! The Computer chose rock!")
            print("Computer wins!")
            game_over = 1

    elif choice == "s" and cpu_choice == "p":
            print("You chose scissors! The Computer chose paper!")
            print("You win!")
            game_streak += 1

    elif choice == "s" and cpu_choice == "s":
            print("You chose scissors! The Computer chose scissors!")
            print("Tie Game!")
    else:
            print("Invalid entry!") # input not satisfying requirements for the game
            exit()

    print("Game Streak: " + str(game_streak) + "\n") # displaying the current streak of game wins
print("Game Over!")