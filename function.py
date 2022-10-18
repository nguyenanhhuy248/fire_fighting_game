from game_map import column_list
import random
import sys
import os


def is_integer_distance(distance):
    try:
        float(distance)
    except ValueError:
        return False
    else:
        return float(distance).is_integer()
    

def current_position(player):
    return f'{column_list[player.state[1]]}{player.state[0]}'


def spray(player, fire):
    """Extinguish the fire.
    """
    damage = min(int(fire.power), int(player.extinguisher.power))
    fire.power = int(fire.power) - damage
    player.extinguisher = None
    print(f'You have reduced the fire power by {damage}')


def delete_dictionary_key(dictionary, key_list):
    for key in key_list:
        if key in list(dictionary.keys()):
            del dictionary[key]           


def save_and_quit(id, dictionary):
    with open(f"../saved_file/{id}.txt", "w") as myfile:
            myfile.write(str(dictionary))
    print(dictionary)
    print('Quit game!')
    sys.exit(0)


def save_and_quit_win(id, dictionary):
    with open(f"../saved_file/{id}.txt", "w") as myfile:
            myfile.write(str(dictionary))
    diplayed_dict = dictionary
    delete_dictionary_key(diplayed_dict, ['Mission 1', 'Mission 2'])
    print(diplayed_dict)
    print('Quit game!')
    sys.exit(0)


def delete_progress_and_quit(id):
    if f"{id}.txt" in os.listdir('../saved_file'):
        os.remove(f"../saved_file/{id}.txt")
    print('Quit game!')
    sys.exit(0)

