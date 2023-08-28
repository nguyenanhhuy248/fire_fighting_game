from game_map import *
from Class.player import *
from Class.fire import *
from Class.equipment import *
from function import *
from character_creation import create_character
import pandas as pd
import os
import sys
from mission_1 import mission_1
from mission_2 import mission_2

user_id = None
player_dictionary = {"Mission 1": "Not completed", "Mission 2": "Not completed"}

# Create or load user_id

active_1 = True
while active_1:
    print("Welcome to the Fire evacuation MUD game!\n")
    prompt_1 = input(
        "Have you had an account ID?\
        \nType 'Y' for Yes, or 'N' for No, or 'quit' to exit the game\n"
    )

    user_list = pd.read_csv(
        "../saved_file/user_list.csv",
        sep=",",
        error_bad_lines=False,
        index_col=False,
        dtype="unicode",
    )

    if prompt_1.lower() == "y":
        active_2 = True
        while active_2:
            user_id = input(
                "Enter your unique account ID, or 'back' to go to back to account menu\n"
            )
            if user_id in user_list["id"].values.tolist():
                print(f"Hello user {user_id}, your saved progress:")
                try:
                    with open(f"../saved_file/{user_id}.txt", "r") as myfile:
                        saved = myfile.read()
                        player_dictionary = eval(saved)
                        print(player_dictionary)
                except Exception:
                    print("No progress found, start by creating your character.")
                active_2 = False
                active_1 = False
            elif user_id.lower() == "back":
                prompt_2 = input("Going back? Type 'Y' to proceed, or 'N' to cancel\n")
                if prompt_2.lower() == "y":
                    active_2 = False
                    active_1 = True
                else:
                    continue
            else:
                print("User ID not found, please try again!")
                continue

    elif prompt_1.lower() == "n":
        active_3 = True
        while active_3:
            new_user_id = input(
                "Enter your unique account ID, or 'back' to go to back to account menu\n"
            )
            if new_user_id in user_list["id"].values.tolist():
                print("Sorry, that user ID was taken, please try another user ID")
                continue
            elif new_user_id.lower() == "back":
                prompt_3 = input("Going back? Type 'Y' to proceed, or 'N' to cancel\n")
                if prompt_3.lower() == "y":
                    active_3 = False
                    active_1 = True
                else:
                    continue
            else:
                new_user = pd.DataFrame([new_user_id], columns=["id"])
                updated_user_list = user_list.append(new_user, ignore_index=True)
                updated_user_list.to_csv("../saved_file/user_list.csv", index=False)
                print(f"User ID: {new_user_id} successfully created")
                user_id = new_user_id
                active_3 = False
                active_1 = False

    elif prompt_1.lower() == "quit":
        prompt_4 = input("Exit the game? Type 'Y' to proceed, or 'N' to cancel\n")
        if prompt_4.lower() == "y":
            print("Quit game!")
            sys.exit(0)
        else:
            continue

    else:
        print("Incorrect command!\n")
        continue


"""Character creation"""

while True:
    if f"{user_id}.txt" in os.listdir("../saved_file"):
        break
    else:
        prompt_5 = input(
            "\nNow you can create your character in the game.\
                         \nType 'Y' to start character creation, or 'quit' to exit the game\n"
        )
        if prompt_5.lower() == "y":
            player_dictionary.update(create_character())
            print(player_dictionary)
            break
        elif prompt_5.lower() == "quit":
            prompt_6 = input(
                "Exit the game? Your progress this time is not saved.\
                             \nType 'Y' to proceed, or 'N' to cancel\n"
            )
            if prompt_6.lower() == "y":
                print("Quit game!")
                sys.exit(0)
            else:
                continue
        else:
            print("Incorrect command")
            continue

# Mission 1

mission_1(user_id, player_dictionary)

# Mission 2

mission_2(user_id, player_dictionary)

# All missions completed, save or delete profile and quit

while True:
    prompt = input(
        "\nAll missions accomplished! Do you want to save your character' profile.\
        \nType 'Y' to save profile and quit, or 'N' to quit without saving character's profile\n"
    )
    if prompt.lower() == "y":
        player_dictionary.update(
            {"Mission 1": "Not completed", "Mission 2": "Not completed"}
        )
        key_list = [
            "position",
            "fire position",
            "fire power",
            "mask",
            "e_type",
            "e_power",
        ]
        delete_dictionary_key(player_dictionary, key_list)
        save_and_quit_win(user_id, player_dictionary)

    elif prompt.lower() == "n":
        delete_progress_and_quit(user_id)
    else:
        print("Incorrect command!")
        continue
