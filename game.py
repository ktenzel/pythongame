from sys import exit
sword = True

def drop_sword():
    sword = False
    print("You've dropped your sword")
    field()

def start():
    print("It's dangerous to go alone.")
    print("Take this...")
    print("aquired sword.")
    print("What to do now?")
    print("Head to the desert, hills or ocean?")

    choice = input("> ")

    if choice == "desert" or "1":
        desert()
    elif choice == "hills" or "2":
        hills()
    elif choice == "ocean" or "3":
        ocean()
    else:
        drop_sword()

start()