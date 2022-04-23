import random


def drink_potion(health):
    return health+2

def attack(weapon, health):
    if weapon == "sword": return  health - 1
    if weapon == "club": return health - 1

def encounter():
    inventory = {
    "potion": 1,
    "sword": 1,
    }
    health = 5
    goblin_health = 6
    chosen = []
    while goblin_health:
        attacking = False
        defending = False
        healing = False
        option = random.choice(["attacking", "defending", "healing"])
        chosen.append(option)
        if option == "attacking": attacking = True
        elif option == "defending": defending = True
        elif option == "healing": healing = True

        if healing:
            if inventory["potion"]:
                inventory["potion"] -= 1
                health = drink_potion(health)
        if not defending:
            health = attack("club", health)
        if attacking:
            goblin_health = attack("sword", goblin_health)
        if health <= 0:
            # print("You died.")
            return (chosen, False)
        if goblin_health <= 0:
            # print(f"The goblin has been killed in {len(chosen)} turns.")
            return (chosen, True)

def read_log():
    enemy_health = 7
    with open("log.csv", "r") as log:
        lines = log.readlines()
    subten = []
    for line in lines:
        if "False" in line:
            lines.remove(line)
        choices = line.split(',')[0].split(" -- ")
        choices.remove(choices[-1])
        if len(choices) <= enemy_health:
            subten.append(choices)
    print(subten)

def main():
    option = input()
    if option != "read":
        while 1:
            choices, success = encounter()
            with open("log.csv", "a") as log:
                for choice in choices:
                    log.write(f"{choice} -- ")
                log.write(f",{success}\n")
    else:
        read_log()

if __name__ == "__main__":
    main()
