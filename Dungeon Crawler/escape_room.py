def continue_dungeon():
    print("------------------------------------------------------")
    print(" Your lust for treasure and riches get the better of")
    print(" you! You confidently walk up to the door oppisite you")
    print(" and throw it open and walking blindly into the next")
    print(" room.")
    print("------------------------------------------------------")

    input("Press ENTER")
    print()

    return ""

def use_staircase():
    print("------------------------------------------------------")
    print(" The stresses of the dungeon get the better of you and")
    print(" you elect to leave the dungeon while you still have")
    print(" the chance. Grasping tightly to the treasures you've")
    print(" managed to collect up to this point, you start the")
    print(" long climb to the surface.")
    print("------------------------------------------------------")

    input("Press ENTER")
    print()

    return "EXIT"

def room_description():
    print("------------------------------------------------------")
    print(" You walk into a, small, dimly lit room. Glancing ")
    print(" around the room you see a door at the opposite end of")
    print(" the room (presumably leading further into the dungeon)")
    print(" and a set of stairs leading upwards.")
    print()
    input("Press ENTER")
    print()
    print(" What will you do?")
    print()
    print(" (1) Continue your journey through the dungeon?")
    print(" (2) Take the stairs and exit the dungeon?")
    print("------------------------------------------------------")

    while True:
        try:
            user_input = int(input("What will you do? "))

            if user_input == 1:
                result = continue_dungeon()

                return result

            elif user_input == 2:
                result = use_staircase()

                return result

            else:
                print("Please select a valid option.")
                input("Press ENTER")
                print()
            
        except:
            print("Please select a valid option")
            print()
            input("Press ENTER")
            print()

def escape_room_main():
    results = room_description()

    return results