import random


def open_chest_1():
    print("------------------------------------------------------")
    print(" You walk up to the chest and insert the key. As soon")
    print(" as the key is turned long gangly arms sprout out the")
    print(" side of the chest. Quicker than you can act large bony")
    print(" hands wrap around your torso. The lid of the chest ")
    print(" slowly opens revealing yellow sharp teeth lining the")
    print(" rim and a sickly purple tongue reaching towards you.")
    print()

    input("Press ENTER")
    print()

    print()
    print(" You were killed by a mimmic. You lost everythin you")
    print(" collected up to this point, along with your life")
    print("------------------------------------------------------")

    print()
    input("Press ENTER")
    print()

    return "DEAD"

def open_chest_2():
    print("------------------------------------------------------")
    print(" You insert the key and open the chest. Inside is a")
    print(" item covered in grime. You pick it up and place it in")
    print(" your bag (It may be worth something once you leave).")

    input("Press ENTER")
    print()

    print(" Unfortunately, the key appears to be stuck in the ")
    print(" chest. You leave the room of chests and head out to")
    print(" the next room")
    print("------------------------------------------------------")

    input("Press ENTER")
    print()

    return ""

def open_chest_3():
    print("------------------------------------------------------")
    print(" You walk up to the chest and insert the key. As you")
    print(" turn the key the handle snapps off. You were unable")
    print(" to open the chest and claim the treasure inside.")

    input("Press ENTER")
    print()

    print(" You end up leave the room empty handed.")
    print("------------------------------------------------------")

    input("Press ENTER")
    print()

    return ""

def going_cakeless():
    print("------------------------------------------------------")
    print(" You decide to forgo trying to open any of the chests,")
    print(" even though it goes against the reasons you had for")
    print(" entering the dungeon in the first place...")

    input("Press ENTER")
    print()

    print(" You do your adventuring your way... I guess...")
    print("------------------------------------------------------")

    input("Press ENTER")
    print()

    return ""

def room_description(chest_order):
    print("------------------------------------------------------")
    print(" You find yourself in a small dimly lit room. At the")
    print(" center of the room are three medium-sized chests. As")
    print(" you draw nearer to them a small glint on the ground")
    print(" in front of you catches your eye. Bending down you")
    print(" pick up a small brass key (it probably goes to one of")
    print(" the three chests). What will you do?")
    print()
    print(" (1) Use the key on the Left Chest")
    print(" (2) Use the key on the Center Chest")
    print(" (3) Use the key on the Right Chest")
    print(" (4) Leave the room without opening any of the chests")
    print("------------------------------------------------------")
    print()

    while True:
        try:
            user_input = int(input("What will you do? "))
            
            if 1 <= user_input <= 3:
                door_choice = int(chest_order[(user_input - 1)])

            elif user_input == 4:
                result = going_cakeless()

                return result

            if door_choice == 1:
                result = open_chest_1()

                return result

            elif door_choice == 2:
                result = open_chest_2()

                return result

            elif door_choice == 3:
                result = open_chest_3()

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

def randomize_chests(chest_order):
    chest_count = 3
    chest_pool = [1,2,3]

    for chest in range(chest_count):
        total_chests = len(chest_pool)
        random_chest = random.randrange(total_chests)

        chest_order.append(chest_pool[random_chest])
        chest_pool.pop(random_chest)

def three_chests_main():
    chest_order = []
    randomize_chests(chest_order)

    print (f" Print: {chest_order}")

    results = room_description(chest_order)

    return results