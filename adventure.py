
print("There are three doors marked with 'A', 'B', and 'C'! Choose a door to begin your adventure.")
door_selection = input("Door Selection: ").upper()


if door_selection != "A" and door_selection != "B" and door_selection != "C":
    print("Invalid entry! Please try again.")
    print("Ending program...")
    exit()

if door_selection == "A":
    print("The door opens and you see darkness...")
    print("A light suddenly turns on and you see two small tables with items on them.")
    print("Upon closer inspection you realize that both of these items are keys.")
    print("One is marked with '1' and another is marked with '2'. Which key are you taking?")
    print()
    key_selection = input("Key Selection: ")


    if key_selection == "1":
        print("You grab Key 1 and walk deeper into the room. You notice a door labeled '1.' You put the key inside the door and it opens...")
        print("You feel a cold breeze as you step outside. You walk on a porch and suddenly the door behind you closes.")
        print("You start hearing footsteps nearby but you don't see anyone.")
        print("Out of nowhere, you feel your body falling and blackness invades your vision...")
        print("Game Over!")
        exit()

    elif key_selection == "2":
        print("You grab Key 2 and walk deep into the room. You notice a door labeled '2'. You put the key inside the door and it opens...")
        print("You walk outside and notice train tracks in the distance. You notice an abandoned mining cart on the track.")
        print("Suddenly, you fight of flight senses kick in because you hear a mob of footsteps rushing towards you from the distance.")
        print("A man yells and he appears to be holding a shotgun. You have two options.")
        print("'1': Wait for the mob. '2': Hop in the mining cart and ride down the track.")
        option = input("Choice: ")

        if option == "1":
            print("The mob finally arrives in your vicinity. The man with the shotgun approaches you.")
            print("He signals for one of his companions to stand next to him. His companio pulls out a bag and hands it to me.")
            print("I grab the bag and say thank you. The men tell me to open it...")
            print("Inside the bag is a ton of GOLD! ")
            print("******* You win! ******")

        elif option1 == "2":
            print("You ride down the train tracks as the men call for your attention. The journey is a long one and you begin to drift to sleep.")
            print("You wake up and you feel your body aching. You are tied to a log by rope. Your vision slow comes back to you. ")
            print("You observe yourself in a camp site full of bandits.")
            print("Oh no...")
            print("Game Over!")
            exit()

elif door_selection == "B":
    print("You open the door and walk inside. Crazy enough, you seem to have walked yourself into a small amusemnet park.")
    print("You notice that there is only one ride. You're curious and no one else is around.")
    print("You decide to sit in one of the seats of the ride expecting nothing...")
    print("Suddenly, your seat is locked down. You attempt to push against the lock but all attempts fail.")
    print("The roller coaster begins to inch towards the sky. Once you reach the top and look down, you realize that the construction of the roller coaster isn't finished...")
    print("Game Over!")

elif door_selection == "C":
    print("You walk inside. You pass out...")
    print("Your eyes open and suddenly you're in an intense boxing match.")
    print("Your opponent seems to be out of breath and struggling. ")
    print("1: Finish Him! 2: Give Him Space to Recover  ")
    decision = input("Choice: ")

    if decision == "1" or decision == "2":
        print("Your head is beating and you're laying in bed. You woke up from an intense dream...")
        print("Game Over!")
        exit()

