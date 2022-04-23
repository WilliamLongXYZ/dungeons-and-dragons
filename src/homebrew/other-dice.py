import random


def location_die():
    sides = ["Target", "Left Leg", "Right Arm", "Torso", "Torso", "Right Leg", "Head", "Torso", "Right Leg", "Left Leg", "Torso", "Left Arm"]
    return random.choice(sides)

def main():
    actions = {
        "location": location_die
    }
    while 1:
        action = input()
        print(actions[action]())

if __name__ == "__main__":
    main()









'''

1-2. Weapon Break. The force of your blow, or parrying that of your opponent’s, causes your weapon to snap in two. (For magical weapons roll an additional d10, on a 1 they break).

3-4. Goodbye Fair Blade! Roll an Strength / Athletics check DC 15, or your weapon flies d12 feet out of your hand in a random direction. If you have any movement and a bonus action left you can go and pick it up. In doing so you provoke an opportunity attack from anyone in the area, starting with your most immediate opponent. (Otherwise you could simply draw a second weapon, if you have one, using a bonus action).

5-6. Wild Swing. You overextend yourself going for the kill. Your opponent gains advantage on their next attack roll.

7. Stuck Weapon. Your weapon gets stuck in your opponent’s shield, armour, hide, or else in a tree or wall, or the ground. Roll a Strength check to see if you can free it using a bonus action. The DC is 8 + your strength modifier.

8. Ooops! You hit an unintended foe in combat. Randomise all combatants within 5 feet and roll a second attack roll, if you beat their armour class roll damage as if they were your intended target. (Discount sneak attack damage for Rogues).

9. Self Inflicted wound. You manage to slice yourself with your own blade, roll normal damage and half it. (Applies to combatants using slashing weapons and flails only. Other weapon types roll again. Discount sneak attack damage for Rogues).

10-14. Slip Up. You lose your footing. Roll Dexterity / Acrobatics check (DC15) or fall prone. Your turn has ended and melee attacks have advantage on you (see p292 of PH for conditions of being prone).

15. Pulled Muscle (Arms). Roll a Constitution Saving Throw DC15 or the strain of your attack causes you to pull a muscle in your upper body. You have disadvantage in attack rolls and ability checks requiring upper body strength until you have completed three long rests, or received magical healing.

16. Pulled Muscle (Legs). Roll a Constitution Saving Throw DC15 or the strain of combat causes you to pull a muscle in your leg. Your movement is halved, and you lose your dex modifier to AC and initiative, and you have disadvantage on any ability checks that require lower body strength, until you have completed three long rests, or received magical healing.

17-18. Loss of Nerve. Man your opponent looks tough. Make a Wisdom Saving Throw with a base DC of 10 modified by +2 for every hit dice higher than you your opponent has (or -2 for every hit dice less). On a fail you are frightened (see p292 of Player’s Handbook). After one turn you can attempt the saving throw again.

19. Broken Item. In the hurly burly of combat, something fragile – like a magic potion – you’re carrying breaks. Randomise fragile objects you have in your possession and roll to determine which. (Note, better to do this when the combat is over).

20. A Little Accident. Either through fear, excitement or simply needing to go, you soil yourself. 75% chance it’s only pee.

Critical Misses Table (Shooting Range Weapons)
Roll a d20…

1-2. Weapon Break. Your bow shaft or a mechanism in your crossbow breaks and is now useless. (For magical weapons roll an additional d10, on a 1 they break).

3-5. String Break. Your bowstring snaps. Assuming you have a spare string, it requires 1 minute to replace it.

6-8. Loose String. Your string comes loose. You lose this attack. Starting next turn you can make a sleight of hand check DC15 to fix it. Each attempt takes one turn.

9-16. Ooops! You hit an unintended random target. Randomise all combatants within 10 feet (for a short range attack, or 30 feet for a long range attack) and roll a second attack roll, if you beat their armour class roll damage as if they were your intended target (discount sneak attack damage for Rogues).

17-18. Ammo Accident. Your quiver spills (50% strap broken, 50% you tilt it over by accident), and the remainder of your arrows / bolts fall to the floor. If you remain still you can use a bonus action to pick up one a round and still fire using your action. Otherwise you can use an action to pick up 2d8 and put them back in your quiver.

19. Pulled Muscle (Upper Body). Roll a Constitution Saving Throw DC15 or the strain of your attack causes you to pull a muscle in your upper body. You have disadvantage in attack rolls and ability checks requiring upper body strength until you have completed three long rests, or received magical healing.

20. Slip Up. You lose your footing. Roll Dexterity / Acrobatics (DC15) or fall prone. Your turn has ended and melee attacks have advantage on you (see p292 of PH for conditions of being prone).

Critical Misses Table (Thrown Range Weapons)
Roll a d10

1. Weapon Break. The impact of your weapon hitting a tree, the ground, a shield etc. causes it to break. It is now useless. (For magical weapons roll an additional d10, on a 1 they break).

2. Pulled Muscle (Arms). Roll a Constitution Saving Throw DC15 or the strain of your attack causes you to pull a muscle in your upper body. You have disadvantage in attack rolls and ability checks requiring upper body strength until you have completed three long rests, or received magical healing.

3-4. Slip Up. You lose your footing. Roll Dexterity / Acrobatics (DC15) or fall prone. Your turn has ended and melee attacks have advantage on you (see p292 of PH for conditions of being prone).

5-9. Ooops! You hit an unintended random target. Randomise all combatants within 10 feet (for a short range attack, or 30 feet for a long range attack) and roll a second attack roll, if you beat their armour class roll damage as if they were your intended target (discount sneak attack damage for Rogues).

10. WTF? You launch a comically bad projectile attack nowhere near your intended opponent – it flies into a huge empty space (or at DM’s discretion a distant unintended target) taking your self confidence with it. Roll wisdom saving throw DC15, or suffer disadvantage to attack rolls until you next score a hit on an opponent.

Critical Fumbles for High Level Characters. Once your PCs have two or three attacks a round, they might start rolling an incongruous number of fumbles, especially for heroes of their ability. Whilst being a higher level should also make passing some saving throws / skills checks easier, as well as reduce the chance of weapon breaks (as most high level characters fight with magical weapons), if you feel it’s necessary you could bring in a new rule. Starting at Level 5 you could give them a fumble saving throw where if they roll their level or below on a d20 they suffer no adverse effects. That way extremely high level characters will rarely fumble. Or you could rule that only if they roll a 1 on their first attack of their round do they have to consult this table. Rolling a 1 on any other attack and it’s just an automatic miss.

Like this? I’ve got a few other homebrew rules that you might like as well. If you have a chance to play test any of them do let me know in the comments. Would love to hear from you…

Update, what happens when a monster with natural weapons, such as bite, claw or tail attack, rolls a 1? Here we go….

Critical Misses Table (Natural Weapons)
Roll a d10.

1-2. Ouch! The attacker snaps one or several teeth / claws on its target’s weapon or armour, or nearby surface. They receive 1d3hp of damage, and furthermore they must subtract the result of the same d3 roll from damage done from this attack from now on. (Ignore for tail attacks).

3-5. Wild Swing. The attacker overextends itself going for the kill. Their intended target gains advantage on their next attack roll.

6-7. Slip Up. The attacker loses its footing. Roll Dexterity / Acrobatics check (DC15) or fall prone. Their turn has ended and melee attacks have advantage on you (see p292 of PH for conditions of being prone). Creatures with more than two legs are immune to this effect.

8-10. Loss of Nerve. The attacker is scared. They must make a Wisdom Saving Throw with a base DC of 10 modified by +2 for every hit dice higher the target of the attack has vs. the attacker (or -2 for every hit dice less). On a fail they are frightened (see p292 of Player’s Handbook). After one turn they can attempt the saving throw again. Creatures that inspire fear are immune to this effect (unless their target also inspires fear).

'''

