import random

def use_bridge():
    bridge_break = random.randrange(0,1)

    if bridge_break == 0:
        print("------------------------------------------------------")
        print(" You make your way across the rickety roap bridge. When")
        print(" you get to the center pillar you open the chest to")
        print(" a small bag filled with gold coins.")
        print()
        input("Press ENTER")
        print(" After pocketing the bag of gold, you carefully make")
        print(" your way back across the ropa bridge. Once across you")
        print(" Take the path that leads to the next doorway around")
        print(" the chasm.")
        print("------------------------------------------------------")
        print()
        input("Press ENTER")

        return ""
    elif bridge_break == 1:
        print("------------------------------------------------------")
        print(" You start walking across the rope bridge. As you")
        print(" As you approach the middle of the bridge you hear a")
        print(" snapping sound as the ropes of the bridge fail under")
        print(" your weight.")
        print()
        input("Press ENTER")
        print(" You fall to the depths of the chasm. Never to be heard")
        print(" from again.")
        print("------------------------------------------------------")
        print()
        input("Press ENTER")

        return "DEAD"
    else:
        print("Something went wrong with the code.")

def take_path():
    print("------------------------------------------------------")
    print(" Deciding to avoid all danger and risk you turn your")
    print(" back on the potential of treasure and take the safe")
    print(" route around the chasm. Your bag remains light as ever")
    print(" as you forgo the treasure at the center of the chasm")
    print()
    input("Press ENTER")
    print(" Why did you venture into go into this dungeon in the") 
    print(" first place?")
    print("------------------------------------------------------")
    print()
    input("Press ENTER")

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
    results = room_description()

    return results