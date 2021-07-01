import random
import three_chests
import escape_room

ROOMS = [1, 2, 3, 4, 5]

def print_instructions():
    print("------------------------------------------------------")
    print(" Dungeon Crawler is a game that gives you, the player,")
    print(" a chance to explore a deadly dungeon avoiding traps,")
    print(" collecting treasures and making it back to your home")
    print(" alive.")
    print()
    print(" To play, type the letter in the terminal that goes with") 
    print(" the option presented in the situation you find ")
    print(" yourself in.")
    print("------------------------------------------------------")
    print()

    input("Press ENTER")

def get_menu():

    while True:

        print("------------------------------------------------------")
        print(" Dungeon Crawler")
        print()
        print(" (i) Instructions")
        print(" (p) Play Game")
        print(" (e) Exit Game")
        print("------------------------------------------------------")
        print()

        response = input()

        if response.upper() == "I":
            print_instructions()

        elif response.upper() == "P":
            return True

        elif response.upper() == "E":
            return False
        
        else:
            print("Please select a valid option.")
            input("Press ENTER")

def generate_dungeon(room_list):
    global ROOMS
    rooms = ROOMS
    room_limit = len(ROOMS)
    generated = False
    number_of_rooms = ""

    while True:
        print("------------------------------------------------------")
        print(f" How large do you want the dengeon to be? (1-{room_limit} rooms)")

        while not isinstance(number_of_rooms, int):
            try:
                number_of_rooms = int(input("Please enter your response: "))
            except:
                print("Please use an integer: ")


        if number_of_rooms <= room_limit and number_of_rooms > 0:

            for rew_room in range(number_of_rooms):
                total_rooms = len(rooms)
                random_room = random.randrange(total_rooms)

                room_list.append(rooms[random_room])
                rooms.pop(random_room)
            
            generated = True
        

        if generated == True:
            break

def visit_room(inventory, room):
    results = ""

    if room == 1:
        results = three_chests.three_chests_main(inventory)
    elif room == 2:
        results = escape_room.escape_room_main()
    elif room == 3:
        pass
    elif room == 4:
        pass
    elif room == 5:
        pass

    return results

def main():
    play_game = get_menu()
    room_list = []
    inventory = []
    dungeon_size = 0

    while play_game == True:
        generate_dungeon(room_list)
        dungeon_size = len(room_list)

        # print(room_list)
        input("Press ENTER")
        
        for room in range(dungeon_size):
            result = visit_room(inventory, room_list[0])
            room_list.pop(0)

            if result == "EXIT":
                break
            elif result == "DEAD":
                break


        play_game = get_menu()

    print("------------------------------------------------------")
    print(" Thank you for playing Dungeon Crawler!!!")
    print(" Feel free to play again another time.")
    print("------------------------------------------------------")
    
    input("Press ENTER")



if __name__ == '__main__':
    main()