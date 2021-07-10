import random
from utils import append_list_as_row as csv_append
# http://fexlabs.com/dump/PHB_5E.pdf

# TODO: physical characteristics +feature
# TODO: spells +feature
# TODO: subclasses +feature
# TODO: inventory +feature
# TODO: proficiency bonus +feature
# TODO: armor class +feature
# TODO: initiative +feature
# TODO: saving throws +feature
# TODO: skill profficiencies +feature
# TODO: passive senses +feature
# TODO: hit dice +feature
# TODO features and traits +feature

exp = 0
level = 1
cap = {
    1: 300,
    2: 900,
    3: 2700,
    4: 6500,
    5: 14000,
    6: 23000,
    7: 34000,
    8: 48000,
    9: 64000,
    10: 85000,
    11: 100000,
    12: 120000,
    13: 140000,
    14: 165000,
    15: 195000,
    16: 225000,
    17: 265000,
    18: 305000,
    19: 355000
}
def level_up(prev):
    level = prev+1
    

def gain_experience(level, exp, gained):
    current = exp+gained
    if current >= cap[level]:
        level_up(level)
    return exp+gained

classes = [
    "Barbarian", "Bard", "Cleric",
    "Druid", "Fighter", "Monk",
    "Paladin", "Ranger", "Rogue",
    "Sorcerer", "Warlock", "Wizard"
]
races   = [
    "Dragonborn", "Hill Dwarf", "Mountain Dwarf",
    "Dark Elf", "High Elf", "Wood Elf",
    "Gnome", "Halfling", "Half-Elf",
    "Half-Orc", "Human", "Tiefling",
]
backgrounds = [
    "Acolyte", "Criminal", "Charlatan", "Entertainer",
    "Folk Hero", "Guild Artisan", "Hermit", "Noble",
    "Outlander", "Sage", "Sailor", "Soldier", "Urchin"
]
languages = [
    # std
    "Common", "Dwarvish", "Elvish", "Giant",
    "Gnomish", "Goblin", "Halfling", "Orc",
    # exotic
    "Abyssal", "Celestial", "Draconic", "Deep Speech",
    "Infernal", "Primordial", "Sylvan", "Undercommon"
]
class_languages = ["Druidic", "Thieves' Cant"]
allignments = [
    "Lawful Good", "Neutral Good", "Chaotic Good",
    "Lawful Neutral", "True Neutral", "Chaotic Neutral",
    "Lawful Evil", "Neutral Evil", "Chaotic Evil"
]
personality_traits = {
    "Acolyte": [
        "(1) I idolize a particular hero of my faith, and constantly refer to that person's deeds and example.",
        "(2) I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.",
        "(3) I see omens in every event and action. The gods try to speak to us, we just need to listen.",
        "(4) Nothing can shake my optimistic attitude.",
        "(5) I quote (or misquote) sacred texts and proverbs in almost every situation",
        "(6) I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.",
        "(7) I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me.",
        "(8) I've spent so long in the temple that I have little practical experience dealing with people in the outside world.",
    ],
    "Charlatan": [
        "(1) I fall in and out of love easily, and am always pursuing someone.",
        "(2) I have a joke for every occasion, especially occasions where humor is inappropriate.",
        "(3) Flattery is my preferred trick for getting what I want.",
        "(4) I'm a born gambler who can't resist taking a risk for a potential payoff.",
        "(5) I lie about almost everything, even when there' no good reason to.",
        "(6) Sarcasm and insults are my weapons of random.choice.",
        "(7) I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.",
        "(8) I pocket anything I see that might have some value.",
    ],
    "Criminal": [
        "(1) I always have a plan for what to do when things go wrong.",
        "(2) I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
        "(3) The first thing I do in a new place is note the locations of everything valuable -- or where such things could be hidden.",
        "(4) I would rather make a new friend then a new enemy.",
        "(5) I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
        "(6) I don't pay attention to the risks in a situation. Never tell me the odds.",
        "(7) The best way to get me to do something is to tell me I can't do it.",
        "(8) I blow up at the slightest insult.",
    ],
    "Entertainer": [
        "(1) I know a story relevant to almost every situation.",
        "(2) Whenever I Come to a new place, I collect local rumors and spread gossip.",
        "(3) I'm a hopeless romantic, always searching for that 'special someone.",
        "(4) Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
        "(5) I love a good insult, even one direct at me.",
        "(6) I get bitter if I'm not the center of attention.",
        "(7) I'll settle for nothing less than perfection.",
        "(8) I change  my mood or my mind as quickly as I change key in a song.",
    ],
    "Folk Hero": [
        "(1) I judge people by their actions, not their words.",
        "(2) If someone is in trouble, I'm always ready to lend help.",
        "(3) When I set my mind to something, I follow through no matter what gets in my way.",
        "(4) I have a strong sense of fair play and always try to find the most equitable solution to arguments.",
        "(5) I'm confident in my own abilities and do what I can to instill confidence in others.",
        "(6) Thinking is for other people. I prefer action.",
        "(7) I misuse long words in an attempt to sound smarter.",
        "(8) I get bored easily. When am I going to get on with my destiny?",
    ],
    "Guild Artisan": [
        "(1) I believe that anything worth doing is worth doing right. I can't help it -- I'm a perfectionist.",
        "(2) I'm a snob who looks down on those who can't appreciate fine art.",
        "(3) I always want to know how things work and what makes people tick.",
        "(4) I'm full of witty aphorisms and have a proverb for every occasion.",
        "(5) I'm rude to people who lack my commitment to hard work and fair play.",
        "(6) I like to talk at length about my profession.",
        "(7) I don't part with my money easily and will haggle tirelessly to get the best deal possible.",
        "(8) I'm well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when people haven't heard of me.",
    ],
    "Hermit": [
        "(1) I've been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.",
        "(2) I am utterly serene, even in the face of disaster.",
        "(3) The leader of my community had something wise to say on every topic, and I am eager to share that wisdom",
        "(4) I feel tremendous empathy for all who suffer.",
        "(5) I'm oblivious to etiquette and social expectations.",
        "(6) I connect everything that happens to me to a grand cosmic plan.",
        "(7) I often get lost in my own thought and contemplation, becoming oblivious to my surroundings.",
        "(8) I am working on a grand philosophical theory and love sharing my ideas.",
    ],
    "Noble": [
        "(1) My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
        "(2) The common folk love me for my kindness and generosity.",
        "(3) No one could doubt by looking at my regal bearing that I am cut above the unwashed masses.",
        "(4) I take great pains to always look my best and follow the latest fashions.",
        "(5) I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations.",
        "(6) Despite my noble birth, I do not place myself above other folk. We all have the same blood.",
        "(7) My favor, once lost, is lost forever.",
        "(8) If you do me injury, I will crush you, ruin your name, and salt your fields.",
    ],
    "Outlander": [
        "(1) I'm driven by a wanderlust that led me away from home.",
        "(2) I watch over my friends as if they were a litter of newborn pups.",
        "(3) I once ran twenty-five miles without stopping to warn to my clan of an approaching monster horde. I'd do it again if I had to.",
        "(4) I have a lesson for every situation, drawn from observing nature.",
        "(5) I place no stock in wealthy or well-mannered folk. Money and manners won't save you from a hungry owlbear.",
        "(6) I'm always picking things up, absently fiddling with them, and sometimes accidentally breaking them.",
        "(7) I feel far more comfortable around animals than people.",
        "(8) I was, in fact, raised by wolves.",
    ],
    "Sage": [
        "(1) I use polysyllabic words that convey the impression of great erudition.",
        "(2) I've read every book in the world's greatest libraries -- or I like to boast that I have.",
        "(3) I'm used  to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others.",
        "(4) There's nothing I like more than a good mystery.",
        "(5) I'm willing to listen to every side of an argument before I make my own judgment.",
        "(6) I ... speak ... slowly ... when talking ... to idiots ... which ... almost ... everyone ... is ... compared ... to me.",
        "(7) I am horribly, horribly awkward in social situations.",
        "(8) I'm convinced that people are always trying to steal my secrets.",
    ],
    "Sailor": [
        "(1) My friends know they can rely on me, no matter what.",
        "(2) I work hard so that I can play hard when the work is done.",
        "(3) I enjoy sailing into new ports and making new friends over a flagon of ale.",
        "(4) I stretch the truth for the sake of a good story.",
        "(5) To me, a tavern brawl is a nice way to get to know a new city.",
        "(6) I never pass up a friendly wager.",
        "(7) My language is as foul as an otyugh nest.",
        "(8) I like a job well done, especially if I can convince someone else to do it.",
    ],
    "Soldier": [
        "(1) I'm always polite and respectful",
        "(2) I'm haunted by memories of war. I can't get the images of violence out of my mind.",
        "(3) I've lost too many friends, and I'm slow to make new ones.",
        "(4) I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
        "(5) I can stare down a hell hound without flinching.",
        "(6) I enjoy being strong and like breaking things.",
        "(7) I have a crude sense of humor.",
        "(8) I face problems head-on. A simple, direct solution is the best path to success.",
    ],
    "Urchin": [
        "(1) I hide scraps of food and trinkets away in my pockets.",
        "(2) I ask a lot of questions.",
        "(3) I like to squeeze into small places where no one else can get to me.",
        "(4) I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms.",
        "(5) I eat like a pig and have bad manners.",
        "(6) I think anyone who's nice to me is hiding evil intent.",
        "(7) I don't like to bathe.",
        "(8) I bluntly say what other people are hinting at or hiding.",
    ],
}
ideals = {
    "Acolyte": [
        "(1) Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld (Lawful)",
        "(2) Charity. I always try to help those in need, no matter what the personal cost. (Good)",
        "(3) Change. We must help bring about the changes the gods are constantly working in the world(s). (Chaotic)",
        "(4) Power. I hope to one day rise to the top of my faith's religious hierarchy. (Lawful)",
        "(5) Faith. I trust that my deity will guide my actions. I have faith that if I work hard, things will go well (Lawful)",
        "(6) Aspiration. I seek to prove myself worthy of my god's favor by matching my actions against his or her teachings (Any)",
    ],
    "Charlatan": [
        "(1) Independence. I am a free spirit -- no one tells me what to do. (Chaotic)",
        "(2) Fairness. I never target people who can't afford to lose a few coins. (Lawful)",
        "(3) Charity. I distribute the money I acquire to the people who really need it. (Good)",
        "(4) Creativity. I never run the same con twice. (Chaotic)",
        "(5) Friendship. Material goods come and go. Bonds of friendship last forever. (Good)",
        "(6) Aspiration. I'm determined to make something of myself. (Any)",
    ],
    "Criminal": [
        "(1) Honor. I don't steal from others in the trade. (Lawful)",
        "(2) Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic)",
        "(3) Charity. I steal from the wealthy so that I can help people in need. (Good)",
        "(4) Greed. I will do whatever it takes to become wealthy. (Evil)",
        "(5) People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care. (Neutral)",
        "(6) Redemption. There's a spark of good in everyone. (Good)",
    ],
    "Entertainer": [
        "(1) Beauty. When I perform, I make the world better than it was. (Good)",
        "(2) Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are. (Lawful)",
        "(3) Creativity. The world is in need of new ideas and bold action. (Chaotic)",
        "(4) Greed. I'm only in it for the money and fame. (Evil)",
        "(5) People. I like seeing the smiles on people's faces when I perform. That's all that matters. (Neutral)",
        "(6) Honesty. Art should reflect the soul; it should come from within and reveal who we really are. (Any)",
    ],
    "Folk Hero": [
        "(1) Respect. People deserve to be treated with dignity and respect. (Good)",
        "(2) Fairness. No one should get preferential treatment before the law, and no one is above the law. (Lawful)",
        "(3) Freedom. Tyrants must not be allowed to oppress the people. (Chaotic)",
        "(4) Might. If I become strong, I can take what I want -- what I deserve. (Evil)",
        "(5) Sincerity. There's no good in pretending to be something I'm not (Neutral)",
        "(6) Destiny. Nothing and no one can steer me away from my higher calling. (Any)",
    ],
    "Guild Artisan": [
        "(1) Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization. (Lawful)",
        "(2) Generosity. My talents were given to me so that I could use them to benefit the world. (Good)",
        "(3) Freedom. Everyone should be free to pursue his or her own livelihood. (Chaotic)",
        "(4) Greed. I'm only in it for the money. (Evil)",
        "(5) People. I'm committed to the people I care about, not to ideals. (Neutral)",
        "(6) Aspiration. I work hard to be the best there is at my craft.",
    ],
    "Hermit": [
        "(1) Greater Good. My gifts are meant to be shared with all, not used for my own benefit. (Good)",
        "(2) Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking. (Lawful)",
        "(3) Free Thinking. Inquiry and curiosity are the pillars of progress. (Chaotic)",
        "(4) Power. Solitude and contemplation are paths toward mystical or magical power. (Evil)",
        "(5) Live and Let Live. Meddling in the affairs of others only causes trouble (Neutral)",
        "(6) Self-Knowledge. If you know yourself, there's nothing left to know (Any)",
    ],
    "Noble": [
        "(1) Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity. (Good)",
        "(2) Responsibility. It is my duty to respect the authority of those above me, just as those below me must respect mine. (Lawful)",
        "(3) Independence. I must prove that I can handle myself without the coddling of my family. (Chaotic)",
        "(4) Power. If I can attain more power, no one will tell me what to do. (Evil)",
        "(5) Family. Blood runs thicker than water. (Any)",
        "(6) Noble Obligation. It is my duty to protect and care for the people beneath me. (Good)",
    ],
    "Outlander": [
        "(1) Change. Life is like the seasons, in constant change, and we must change with it. (Chaotic)",
        "(2) Greater Good. it is each person's responsibility to make the most happiness for the whole tribe. (Good)",
        "(3) Honor. if I dishonor myself, I dishonor my whole clan. (Lawful)",
        "(4) Might. The strongest are meant to rule. (Evil)",
        "(5) Nature. The natural world is more important than all the constructs of civilization. (Neutral)",
        "(6) Glory. I must earn glory in battle, for myself and my clan. (Any)",
    ],
    "Sage": [
        "(1) Knowledge. The path to power and self-improvement is through knowledge. (Neutral)",
        "(2) Beauty. What is beautiful points us beyond itself toward what is true. (Good)",
        "(3) Logic. Emotions must not cloud our logical thinking. (Lawful)",
        "(4) No limits. Nothing should fetter the infinite possibility inherent in all existence. (Chaotic)",
        "(5) Power. Knowledge is the path to power and domination. (evil)",
        "(6) Self-Improvement. The goal of a life of study is the betterment of oneself. (Any)",
    ],
    "Sailor": [
        "(1) Respect. The thing that keeps a ship together is mutual respect between captain and crew. (Good)",
        "(2) Fairness. We all do the work, so we all share in the rewards. (Lawful)",
        "(3) Freedom. The sea is freedom -- the freedom to go anywhere and do anything. (Chaotic)",
        "(4) Mastery. I'm a predator, and the other ships on the sea or in the sky are my prey. (Evil)",
        "(5) People. I'm committed to my crewmates, not to ideals. (Neutral)",
        "(6) Aspiration. Someday I'll own my own ship and chart my own destiny. (Any)",
    ],
    "Soldier": [
        "(1) Greater Good. Our lot is to lay down our lives in defense of others. (Good)",
        "(2) Responsibility. I do what I must and obey just authority. (Lawful)",
        "(3) Independence. When people follow orders blindly, they embraces a kind of tyranny. (Chaotic)",
        "(4) Might. In life as in war, the stronger force wins. (Evil)",
        "(5) Live and Let Live. Ideals aren't worth killing over or going to war for. (Neutral)",
        "(6) Nation. My city, nation, or people are all that matter. (Any)",
    ],
    "Urchin": [
        "(1) Respect. All people, rich or poor, deserve respect. (Good)",
        "(2) Community. We have to take care of each other, because no one else is going to do it. (Lawful)",
        "(3) Change. The low are lifted up, and the high and mighty are brought down. Change is the nature of things. (Chaotic)",
        "(4) Retribution. The rich need to be shown what life and death are like in the gutters (Evil)",
        "(5) People. I help the people who help me -- that's what keeps us alive. (Neutral)",
        "(6) Aspiration. I'm going to prove that I'm worthy of a better life. (Any)",
    ],
}
bonds = {
    "Acolyte": [
        "(1) I would die to recover an ancient relic of my faith that was lost long ago.",
        "(2) I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
        "(3) I owe my life to the priest who took me in when my parents died.",
        "(4) Everything I do is for the common people.",
        "(5) I will do anything to protect the temple where I served.",
        "(6) I seek to preserve  sacred text that my enemies consider heretical and seek to destroy.",
    ],
    "Charlatan": [
        "(1) I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.",
        "(2) I owe everything to my mentor -- a horrible person who's probably rotting in jail somewhere.",
        "(3) Somewhere out there, I have a child who doesn't know me. I'm making the world better for him or her.",
        "(4) I come from a noble family, and one day I'll reclaim my lands and title from those who stole them from me.",
        "(5) A powerful person killed someone I love. Some day soon, I'll have my revenge.",
        "(6) I swindled and ruined a person who didn't deserve it. I seek to atone for my misdeeds but might never be able to forgive myself.",
    ],
    "Criminal": [
        "(1) I'm trying to pay off an old debt I owe to a generous benefactor.",
        "(2) My ill-gotten gains go to support my family.",
        "(3) Something important was taken from me, and I aim to steal it back.",
        "(4) I will become the greatest thief that ever lived.",
        "(5) I'm guilty of a terrible crime. I hope I can redeem myself for it.",
        "(6) Someone I loved died because of one mistake I made. That will never happen again.",
    ],
    "Entertainer": [
        "(1) My instrument is my most treasured possession, and it reminds me of someone I love.",
        "(2) Someone stole my precious instrument, and someday I'll get it back.",
        "(3) I want to be famous, whatever it takes.",
        "(4) I idolize a hero of the old tales and measure my deeds against that person's.",
        "(5) I will do anything to prove myself superior to my hated rival.",
        "(6) I would do anything to prove for the other members of my old troupe.",
    ],
    "Folk Hero": [
        "(1) I have a family, but I have no idea where they are one day, I hope to see them again.",
        "(2) I worked the land, I love the land, and I will protect the land.",
        "(3) A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
        "(4) My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
        "(5) I protect those who cannot protect themselves.",
        "(6) I wish my childhood sweetheart had come with me to pursue my destiny.",
    ],
    "Guild Artisan": [
        "(1) The workshop where I learned my trade is the most important place in the world to me.",
        "(2) I created a great work for someone, and then found them unworthy to receive it. I'm still looking for someone worthy",
        "(3) I owe my guild a great debt for forging me into the person I am today.",
        "(4) I pursue wealth to secure someone's love.",
        "(5) One day I will return to my guild and prove that I am the greatest artisan of them all.",
        "(6) I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood.",
    ],
    "Hermit": [
        "(1) Nothing is more important than the other members of my hermitage, order, or association.",
        "(2) I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.",
        "(3) I'm still seeking the enlightenment I pursued in my seclusion, and it still eludes me.",
        "(4) I entered seclusion because I loved someone I could not have.",
        "(5) Should my discovery come to light, it could bring ruin to the world.",
        "(6) My isolation gave me great insight into a great evil that only I can destroy.",
    ],
    "Noble": [
        "(1) I will face any challenge to win the approval of my family.",
        "(2) My house's alliance with another noble family must be sustained at all costs.",
        "(3) Nothing is more important than the other members of my family.",
        "(4) I am in love with the heir of a family that my family despises.",
        "(5) My loyalty to my sovereign is unwavering.",
        "(6) The common folk must see me as a hero of the people.",
    ],
    "Outlander": [
        "(1) My family, clan, or tribe is the most important thing in my life, even when they are far from me.",
        "(2) An injury to the unspoiled wilderness of my home is an injury to me.",
        "(3) I will bring terrible wrath down on the evildoers who destroyed my homeland.",
        "(4) I am the last of my tribe, and it is up to me to ensure their names enter legend.",
        "(5) I suffer awful visions of a coming disaster and will do anything to prevent it.",
        "(6) It is my duty to provide children to sustain my tribe.",
    ],
    "Sage": [
        "(1) It is my duty to protect my students.",
        "(2) I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
        "(3) I work to preserve a library, university, scriptorium, or monastery.",
        "(4) My life's work is a series of tomes related to a specific field of lore.",
        "(5) I've been searching my whole life for the answer to a certain question.",
        "(6) I sold my soul for knowledge. I hope to do great deeds and win it back.",
    ],
    "Sailor": [
        "(1) I'm loyal to my captain first, everything else second.",
        "(2) The ship is most important -- crewmates and captains come and go.",
        "(3) I'll always remember my first ship.",
        "(4) In a harbor town, I have a paramour whose eyes nearly stole me from the sea.",
        "(5) I was cheated out of my fair share of the profits, and I want to get my due.",
        "(6) Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine.",
    ],
    "Soldier": [
        "(1) I would still lay down my life for the people I served with.",
        "(2) Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
        "(3) My honor is my life.",
        "(4) I'll never forget the crushing defeat my company suffered or the enemies who dealt it.",
        "(5) Those who fight beside me are those worth dying for.",
        "(6) I fight for those who cannot fight for themselves.",
    ],
    "Urchin": [
        "(1) My town or city is my home, and I'll fight to defend it.",
        "(2) I sponsor an orphanage to keep others from enduring what I was forced to endure.",
        "(3)  I owe my survival to another urchin who taught me to live on the streets.",
        "(4) I owe a debt I can never repay to the person who took pity on me.",
        "(5) I escaped my life of poverty by robbing an important person, and I'm wanted for it.",
        "(6) No one else should have to endure the hardships I've been through.",
    ],
}
flaws = {
    "Acolyte": [
        "(1) I judge others harshly, and myself even more severely.",
        "(2) I put too much trust in those who wield power within my temple's hierarchy.",
        "(3) My piety sometimes leads me to blindly trust those that profess faith in my god.",
        "(4) I am inflexible in my thinking.",
        "(5) I am suspicious of strangers and expect the worst of them.",
        "(6) Once I pick a goal. I become obsessed with it to the detriment of everything else in my life.",
    ],
    "Charlatan": [
        "(1) I can't resist a pretty face.",
        "(2) I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
        "(2) I'm convinced that no one could ever fool me the why I fool others.",
        "(4) I'm too greedy for my own good. I can't resist taking a risk if there's money involved.",
        "(5) I can't resist swindling people who are more powerful than me.",
        "(6) I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough.",
    ],
    "Criminal": [
        "(1) When I see something valuable, I can't think about anything but how to steal it.",
        "(2) When faced with a random.choice between money and my friends, I usually choose the money.",
        "(3) If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
        "(4) I have a 'tell' that reveals when I'm lying.",
        "(5) I turn tail and run when things look bad.",
        "(6) An innocent person is in prison for a crime that I committed. I'm okay with that."
    ],
    "Entertainer": [
        "(1) I'll do anything to win fame and renown.",
        "(2) I'm a sucker for a pretty face.",
        "(3) A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
        "(4) I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
        "(5) I have trouble keeping my true feelings hidden/. My sharp tongue lands me in trouble.",
        "(6) Despite my best efforts, I am unreliable to my friends.",
    ],
    "Folk Hero": [
        "(1) The tyrant who rules my land will stop at nothing to see me killed.",
        "(2) I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
        "(3) The people who knew me when I was younger know my shameful secret, so I can never go home again.",
        "(4) I have a weakness for the vices of the city, especially hard drink.",
        "(5) Secretly, I believe that things would be better if I were a tyrant lording over the land.",
        "(6) I have trouble trusting in my allies.",
    ],
    "Guild Artisan": [
        "(1) I'll do anything to get my hands on something rare or priceless.",
        "(2) I'm quick to assume that someone is trying to cheat me.",
        "(3) No one must ever learn that I once stole money from guild coffers.",
        "(4) I'm never satisfied with what I have -- I always want more.",
        "(5) I would kill to acquire a noble title.",
        "(6) I'm horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I'm surrounded by rivals.",
    ],
    "Hermit": [
        "(1) Now that I've returned to the world, I enjoy its delights a little too much.",
        "(2) I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.",
        "(3) I am dogmatic in my thoughts and philosophy.",
        "(4) I let my need to win arguments overshadow friendships and harmony.",
        "(5) I'd risk too much to uncover a lost bit of knowledge.",
        "(6) I like keeping secrets and won't share them with anyone.",
    ],
    "Noble": [
        "(1) I secretly believe that everyone is beneath me.",
        "(2) I hide a truly scandalous secret that could ruin my family forever.",
        "(3) I too often hear veiled insults and threats in every word addressed to me, and I'm quick to anger.",
        "(4) I have an insatiable desire for carnal pleasures.",
        "(5) In fact, the world does revolve around me.",
        "(6) By my words and actions, I often bring shame to my family."
    ],
    "Outlander": [
        "(1) I am too enamored of ale, wine, and other intoxicants.",
        "(2) There's no room for caution in a life lived to the fullest.",
        "(3) I remember every insult I've received and nurse a silent resentment toward anyone who's ever wronged me.",
        "(4) I am slow to trust members of other races, tribes, and societies.",
        "(5) Violence is my answer to almost any challenge.",
        "(6) Don't expect me to save those who can't save themselves. It is nature's way that the strong thrive and the weak perish.",
    ],
    "Sage": [
        "(1) I am easily distracted by the promise of information.",
        "(2) Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
        "(3) Unlocking an ancient mystery is worth the price of a civilization.",
        "(4) I overlook obvious solutions in favor of complicated ones.",
        "(5) I speak without really thinking through my words, invariably insulting others.",
        "(6) I can't keep a secret to save my life, or anyone else's.",
    ],
    "Sailor": [
        "(1) I follow orders, even if I think they're wrong.",
        "(2) I'll say anything to avoid having to do extra work.",
        "(3) Once someone questions my courage, I never back down no matter how dangerous the situation.",
        "(4) Once I start drinking, it's hard for me to stop.",
        "(5) I can't help but pocket loose coins and other trinkets I come across.",
        "(6) My pride will probably lead to my destruction.",
    ],
    "Soldier": [
        "(1) The monstrous enemy we faced in battle still leaves me quivering with fear.",
        "(2) I have little respect for anyone who is not a proven warrior.",
        "(3) I made a terrible mistake in battle cost many lives -- and I would do anything to keep that mistake secret.",
        "(4) My hatred of my enemies is blind and unreasoning.",
        "(5) I obey the law, even if the law causes misery.",
        "(6) I'd rather eat my armor than admit when I'm wrong.",
    ],
    "Urchin": [
        "(1) If I'm outnumbered, I will run away from a fight.",
        "(2) Gold seems like a lot of money to me, and I'll do just about anything for more of it.",
        "(3) I  will never fully trust anyone other than myself.",
        "(4) I'd rather kill someone in their sleep then fight fair.",
        "(5) It's not stealing if I need it more than someone else.",
        "(6) People who can't take care of themselves get what they deserve."
    ],
}
bonus_things = {
    "Charlatan": [ # Favorite Schemes
        "(1) I cheat at games of chance.",
        "(2) I shave coins or forge documents.",
        "(3) I insinuate myself into people's lives to prey on their weakness and secure their fortunes.",
        "(4) I put on new identities like clothes.",
        "(5) I run sleight-of-hand cons on street corners.",
        "(6) I convince people that worthless junk is worth their hard-earned money.",
    ],
    "Folk Hero": [ # Defining Event
        "(1)  I stood up to a tyrant's agents.",
        "(2) I saved people during a natural disaster.",
        "(3) I stood alone against a terrible monster.",
        "(4) I stole from a corrupt merchant to help the poor.",
        "(5) I led a militia to fight off an invading army.",
        "(6) I broke into a tyrant's castle and stole weapons to arm the people.",
        "(7) I trained the peasantry to use farm implements as weapons against a tyrant's soldiers.",
        "(8) A lord rescinded an unpopular decree after I led a symbolic act of protect against it.",
        "(9) A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.",
        "(10) Recruited into the lord's army, I rose to leadership and was commended for my heroism.",
    ],
    "Criminal": [ # Criminal Specialty
        "(1) Blackmailer",
        "(2) Burglar",
        "(3) Enforcer",
        "(4) Fence",
        "(5) Highway robber",
        "(6) Hired Killer",
        "(7) Pickpocket",
        "(8) Smuggler",
    ],
    "Entertainer": [ # Entertainer Routines
        "(1) Actor",
        "(2) Dancer",
        "(3) Fire-eater",
        "(4) Jester",
        "(5) Juggler",
        "(6) Instrumentalist",
        "(7) Poet",
        "(8) Singer",
        "(9) Storyteller",
        "(10) Tumbler",
    ],
    "Guild Artisan": [ # Guild Business
        "(1) Alchemists and apothecaries",
        "(2) Armorers, locksmiths, and finesmiths",
        "(3) Brewers, distillers, and vintners",
        "(4) Calligraphers, scribes, and scriveners",
        "(5) Carpenters, roofers, and plasterers",
        "(6) Cartographers, surveyors, and chart0makers",
        "(7) Cobblers and shoemakers",
        "(8) Cooks and bakers",
        "(9) Glassblowers and glaziers",
        "(10) Jewelers and gemcutters",
        "(11) Leatherworkers, skinners, and tanners",
        "(12) Masons and stonecutters",
        "(13) Painters, limners, and sign-makers",
        "(14) Potters and tile-makers",
        "(15) Shipwrights and sailmakers",
        "(16) Smiths and metal-forgers",
        "(17) Tinkers, pewterers, and casters",
        "(18) Wagon-makers and wheelwrights",
        "(19) Weavers and dyers",
        "(20) Woodcarvers, coopers, and bowyers",
    ],
    "Hermit": [ # Life of Seclusion
        "(1) I was searching for spiritual enlightenment.",
        "(2) I was partaking of communal living in accordance with the dictates of a religious order.",
        "(3) I was exiled for a crime I didn't commit.",
        "(4) I retreated from society after a life-altering event.",
        "(5) I needed a quiet place to work on my art, literature, music, or manifesto.",
        "(6) I needed to commune with nature, far from civilization.",
        "(7) IU was the caretaker of an ancient ruin or relic.",
        "(8) I was a pilgrim in search of a person, place, or relic of spiritual significance.",
    ],
    "Outlander": [ # Origin
        "(1) Forester",
        "(2) Trapper",
        "(3) Homesteader",
        "(4) Guide",
        "(5) Exile or outcast",
        "(6) Bounty hunter",
        "(7) Pilgrim",
        "(8) Tribal nomad",
        "(9) Hunter-gatherer",
        "(10) Tribal marauder",
    ],
    "Sage": [ # Specialty
        "(1) Alchemist",
        "(2) Astronomer",
        "(3) Discredited Academic",
        "(4) Librarian",
        "(5) Professor",
        "(6) Researcher",
        "(7) Wizard's Apprentice",
        "(8) Scribe",
    ],
    "Soldier": [ # Specialty
        "(1) Officer",
        "(2) Scout",
        "(3) Infantry",
        "(4) Cavalry",
        "(5) Healer",
        "(6) Quartermaster",
        "(7) Standard bearer",
        "(8) Support staff (cook, blacksmith, or the like...)",
    ],
}
variants = {
    "Variant Criminal: Spy": [
        "Although your capabilities are not much different from those of a burglar or smuggler, you learned and practiced them in a very different context; as an espionage agent. You might have been an officially sanctioned agent of the crown, or perhaps you sold the secrets you uncovered to the highest bidder.",
    ],
    "Variant Entertainer: Gladiator": [
        "A gladiator is as much an entertainer as any minstrel or circus performer, trained to make the arts of combat into a spectacle the crowd can enjoy. This kind of flashy combat is your entertainer routine, though you might also have some skills as a tumbler or actor. Using your By Popular Demand feature, you can find a place to perform in any place that features combat for entertainment -- perhaps a  gladiatorial arena or secret pit fighting club. You can replace the musical instrument in your equipment package with an inexpensive but unusual weapon, such as a trident or net.",
    ],
    "Variant Guild Artisan: Guild Merchant": [
        "Instead of an artisans' guild, you might belong to a guild of traders, caravan masters, or shopkeepers. You don't craft items yourself but earn a living by buying and selling the works of others (or raw materials artisans need to practice their craft.) Your guild might be a large merchant consortium (or family) with interests across the region (or worlds). Perhaps you transported goods from one place to another, by ship, wagon, or caravan, or bought them from traveling traders and sold them in your own little shop. In some ways, the traveling merchant's life lends itself to adventure far more than the life of an artisan. Rather than proficiency with artisan's tools, you might be proficient with navigator's tools or an additional language. And instead of artisan's tools, you can start with a mule and a cart.",
    ],
    "Other Hermits": [
        "This hermit background assumes a contemplative sort of seclusion that allows room for study and prayer. If you want to play a rugged wilderness recluse who lives off the land while shunning the company of other people, look at the outlander background. On the other hand, if you want to go in a more religious direction, the acolyte might be what you're looking for. Or you could even be a charlatan, posing as a wise and holy person and letting pious fools support you.",
    ],
    "Variant Noble: Knight": [
        "A knighthood is among the lowest noble titles in most societies, but is can be a path to higher status. If you wish to be a knight, choose the Retainers feature instead of the Position of Privilege feature. One of your commoner retainers is replaced by a noble who serves as your squire, aiding you in exchange for training on his or her own path to knighthood. Your two remaining retainers might include a groom to care for your horse and a servant who polishes your armor (and even helps you put it on). As an emblem of chivalry and the ideals of courtly love, you might include among your equipment a banner or other token from a noble lord or lady to whom you have given your heart -- in a chaste sort of devotion (This person could be your bond.)",
    ],
    "Variant Sailor: Pirate": [
        "You spent your youth under the sway of a dread pirate, a ruthless cutthroat who taught you how to survive in a world of sharks and savages. You've indulged in larceny on the high seas and blue skies and sent more than one deserving soul to an early grave. Fear and bloodshed are no strangers to you, and you've garnered a somewhat unsavory reputation in many a port town. If you decide that your sailing career involved piracy you can choose the Bad Reputation feature instead of the Ship's Passage feature.",
    ],
}

inventory = {
    
}


def convert(conversion, value):
    conversions = {
        'ptg': (value//10, value %10),
        'pte': (value//20, value % 20),
        'pts': (value//100, value % 100),
        'ptc': (value//1000, value % 1000),

        'gtp': (value*10),
        'gte': (value//2, value % 2),
        'gts': (value//10, value % 10),
        'gtc': (value//100, value % 100),

        'etp': (value//20, value % 20),
        'etg': (value//2, value % 2),
        'ets': (value//5, value % 5),
        'etc': (value//50, value % 50),

        'stp': (value*100),
        'stg': (value*10),
        'ste': (value//5, value % 5),
        'stc': (value//10, value % 10),

        'ctp': (value*1000),
        'ctg': (value*100),
        'cte': (value*50),
        'cts': (value*10),
    }

    return conversions[conversion]


def determine_languages(bg, race):
    langs = []
    def race_langs(race, langs): 
        if race == races[0]: # Dragonborn 	 Common, Draconic
            langs.extend([languages[0], languages[10]])
        elif race == races[1]: # Hill Dwarf	  	 Common, Dwarvish
            langs.extend([languages[0], languages[1]])
        elif race == races[2]: # Mountain Dwarf	 Common, Dwarvish
            langs.extend([languages[0], languages[1]])
        elif race == races[3]: # Drow 	         Common, Elvish
            langs.extend([languages[0], languages[2]])
        elif race == races[4]: # High Elf 	     Common, Elvish
            langs.extend([languages[0], languages[2]])
        elif race == races[5]: # Wood Elf 	     Common, Elvish
            langs.extend([languages[0], languages[2]])
        elif race == races[6]: # Gnome   	     Common, Gnomish
            langs.extend([languages[0], languages[4]])
        elif race == races[7]: # Halfling 	     Common, Halfling
            langs.extend([languages[0], languages[6]])
        elif race == races[8]: # Half-Elf 	     Common, Elvish
            langs.extend([languages[0], languages[2]])
        elif race == races[9]: # Half-Orc 	     Common, Orc
            langs.extend([languages[0], languages[7]])
        elif race == races[10]: # Human 	         Common, 1 Additional
            langs.extend([languages[0], languages[random.randint(1, 15)]])
        elif race == races[11]: # Tiefling 	     Common, Infernal
            langs.extend([languages[0], languages[12]])
        return langs

    def background_langs(background, langs):
        if background in [backgrounds[0], backgrounds[9]]:
            # Two langs
            while 1:
                n = languages[random.randint(0, 15)]
                if n not in langs:
                    langs.append(n)
                    break
            while 1:
                m = languages[random.randint(0, 15)]
                if m not in langs and m != n:
                    langs.append(m)
                    break
        if background in [backgrounds[5], backgrounds[6], backgrounds[7], backgrounds[8]]:
            # One lang
            while 1:
                n = languages[random.randint(0, 15)]
                if n not in langs:
                    langs.append(n)
                    break
        if background in [backgrounds[1], backgrounds[2], backgrounds[3], backgrounds[4], backgrounds[10], backgrounds[11], backgrounds[12]]:
            return langs # Zero langs
        return langs
    return background_langs(bg, race_langs(race, langs))

def determine_race():
    return random.choice(races)

def determine_class():
    return random.choice(classes)

def determine_background():
    return random.choice(backgrounds)

def roll_stats():
    return [random.randint(9, 18) for i in range(0, 6)]

def determine_allignment():
    return random.choice(allignments)

def random_stats(stats):
    while 1:
        n = random.randint(1, len(stats)-1)
        if n != 5:
            stats[n] += 1
            break
    while 1:
        m = random.randint(1, len(stats)-1)
        if m != 5 and m != n:
            stats[m] += 1
            break
    return stats

def generate_sex():
    return random.choice(["Male", "Female"])

def alter_stats(stats, race):
    # str dex con int wis cha
    if race == races[0]: # Dragonborn 	     2 STR, 1 CHA
        stats[0] += 2
        stats[5] += 1
    elif race == races[1]: # Hill Dwarf	  	 2 CON, 1 WIS
        stats[2] += 2
        stats[4] += 1
    elif race == races[2]: # Mountain Dwarf	 2 CON, 2 STR
        stats[0] += 2
        stats[2] += 2
    elif race == races[3]: # Drow 	         2 DEX, 1 CHA
        stats[1] += 2
        stats[5] += 1
    elif race == races[4]: # High Elf 	     2 DEX, 1 INT
        stats[1] += 2
        stats[3] += 1
    elif race == races[5]: # Wood Elf 	     2 DEX, 1 WIS
        stats[1] += 2
        stats[4] += 1
    elif race == races[6]: # Gnome   	     2 INT
        stats[3] += 2
    elif race == races[7]: # Halfling 	     2 DEX
        stats[1] += 2
    elif race == races[8]: # Half-Elf 	     2 CHA, 1 ASI
        stats[5] += 2
        stats = random_stats(stats)
    elif race == races[9]: # Half-Orc 	     2 STR, 1 CON
        stats[0] += 2
        stats[2] += 1
    elif race == races[10]: # Human          1 to All
        stats = [stat + 1 for stat in stats]
    elif race == races[11]: # Tiefling 	     2 CHA, 1 INT
        stats[5] += 2
        stats[3] += 1
    else: raise ValueError(f'The race you entered, {race}, is currently not included.')
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
        else: raise ValueError("Your stat value is too high or too low. Cheating isn't cool.")
        mods.append(mod)
    return mods

def generate_size(race):
    if race == races[0]: # Dragonborn        66    +2d8    175 lb.   x (2d6) lb.
        mod = random.randint(2, 16)
        height = 66 + mod
        weight = 175 + mod*random.randint(2, 12)
    elif race == races[1]: # Dwarf, hill       44    +2d4    115 lb.   x (2d6) lb.
        mod = random.randint(2, 8)
        height = 44 + mod
        weight = 115 + mod*random.randint(2, 12)
    elif race == races[2]: # Dwarf, mountain   48    +2d4    130 lb.   x (2d6) lb.
        mod = random.randint(2, 8)
        height = 48 + mod
        weight = 130 + mod*random.randint(2, 12)
    elif race == races[3]: # Elf, drow         53    +2d6    75 lb.    x (1d6) lb.
        mod = random.randint(2, 12)
        height = 53 + mod
        weight = 75 + mod*random.randint(2, 12)
    elif race == races[4]: # Elf, high         54    +2d10   90 lb.    x (1d4) lb.
        mod = random.randint(2, 20)
        height = 54 + mod
        weight = 90 + mod*random.randint(2, 8)
    elif race == races[5]: # Elf, wood         54    +2d10   100 lb.   x (1d4) lb.
        mod = random.randint(2, 20)
        height = 54 + mod
        weight = 100 + mod*random.randint(2, 8)
    elif race == races[6]: # Gnome             35    +2d4    35 lb.    x 1 lb.
        mod = random.randint(2, 8)
        height = 35 + mod
        weight = 35 + mod*1
    elif race == races[7]: # Halfling          31    +2d4    35 lb.    x 1 lb.
        mod = random.randint(2, 8)
        height = 31 + mod
        weight = 35 + mod*1
    elif race == races[8]: # Half-elf          57    +2d8    110 lb.   x (2d4) lb.
        mod = random.randint(2, 16)
        height = 57 + mod
        weight = 110 + mod*random.randint(2, 8)
    elif race == races[9]: # Half-orc          58    +2d10   140 lb.   x (2d6) lb.
        mod = random.randint(2, 20)
        height = 58 + mod
        weight = 140 + mod*random.randint(2, 12)
    elif race == races[10]: # Human             56    +2d10   110 lb.   x (2d4) lb.
        mod = random.randint(2, 20)
        height = 56 + mod
        weight = 110 + mod*random.randint(2, 8)
    elif race == races[11]: # Tiefling          57    +2d8    110 lb.   x (2d4) lb.
        mod = random.randint(2, 16)
        height = 57 + mod
        weight = 110 + mod*random.randint(2, 8)
    return height, weight


def get_pt(bg):
    person_info = [
        random.choice(personality_traits[bg]),
        random.choice(ideals[bg]),
        random.choice(bonds[bg]),
        random.choice(flaws[bg])
    ]
    if bg in bonus_things:
        person_info.append(random.choice(bonus_things[bg]))
    return person_info

def gen_alig(ideal):
    while True:
        alignment = random.choice(allignments)
        align = alignment.split(' ')
        if 'Any' in ideal:
            return alignment
        if align[0] in ideal or align[1] in ideal:
            return alignment

def determine_hit_dice(char_class):
    '''
    Squishy Arcane Spell Slinger	d6	Sorcerer, Wizard
    Utility Class that Can Frontline	d8	Artificer, Bard, Cleric, Druid, Monk, Rogue, Warlock
    I’m Expected to Frontline	d10	Fighter, Paladin, Ranger
    BARBARIAN!	d12	Barbarian
    '''
    if char_class in ['sorcerer', 'wizard']:
        pass

def determine_equiptment(character_class, bg):
    '''
    Acolyte	        None	                           
    Criminal	    Gaming set, Thieves Tools	       
    Charlatan	    Disguise kit, Forgery kit          
    Entertainer	    Musical instrument, Disguise kit	
    Folk Hero	    Artisan's tool, vehicles (land)	   
    Guild Artisan	Artisan's tool	                   
    Hermit	        Herbalism Kit
    Noble	        Gaming set
    Outlander	    Musical Instrument
    Sage	        Navigator's tools, vehicles
    Sailor	        Navigator's tools, vehicles (water)
    Soldier	        Gaming set, vehicles (land)	
    Urchin	        Disguise kit, Thieves’ tools'''
    if bg == backgrounds[0]:
        return []
    elif bg == backgrounds[1]:
        return ["Gaming Set", "Thieves Tools"]

def log_character(*args):
    csv_append('characters.csv', [arg for arg in args])

def create_character():
    # https://www.dndbeyond.com/sources/basic-rules/step-by-step-characters
    # https://www.instructables.com/Creating-a-DD-5e-Character-for-Beginners/
    race = determine_race()
    character_class = determine_class()
    background = determine_background()
    level = 1
    hit_dice = 0
    stats = alter_stats(roll_stats(), race)
    mods = determine_mods(stats)
    languages = determine_languages(background, race)
    character_sex = generate_sex()
    height, weight = generate_size(race)
    characteristics = get_pt(background)
    allignment = gen_alig(characteristics[1])
    return None

def print_c(lst):
    for i in lst:
        if type(i) == list:
            for j in i:
                print(f'{j}')
        else:
            print(f'{i}')

