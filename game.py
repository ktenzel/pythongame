from sys import exit

def gold_room():
    print("This room is full of gold.  How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def desert():
    print("There is a bear here.\nThe bear has a bundh of honey.\nThe fat bear is in fornt of another door. \nHow are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("Bear has moved from the door.\nYou can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def hills():
    print("Hills Here you see the great evil Cthulhu.")
    print("He, it, whatever startes at you and you go insane")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        cthulhu_room()

def ocean():
    print("A vast ocean surounds you")
    print("Build a boat or swim")

    choice = input("> ")

    if "boat" in choice:
        boat()
    elif "swim" in choice:
        dead("the gret monsters of the deep find you.")
    else:
        dead("You have lost your way")

def boat():
    print("YOU sail for many days")
    print("You find water ans shelter on an Island")
    print("Search of food on the beach or in land")
    
    choice = input(">")

    if choice == "land":
        jungle()
    elif choice == "beach":
        beach()
    else:
        deadt("you have lost your sword")
        
def jungle():
    print("You enter a thick Jungle")
    print("Should you swing from the trees")
    print("Or stick to the ground")
    if choice == "trees":
        print("you swing from the trees and makeit to the hills")
        hills()
    elif choice == "ground":
        beach("A large snake lowers from the trees and bites you.")
    else:
        deadt("you have lost your sword")

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("It's dangerous to go alone, take this")
    print("aquire swor")
    print("leave the cave and go to the hills, ocean desert")

    choice = input(">")

    if choice == "desert":
        desert()
    elif choice == "hills":
        hills()
    elif choice == "ocean":
        ocean()
    else:
        deadt("you have lost your sword")

start()