#split from new file diceroller.py intent to make separate gui based roller using TK
import random

def dice_pool():
    ability_scores = [0,0,0,0,0,0]
    dice_set = [1,1,1,1] #4 dice to be rolled
    for x in range (0, 6): #rolls sets of dice 6 time
        for y in range (0, 4): #rolls 4 dice
            dice_set[y] = random.randint(1, 6) #dice are d6
            #print(dice_set)
        dice_set.remove(min(dice_set))
        if sum(dice_set) < 8: #prevents saving an ability score lower than 8, adjust if needed set to 0 for no safety
            ability_scores[x]= 8
        else:
            ability_scores[x]= sum(dice_set)
        dice_set = [1,1,1,1]
    if sum(ability_scores) < 72: #prevents saving a character with less than 72 total ability points, adjust if needed
        dice_pool()
    else:
        print("Assign from the following ability scores and associated modifiers:")
        print("Ability score: ",ability_scores)
        modifiers = [0,0,0,0,0,0]
        for m in range (0,6):
            modifiers[m] = int((ability_scores[m] - 10)/2) #roll modifiers based on ability score minus 10 div 2
        print("Modifiers are: ", modifiers)
    input("Press \"Enter\" to quit") #holds window prior to closing

dice_pool()
