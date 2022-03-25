#oregon trail
from calendar import c
from glob import glob
from os import stat
import random
from threading import current_thread
from random import randrange

name = input("Enter valid username: ")

print("You start in Independence, Missouri. It is March 1st and the road ahead is about 2,000 miles ahead. You have purchased 500 pounds of food and 5 health")
# variables 
loop = True 
miles_left = 2000
food = 500
health = 5
MONTHS = ['no month', 'January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MONTHS_30_DAYS = ['April', 'June', 'September', 'November']
current_day = 1
current_month = 3

 #functions
def choices():
    choice = input("What would you like to do?: travel,rest, hunt, status, help, quit")
    print(choice)
    return choice

def consume_food(days):
    global food

    food_consumed_this_turn = 5 * days 

    food = 


def rest():
    global health
    days_this_rest = randrange(2, 6)
    print(f"You rest for {days_this_rest} days")

    health += 1
    if health == 5:
        print('Health at max')
    else: 
        

    add_day(days_this_rest)
    

def hunt():
    global food 
    
    days_this_hunt = random.randrange(2,6)
    food += 100 
    
    


    add_day(days_this_rest)
def travel():
    days_travel = random.randint(3,7)
    miles_traveled = random.randint(30, 60)
    print(f"It took you {days_travel} traveling days")
    print(f"You traveled {miles_traveled} miles")
    
    add_day(days_travel)


#ask help for hp here
def hp(health):
    return health + 1 

def travel():
    global miles_left, current_day

    days_travel = random.randint(3,7)
    miles_traveled = random.randint(30, 60)
    print(f"It took you {days_travel} traveling days")
    print(f"You traveled {miles_traveled} miles")

    miles_left -= miles_traveled

def status():
    print(f"You have {miles_left} miles to go ")
    print(f"It is {MONTHS[current_month]} {current_day}.")
    print(f"You have {health} health")
    print(f"You have {food} pounds of food")

def add_day(days):
    global current_day, current_month 
    current_day += days

    #time to roll over month
    if MONTHS[current_month] in MONTHS_30_DAYS:
        if current_day > 30: 
            current_day -= 30 
            current_month += 1 
    else:
        if current_day > 31: 
            current_day -= 31
            current_month +=1 

while loop: 

    choice = choices()
    # rest = restdays()
    # hunt = huntdays()
    # food = foodsupp(food)
    # miles_lef = status()
    # travel_miles = traveldays()

    if choice == 'rest':
        rest()
        
    elif choice == 'hunt':
        hunt()
    elif choice == 'travel':
        travel()
        
    elif choice == 'status':                         




