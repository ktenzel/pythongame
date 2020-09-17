from sys import exit

def drop_sword():
    print("You've dropped your sword")
    dead("Without a sword you will surly lose.")

def desert():
    print("You head to a desert.")
    print("The sun scorches you skin.")
    print("You see an oacis.")
    print("What do you do?")
    print("Take a drink or head for th hills")
    choice = input("> ")

    if choice == "take a drink" or "1" in choice:
        drink()
    elif choice == "hills" or "2" in choice:
        hills()
    else:
        drop_sword()


def drink():
    print("The waters renew your energy")
    print("You leave the Oasis")
    print("Head to the hills or ocean.")

    if choice == "hills" in choice:
        hills()
    elif choice == "ocean" in choice:
        ocean()
    else:
        drop_sword()

def start():
    print("It's dangerous to go alone.")
    print("Take this...")
    print("aquired sword.")
    print("What to do now?")
    print("Head to the desert, hills or ocean?")

    choice = input("> ")

    if choice == "desert" in choice:
        desert()
    elif choice == "hills" in choice:
        hills()
    elif choice == "ocean" in choice:
        ocean()
    else:
        drop_sword()

def dead(why):
    print(why, "and so paseth you.")
    exit(0)

start()