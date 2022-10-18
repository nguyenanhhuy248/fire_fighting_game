

def create_character():
    character_dictionary = {}
    
    active = True
    while active:
        name = input("What's your character's name?\n")

        age= input("What's your character's age?\n")

        special = input("What is your character's special skill?\n")

        parameter = ()
        while active:
            extra_1 = input("Extra information about your character? \nType \"no\" to not including anything else.\n")
            if extra_1 == "no":
                active = False
            else:
                extra_2 = input(f"Details on your character's {extra_1}.\n")
                parameter = parameter + (extra_1,)
                parameter = parameter + (extra_2,)
    
    character_dictionary["name"] = name
    character_dictionary["age"] = age
    character_dictionary["special_power"] = special
    j = 0
    while j < len(parameter):
        character_dictionary[parameter[j]] = parameter[j+1]
        j+=2
    return (character_dictionary)

if __name__ == "__main__":
    create_character()
