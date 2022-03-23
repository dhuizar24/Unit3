import random

name = input("Enter valid username: ")

print("You start in Independence, Missouri. It is March 1st and the road ahead is about 2,000 miles ahead. You have purchased 500 pounds of food and 5 health")

loop = True 

food = 500
health = 5 
 
def choices():
    choice = input("What would you like to do?: rest, hunt, status, help, quit")
    print(choice)
    return choice


from random import randrange

def restdays():
    return randrange(2, 6)

def huntdays():
    return randrange(2,6)

def foodsupp(food):
    return food + 100


while loop: 

    choice = choices()
    rest = restdays()
    hunt = huntdays()
    bigfood = foodsupp(food)

    if choice == 'rest':
        print(f"You rest for {rest} days")
    elif choice == 'hunt':
        print(f"You took {hunt} days to find food")
        print(f"You now have {bigfood} pounds of food")


