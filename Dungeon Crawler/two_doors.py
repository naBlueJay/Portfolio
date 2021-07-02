import random

def left_door():
    print("------------------------------------------------------")
    print(" Taking the left door you press forward on your quest")
    print(" for riches.")
    print()
    input("Press ENTER")
    print(" You couldn't help but wonder who would come into a")
    print(" dungeon and maintain the other door... You probably")
    print(" dodged a bullet not taking the door on the right.")
    print("------------------------------------------------------")
    ()
    input("Press ENTER")

    return ""


def right_door():
    print("------------------------------------------------------")
    print(" Opening the left door you take a few steps into the")
    print(" room behind. The room is bathed in shadows. Before")
    print(" you have time to react a long arm shoots out and grabs")
    print(" you by the ancle dragging you towards the shadows.")
    print()
    input("Press ENTER")
    print(" You never knew what creature ended up killing you only")
    print(" that anything well-kempt in a dungeon probably should")
    print(" have been avoided.")
    print("------------------------------------------------------")
    print()
    input("Press ENTER")

    return "DEAD"

def room_description():
    print("------------------------------------------------------")
    print(" You find yourself walking down a long hallway.")
    print(" Gradually the path you are taking widens and ends at")
    print(" two doors.")
    print()
    input("Press ENTER")
    print()
    print(" The door on the left is covered with dry-rot and looks")
    print(" like it will disintegrate at the slightest touch. The")
    print(" door on the right shows sign of ware from frequent use.")
    print(" Even with the signs of ware, the door on the right")
    print(" appears to be well kempt.")
    print()
    input("Press ENTER")
    print()
    print(" (1) Take the door on the left")
    print(" (2) Take the door on the right")
    print("------------------------------------------------------")
    print()

    user_input = ("Which door will you take?")

    while True:
        try:
            user_input = int(input("What will you do? "))

            if user_input == 1:
                result = left_door()

                return result

            elif user_input == 2:
                result = right_door()

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

def randomize_doors(door_order):
    door_count = 2
    door_pool = [1,2]

    for chest in range(door_count):
        total_chests = len(door_pool)
        random_chest = random.randrange(total_chests)

        door_order.append(random_chest)
        door_pool.pop(random_chest)

def tow_doors_main():
    door_order = []
    randomize_doors(door_order)

    results = room_description()