def use_bridge():
    pass

def take_path():
    pass

def room_description():
    print("------------------------------------------------------")
    print(" You walk into a dimly lit room. As your eyes adjust")
    print(" to the darkness you see a massive cavern in front of")
    print(" you. There is a thin path wrapping around the edge of")
    print(" the room. At the center of the cavern is a chest ")
    print(" placed atop pillar of stone. Not too far away from")
    print(" where you are standing is a rickety bridge between")
    print(" the path you are standing on and the island.")
    print(" What will you do?")
    print()
    input("Press ENTER")
    print()
    print(" (1) Take the bridge to the chest")
    print(" (2) Take the path around the cavern")
    print("------------------------------------------------------")
    print

    while True:
        try:
            user_input = int(input("What will you do? "))

            if user_input == 1:
                result = use_bridge()

                return result

            elif user_input == 2:
                result = take_path()

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

def cavern_main():
    pass