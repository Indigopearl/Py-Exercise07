import random

print()
print("Welcome to the character generator!")
print()


# define a function to generate a character with randomized stats
def generate_character():
    # randomly choose a character class
    character_class = random.choice(['Barbarian', 'Cleric', 'Druid'])

    # generate random stats between 3 and 15 for each category
    health = random.randint(3, 15)
    strength = random.randint(3, 15)
    magic = random.randint(3, 15)
    initiative = random.randint(3, 15)

    # modify stats based on character class
    if character_class == 'Barbarian':
        health *= 3
        strength *= 3
    elif character_class == 'Cleric':
        magic *= 3
        initiative *= 3
    else:
        health *= 2
        magic *= 2
        initiative *= 2

    # choose a random stat to print in binary, hex, or decimal
    stat_to_print = random.choice(
        ['health', 'strength', 'magic', 'initiative'])
    stat_format = 'd'  # default is decimal
    if random.random() < 0.1:  # 10% chance of binary format
        stat_format = 'b'
    elif random.random() < 0.1:  # 10% chance of hex format
        stat_format = 'x'

    # return a dictionary containing the character's stats, class, and format for one stat
    return {'class': character_class, 'health': health, 'strength': strength, 'magic': magic, 'initiative': initiative, 'stat_to_print': stat_to_print, 'stat_format': stat_format}


# prompt the user for the number of characters to generate
num_characters = int(input("How many characters would you like to create? "))
print()

# initialize an empty list to hold the characters
characters = []

# prompt the user for each character's name and generate a character for each
for i in range(num_characters):
    name = input(f"Character {i+1}? ")
    character = generate_character()
    characters.append({'name': name, **character})

# print out the team 1 with each character's name and stats

print()
print("***YOUR CHARACTERS ARE COMPLETE***")
print()


print("Team 1:")
print()
for character in characters:
    stat_to_print = character['stat_to_print']
    stat_format = character['stat_format']
    print(f"{character['name']} the {character['class']}!")
    print(
        f"    Health = {format(character['health'], stat_format) if stat_to_print == 'health' else character['health']}")
    print(
        f"    Strength = {format(character['strength'], stat_format) if stat_to_print == 'strength' else character['strength']}")
    print(
        f"    Magic = {format(character['magic'], stat_format) if stat_to_print == 'magic' else character['magic']}")
    print(
        f"    Initiative = {format(character['initiative'], stat_format) if stat_to_print == 'initiative' else character['initiative']}")
    print()  # add a blank line after each character's stats
