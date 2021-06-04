import random

def roll_stat():
    return random.randint(9, 18)    

def roll_stats():
    stats = []
    for i in range(0, 6): stats.append(roll_stat())
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
        else: mod = None
        mods.append(mod)
    return mods

stats = roll_stats()
mods = determine_mods(stats)
print(stats, mods)
