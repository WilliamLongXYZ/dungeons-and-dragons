import random
from utils import append_list_as_row as csv_append

classes = [
    "Barbarian", "Bard", "Cleric",
    "Druid", "Fighter", "Monk",
    "Paladin", "Ranger", "Rogue",
    "Sorceror", "Warlock", "Wizard"
]
races   = [
    "Dragonborn", "Dwarf", "Elf",
    "Gnome", "Half-Elf", "Halfling",
    "Half-Orc", "Human", "Tiefling",     
]

def determine_race():
    return random.choice(races)

def determine_class():
    return random.choice(classes)

def roll_stat():
    return random.randint(9, 18)    

def roll_stats():
    stats = []
    for i in range(0, 6): stats.append(roll_stat())
    return stats

def alter_stats(stats, race):
    if race == races[0]:
        stats[0] += 2
        stats[5] += 1
    elif race == races[1]:
        stats[2] += 2
    elif race == races[2]:
        stats[1] += 2
    elif race == races[3]:
        stats[3] += 2
    elif race == races[4]:
        stats[5] += 2
        while True:
            n = random.randint(1, len(stats)-1)
            if n != 5:
                stats[n] += 1
                break
        while True:
            m = random.randint(1, len(stats)-1)
            if m != 5 and m != n:
                stats[m] += 1
                break
        input()
    elif race == races[5]:
        stats[1] += 2
    elif race == races[6]:
        stats[0] += 2
        stats[2] += 1
    elif race == races[7]:
        stats = [stat + 1 for stat in stats]
    elif race == races[8]:
        stats[5] += 2
        stats[3] += 1
    return stats

def determine_mods(stats):
    mods = []
    for stat in stats:
        if stat == 1: mod = -5
        elif stat >= 2 and stat <= 3: mod = -4
        elif stat >= 4 and stat <= 5: mod = -3
        elif stat >= 6 and stat <= 7: mod = -2
        elif stat >= 8 and stat <= 9: mod = -1
        elif stat >= 10 and stat <= 11: mod = 0
        elif stat >= 12 and stat <= 13: mod = 1
        elif stat >= 14 and stat <= 15: mod = 2
        elif stat >= 16 and stat <= 17: mod = 3
        elif stat >= 18 and stat <= 19: mod = 4
        elif stat >= 20 and stat <= 21: mod = 5
        elif stat >= 22 and stat <= 23: mod = 6
        elif stat >= 24 and stat <= 25: mod = 7
        elif stat >= 26 and stat <= 27: mod = 8
        elif stat >= 28 and stat <= 29: mod = 9
        elif stat == 30: mod = 10
        else: return "Error"
        mods.append(mod)
    return mods

def log_character(*args):
    char_info = []
    for arg in args:
        char_info.append(arg)
    csv_append('characters.csv', char_info)

def create_character():
    race = determine_race()
    character_class = determine_class()
    stats = alter_stats(roll_stats(), race)
    mods = determine_mods(stats)
    log_character(race, character_class, stats, mods)
    return race, character_class, stats, mods

while True:
    create_character()
    input()

'''
Dragonborn

Racial Traits
+2 Strength, +1 Charisma, Draconic Ancestry, Breath Weapon, Damage Resistance
View Dragonborn Details
--------------------------------------------------------------------------------------------------------
Dwarf

Racial Traits
+2 Constitution, Darkvision, Dwarven Resilience, Dwarven Combat Training, Stonecunning
View Dwarf Details
--------------------------------------------------------------------------------------------------------
Elf

Racial Traits
+2 Dexterity, Darkvision, Keen Senses, Fey Ancestry, Trance
View Elf Details
--------------------------------------------------------------------------------------------------------
Gnome

Racial Traits
+2 Intelligence, Darkvision, Gnome Cunning
View Gnome Details
--------------------------------------------------------------------------------------------------------
Half-Elf

Racial Traits
+2 Charisma, +1 to Two Other Ability Scores, Darkvision, Fey Ancestry, Skill Versatility
View Half-Elf Details
--------------------------------------------------------------------------------------------------------
Halfling

Racial Traits
+2 Dexterity, Lucky, Brave, Halfling Nimbleness
View Halfling Details
--------------------------------------------------------------------------------------------------------
Half-Orc

Racial Traits
+2 Strength, +1 Constitution, Darkvision, Menacing, Relentless Endurance, Savage Attacks
View Half-Orc Details
--------------------------------------------------------------------------------------------------------
Human

Racial Traits
+1 to All Ability Scores, Extra Language
View Human Details
--------------------------------------------------------------------------------------------------------
Tiefling

Racial Traits
+2 Charisma, +1 Intelligence, Darkvision, Hellish Resistance, Infernal Legacy

str, dex, con, int, wis, cha
'''
