# james jack
# 3/5/21

# function that checks whether your game character has picked up all the items needed to perform certain tasks and
# checks against any status debuffs. Confirm checks with print statements.

# Game Character has the following item list: [pan, paper, idea, rope, groceries]
# Game Character has the following status debuffs: [slow]

# Task 1: Climb a mountain – needs rope, coat, and first aid kit, cannot have slow
# Task 2: Cook a meal – needs pan, groceries, cannot have small
# Task 3: Write a book – needs pen, paper, idea, cannot have confusion

# item list
pan = True
paper = True
idea = True
rope = True
groceries = True
coat = False
first_aid = False
pen = False
# player currently has these debuffs
confuse = False
slow = True
small = False

print("Based on the items and effects you have currently: ")


# function to check if items are in inventory
def game():
    if rope and coat and first_aid is True and slow is False:  # checks if ALL items required are present
        print("You climbed the mountain ")
    else:
        print("You cannot climb the mountain because you do not have the required items")

    if pan and groceries is True and small is False:   # checks if ALL items required are present
        print("You can cook a meal ")
    else:
        print("You do not have the required items to cook a meal ")    # checks if ALL items required are present

    if pen and paper and idea is True and confuse is False:   # checks if ALL items required are present
        print("You are able to write a book")
    else:
        print("You do not have the required items to write a book ")


game()
