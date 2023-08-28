from game_map import *
from Class.player import *
from Class.fire import *
from Class.equipment import *
from function import *
import os


def mission_2(user_id, player_dictionary):
    game_world = matrix

    if player_dictionary["Mission 2"] == "Not completed":
        active_1 = True
        active_2 = True
    else:
        active_1 = False
        active_2 = False

    while active_2:
        prompt_1 = input("\nType 'Y' to go to Mission 2\n")
        if prompt_1.lower() == "y":
            break
        else:
            print("Incorrect command")
            continue

    while active_1:
        print(
            "\n2. Now it is the time to be a hero! Your mission is extinguishing the fire.\
                \nRemember to collect an oxygen mask, denoted by 'm' on the game map.\
                \nWithout an oxygen mask, you can not stand at the fire position.\
                \nYou will also need to collect a fire extinguisher.\
                \nThere are powder type, denoted by 'p' and foam type, denoted by 'p'.\
                \nYou can carry only one extinguisher at a time.\
                \nThe game map and the fire position will be shown to you after you start mission 2."
        )

        prompt_2 = input(
            "Start mission 2 now? Type 'Y' to enter the mission, or 'quit' to exit\n"
        )
        if prompt_2.lower() == "y":
            if f"map_{user_id}.txt" in os.listdir("../saved_file"):
                game_world = np.loadtxt(f"../saved_file/map_{user_id}.txt").reshape(
                    17, 19
                )

            print(
                f"\nThis is the diagram showing the lecture theatre.\
                \nA position is defined by its vertical position (denoted by a letter)\
                \nand horizontal position (denoted by a number).\
                \nE.g. The exits are in A3, S3, and S13.\
                \nOxygen mask is denoted by 'm' on the game map.\
                \nPower extinguisher is denoted by 'p' and foam extinguisher is denoted by 'p'.\
                \nPlease note that this diagram will disappear after you confirm to start the game.\
                \n\n{displayed_map(game_world)}"
            )

            active_3 = True
            while active_3:
                prompt_3 = input(
                    "\nType 'Y' to start playing, or 'N' to go back to mission 2 description\
                                \nOr 'quit' to exit\n"
                )
                if prompt_3.lower() == "y":
                    # Clear the console including the game map
                    os.system("cls||clear")

                    if "position" in list(player_dictionary.keys()):
                        saved_position = player_dictionary["position"]
                        row = int(saved_position[1:])
                        column = int(column_list.index(saved_position[0]))
                        player1 = Player((row, column))

                    if "fire position" in list(player_dictionary.keys()):
                        saved_fire = player_dictionary["fire position"]
                        row = int(saved_fire[1:])
                        column = int(column_list.index(saved_fire[0]))
                        fire1 = Fire((row, column))
                        fire1.power = player_dictionary["fire power"]
                        if player_dictionary["mask"] != "":
                            player1.mask = Mask(player_dictionary["mask"])
                        if player_dictionary["e_type"] != "":
                            player1.extinguisher = Extinguisher(
                                player_dictionary["e_type"],
                                player_dictionary["e_power"],
                            )

                    else:
                        fire1 = Fire((init_a, init_b))

                    fire1.display()
                    print(f"Your current position is {current_position(player1)}")

                    active_4 = True
                    while active_4:
                        prompt_4 = input(
                            "Type 'move' to start your movement,\
                                        \nor 'look' to see the position next to you,\
                                        \nor 'collect' to collect the item at your current position,\
                                        \nor 'quit' to save progress and quit\n"
                        )
                        if prompt_4.lower() == "move":
                            prompt_5 = input(
                                "Which direction do you want to move?\
                                            \nType 'up', 'down', 'left', 'right'.\
                                            \nNote that you can only move 'up', 'down'\
                                            \nwhen you are in the aisle (A,J,S).\
                                            \nIf you are in a seat row, you can only move 'left' or 'right'.\n"
                            )
                            if Player.check_valid_direction(
                                game_world[player1.state[0], player1.state[1]],
                                prompt_5.lower(),
                            ):
                                prompt_6 = input(
                                    "What is the distance you want to move?\
                                                \nE.g. a move from A1 to B1 is with distance = 1. \n"
                                )
                                if is_integer_distance(prompt_6) == True:
                                    x = player1.move(prompt_5.lower(), int(prompt_6))
                                    if not x:
                                        print("Invalid distance!")
                                    elif player1.state == fire1.state:
                                        if player1.mask != None:
                                            if player1.extinguisher != None:
                                                active_5 = True
                                                while active_5:
                                                    prompt_12 = input(
                                                        "You are at the fire position. Type 'spray' to use your extinguisher\n"
                                                    )
                                                    if prompt_12.lower() == "spray":
                                                        spray(player1, fire1)
                                                        if fire1.power == 0:
                                                            player_dictionary[
                                                                "Mission 2"
                                                            ] = "Completed"
                                                            print(
                                                                "Congratulation! Fire extinguished! You win!!!"
                                                            )
                                                            active_5 = False
                                                            active_4 = False
                                                            active_3 = False
                                                            active_1 = False
                                                            if (
                                                                f"map_{user_id}.txt"
                                                                in os.listdir(
                                                                    "../saved_file"
                                                                )
                                                            ):
                                                                os.remove(
                                                                    f"../saved_file/map_{user_id}.txt"
                                                                )
                                                        else:
                                                            print(
                                                                f"Remaining fire power: {fire1.power}"
                                                            )
                                                            print(
                                                                "You need to collect another extinguisher and come back!\n"
                                                            )
                                                            active_5 = False
                                                            active_4 = True
                                                    else:
                                                        print("Incorrect command!")
                                            else:
                                                print(
                                                    "You do not have any fire extinguisher! Go collect one!"
                                                )
                                        else:
                                            print(
                                                "A lot of smoke here! You need to have an oxygen mask, go collect one!"
                                            )

                                    else:
                                        print(
                                            f"Move successfully!!!. Current position: {current_position(player1)}"
                                        )
                                else:
                                    print("Distance must be an integer!")
                            else:
                                print("Invalid direction!")

                        elif prompt_4.lower() == "look":
                            prompt_7 = input(
                                "You can see the position beside you, which way you want to see?\
                                            \nType 'up', 'down', 'left', 'right'.\n"
                            )
                            if prompt_7 in ["up", "down", "left", "right"]:
                                look_value = player1.look(prompt_7)
                                if look_value == False:
                                    print(
                                        "Beside you in this direction is the room wall!"
                                    )
                                else:
                                    see = f"{column_list[look_value[1]]}{look_value[0]}"
                                    print(
                                        f"The position beside you in this direction is: {see}"
                                    )
                            else:
                                print("Invalid direction!")

                        elif prompt_4.lower() == "collect":
                            player1.collect(game_world)

                        elif prompt_4.lower() == "quit":
                            prompt_8 = input(
                                "Do you want to save progress and quit the game?\
                                            \nType 'Y' to quit, or 'N' go back\n"
                            )
                            if prompt_8.lower() == "y":
                                player_dictionary.update(
                                    {
                                        "position": f"{current_position(player1)}",
                                        "fire position": f"{current_position(fire1)}",
                                        "fire power": f"{fire1.power}",
                                    }
                                )

                                if player1.mask != None:
                                    player_dictionary.update(
                                        {"mask": f"{player1.mask.name}"}
                                    )
                                else:
                                    player_dictionary.update({"mask": ""})
                                if player1.extinguisher != None:
                                    player_dictionary.update(
                                        {
                                            "e_type": f"{player1.extinguisher.name}",
                                            "e_power": f"{player1.extinguisher.power}",
                                        }
                                    )
                                else:
                                    player_dictionary.update(
                                        {"e_type": "", "e_power": ""}
                                    )

                                with open(
                                    f"../saved_file/map_{user_id}.txt", "w"
                                ) as map:
                                    for row in game_world:
                                        np.savetxt(map, row)
                                    map.close()
                                save_and_quit(user_id, player_dictionary)
                            else:
                                continue

                        else:
                            print("Incorrect command!")

                elif prompt_3.lower() == "n":
                    prompt_9 = input(
                        "To mission 2 description?\
                                    \nType 'Y' to proceed, or 'N' to go back\n"
                    )
                    if prompt_9.lower() == "y":
                        os.system("cls||clear")
                        break
                    else:
                        continue

                elif prompt_3.lower() == "quit":
                    prompt_10 = input(
                        "Do you want to quit the game?\
                                    \nType 'Y' to quit, or 'N' go back\n"
                    )
                    if prompt_10.lower() == "y":
                        save_and_quit(user_id, player_dictionary)
                    else:
                        continue

                else:
                    print("Incorrect command")
                    continue

        elif prompt_2.lower() == "quit":
            prompt_11 = input(
                "Do you want to quit the game?\
                            \nType 'Y' to quit, or 'N' go back\n"
            )
            if prompt_11.lower() == "y":
                save_and_quit(user_id, player_dictionary)
            else:
                continue

        else:
            print("Incorrect command")
            continue


if __name__ == "__main__":
    test_dict = {
        "Mission 1": "Completed",
        "Mission 2": "Not completed",
        "position": "A3",
        "mask": "",
        "e_type": "",
        "e_power": "",
    }
    mission_2(104, test_dict)
