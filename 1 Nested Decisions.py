# Task 1 

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")

    if action == "climb a tree":
        print("You found a bird's nest!")

    elif action == "cross a river":
        print("You found a boat!")

    else:
        pass

elif place == "cave":
    print("You find a hidden treasure!")

# Task 2

    cave_choice1 = input("Would you like to light a torch or proceed in the dark?")
    if cave_choice1 == "light a torch":
        print("That was a smart choice.  Now you can see the way ahead.")

    elif cave_choice1 == "proceed in the dark":
        print("That is a terrible decision.  You got lost and wandered around underground for several days before dying of malnutrition.  The end.")

    else:
        pass

# Task 3
# see above for all other pass statements related to task 3

else:
    pass
