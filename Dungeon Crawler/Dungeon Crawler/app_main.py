import random
import three_chests
import escape_room
import two_doors
import cavern

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
    ROOMS = [1, 2, 3, 4]
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

def visit_room( room):
    results = ""

    if room == 1:
        results = three_chests.three_chests_main()
    elif room == 2:
        results = escape_room.escape_room_main()
    elif room == 3:
        results = two_doors.tow_doors_main()
    elif room == 4:
        results = cavern.cavern_main()

    return results

def main():
    play_game = get_menu()

    while play_game == True:
        room_list = []
        dungeon_size = 0
        result = ""

        generate_dungeon(room_list)
        dungeon_size = len(room_list)

        # print(room_list)
        
        for room in range(dungeon_size):
            result = visit_room( room_list[0])
            room_list.pop(0)

            if result == "EXIT":
                print("------------------------------------------------------")
                print(" You survived the dungeon... I guess... Try harder")
                print(" next time.")
                print("------------------------------------------------------")
                break
            elif result == "DEAD":
                print("------------------------------------------------------")
                print(" You died. Better luck next time.")
                print("------------------------------------------------------")
                break
        

        if result == "":
            print("------------------------------------------------------")
            print(" Congradualtions on making it out of the dungeon alive!")
            print("------------------------------------------------------")

        play_game = get_menu()

    print("------------------------------------------------------")
    print(" Thank you for playing Dungeon Crawler!!!")
    print(" Feel free to play again another time.")
    print("------------------------------------------------------")
    
    input("Press ENTER")



if __name__ == '__main__':
    main()