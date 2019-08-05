# Guess The Number
# Conn

import random

print("************************************")
print("* Guess a number between 1 and 100!*")
print("************************************")

try:
    random_num = random.randrange(1, 101) #Random number from 1 to 100 created
    guess_num = input("Guess the number: ")
    no_of_guesses = 1



    while random_num != int(guess_num): #Before converting guess_num to integer data type, Python was comparing an integer (random_num) to a string (guess_num)
        print("Incorrect answer!")

        if random_num > int(guess_num):
            print("Your number is too low!")
        else:
            print("Your number is too high!")

        guess_num = input("Guess the number: ")
        no_of_guesses += 1

    print("***********************************")
    print("CORRECT ANSWER! Thanks for playing!")
    print("Number of guesses: " + str(no_of_guesses)) #Converting no_of_guesses to string because it is originally an integer
                                                      #Cannot concatenate a string and integer

except ValueError:
    print("Your input is not a number. Exiting program...")


