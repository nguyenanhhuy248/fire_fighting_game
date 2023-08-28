from game_map import *
from Class.player import *
from Class.fire import *
from Class.equipment import *
from function import *
import os


# Mission 1: evacuation from the lecture theatre


def mission_1(user_id, player_dictionary):
    game_world = matrix

    if player_dictionary["Mission 1"] == "Not completed":
        active_1 = True
        active_2 = True
    else:
        active_1 = False
        active_2 = False

    while active_2:
        prompt_1 = input("Type 'Y' to go to Mission 1\n")
        if prompt_1.lower() == "y":
            break
        else:
            print("Incorrect command")
            continue

    while active_1:
        print(
            "\nYour character is a university student sitting in a lecture theatre.\
                \nSuddenly there is a fire in the room!\
                \n\n1. Your first mission is to get out of the lecture theatre room,\
                \nthrough one of the 3 fire exits.\
                \nFor this mission, a diagram showing the lecture theatre room and\
                \nthe fire exits will be shown only once when you enter the game,\
                \nand will disappear after you confirm to start.\
                \nYou will then be given your initial position in the lecture theatre."
        )

        prompt_2 = input(
            "Start mission 1 now? Type 'Y' to enter the mission, or 'quit' to exit\n"
        )
        if prompt_2.lower() == "y":
            print(
                f"\nThis is the diagram showing the lecture theatre.\
                \nA position is defined by its vertical position (denoted by a letter)\
                \nand horizontal position (denoted by a number).\
                \nE.g. The exits are in A3, S3, and S13.\
                \nPlease note that this diagram will disappear after you confirm to start the game.\
                \n\n{displayed_map(game_world)}"
            )

            active_3 = True
            while active_3:
                prompt_3 = input(
                    "\nType 'Y' to start playing, or 'N' to go back to mission 1 description\
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
                        print(f"Your current position is {saved_position}")

                    else:
                        player1 = Player((init_i, init_j))
                        print(f"Your initial position is {column_list[init_j]}{init_i}")

                    active_4 = True
                    while active_4:
                        prompt_4 = input(
                            "Type 'move' to start your movement,\
                                        \nor 'look' to see the position next to you,\
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
                                matrix[player1.state[0], player1.state[1]],
                                prompt_5.lower(),
                            ):
                                prompt_6 = input(
                                    "What is the distance you want to move?\
                                                \nE.g. a move from A1 to B1 is with distance = 1. \n"
                                )
                                x = player1.move(prompt_5.lower(), int(prompt_6))

                                if matrix[player1.state[0], player1.state[1]] in [
                                    8,
                                    15,
                                ]:
                                    player_dictionary.update({"Mission 1": "Completed"})
                                    print(
                                        "Congratulation!!! You have accomplished mission 1!"
                                    )
                                    player_dictionary.update(
                                        {"position": f"{current_position(player1)}"}
                                    )
                                    active_4 = False
                                    active_3 = False
                                    active_1 = False
                                elif not x:
                                    print("Invalid distance!")
                                else:
                                    print(
                                        f"Move successfully!!!. Current position: {current_position(player1)}"
                                    )
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
                        elif prompt_4.lower() == "quit":
                            prompt_8 = input(
                                "Do you want to save progress and quit the game?\
                                            \nType 'Y' to quit, or 'N' go back\n"
                            )
                            if prompt_8.lower() == "y":
                                player_dictionary.update(
                                    {"position": f"{current_position(player1)}"}
                                )
                                save_and_quit(user_id, player_dictionary)
                            else:
                                continue

                        else:
                            print("Incorrect command!")

                elif prompt_3.lower() == "n":
                    prompt_9 = input(
                        "To mission 1 description?\
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
    test_dict = {"Mission 1": "Not completed", "Mission 2": "Not completed"}
    mission_1(900, test_dict)
