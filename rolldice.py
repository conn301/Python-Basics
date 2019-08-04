#Dice Rolling Simulator
#Conn
import random
print("***************************************************************************")
print("Today, we are going to roll some dice!")
print("To end the program, please enter any value that differs from 'y' and 'Y'.")
print("***************************************************************************")
user_input = "y"

while user_input == "y" or user_input == "Y":
    die = random.randrange(1,7)
    print(die)
    user_input = input("Would you like to roll again? (Enter 'y' or 'Y' to continue): ")

print("Thanks for playing!")