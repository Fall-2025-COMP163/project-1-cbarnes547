"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Chloe Barnes
Date: 10/31/2025

AI Usage: [Document any AI assistance used] 
I used AI (ChatGPT) to help write lines 106 and 107. These lines determine the directory from a file path and then check if that directory exists on the file system.
I used AI (Gemini) to generate character backstories.
i used AI (Gemini) to help me create clear variable names.
"""

"""
TA Elias:
first issue: no virtual env:
    (cmd + shift + p)
    python create environment
    select recommended if there is one else pick the global one
    activate venv: path/to/activate/executable
    install libs: like this pip/pip3 install lib_name

to run the tests:
    python -m pytest


"""
import os

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

"""
first issue: no virtual env:
    (cmd + shift + p)
    python create environment
    select recommended if there is one else pick the global one
    activate venv: path/to/activate/executable
    install libs: like this pip/pip3 install lib_name

to run the tests:
    python -m pytest


"""
import os


def create_character(name, character_class):
    if name == "" or name is None:
        name = "Silent Vanguard"

    # list of valid classes
    valid_class = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_class:
        return None

    # starting level
    level = 1

    # get stats based on class and level
    strength, magic, health = calculate_stats(character_class, level)

    # all new characters start with the same amount of gold
    gold = 50

    equipment = "Basic sword"

    character = {
        "name": name,
        "class": character_class,
        "strength": strength,
        "magic": magic,
        "health": health,
        "level": level,
        "gold": gold,
        "equipment": equipment
    }

    # give each class an automatic backstory
    if character_class == "Warrior":
        backstory = "Born in the harsh mountains, this warrior has trained from childhood to wield sword and shield with unmatched skill. Seeking glory on the battlefield, they fight not only for victory but to uphold honor and protect the weak."
    elif character_class == "Mage":
        backstory = "A prodigy in the arcane arts, the mage spent years in secluded towers studying ancient tomes and unlocking the secrets of magic. Driven by curiosity and the desire to shape reality, they explore both dangerous knowledge and forgotten lore."
    elif character_class == "Rogue":
        backstory = "Once a street urchin surviving by wit and stealth, the rogue learned to navigate the shadows and exploit every opportunity. Cunning and resourceful, they trust no one fully, relying solely on their skills to survive and outsmart their enemies."
    else:
        backstory = "Blessed with divine insight, the cleric has dedicated their life to healing and protecting others. Traveling from village to village, they bring peace, balance, and hope to a world plagued by darkness, guided by faith and compassion."

    character["backstory"] = backstory

    return character

def calculate_stats(character_class, level):
    
    if character_class == "Warrior":
        strength = 15 + (level * 2)
        magic = 5 + (level)
        health = 30 + (level * 5)
    elif character_class == "Mage":
        strength = 8 + (level)
        magic = 20 + (level)
        health = 20 + (level * 3)
    elif character_class == "Rogue":
        strength = 12 + (level * 2)
        magic = 10 + (level)
        health = 25 + (level * 4)
    elif character_class == "Cleric":
        strength = 10 + (level)
        magic = 15 + (level * 2)
        health = 28 + (level * 4)
    return strength, magic, health


def save_character(character, filename):
    if filename == "" or filename is None:
        print("Invalid file name")
        return False
    
    # check if the directory exist
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        print("Error: Directory does not exist.")
        return False

    # write all character info to the file
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
        file.write(f"Equipment: {character['equipment']}\n")
        file.write(f"Backstory: {character['backstory']}\n")
    return True


def load_character(filename):
    if not os.path.exists(filename):
        print("File not found.")
        return None

    # open the file and read all the data
    with open(filename, "r") as file:
        lines = file.readlines()

        # empty dictionary to rebuild the character
        character = {}

        # go through each line and pull out the data
        for line in lines:
            line = line.strip()
            parts = line.split(": ")

            # only run if the line has two parts
            if len(parts) == 2:
                key = parts[0]
                value = parts[1]

                # match file keys to dictionary keys
                if key == "Character Name":
                    character["name"] = value
                elif key == "Class":
                    character["class"] = value
                elif key == "Level":
                    character["level"] = int(value)
                elif key == "Strength":
                    character["strength"] = int(value)
                elif key == "Magic":
                    character["magic"] = int(value)
                elif key == "Health":
                    character["health"] = int(value)
                elif key == "Gold":
                    character["gold"] = int(value)
                elif key == "Equipment":
                    character["equipment"] = value
                elif key == "Backstory":
                    character["backstory"] = value

    return character

def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print(f"Equipment: {character['equipment']}")
    print(f"Backstory: {character['backstory']}")

    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print(f"Equipment: {character['equipment']}")
    print(f"Backstory: {character['backstory']}")


def level_up(character):
        # add one to the level
    character["level"] = character["level"] + 1

    # get new stats for this higher level
    strength, magic, health = calculate_stats(character["class"], character["level"])

    # update dictionary values
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    print(f"{character['name']} leveled up to Level {character['level']}!")

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    char = create_character("TestHero", "Warrior")
    display_character(char)
    
    char = create_character("TestHero", "Warrior")
    display_character(char)
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
