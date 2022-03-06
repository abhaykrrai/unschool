#treasure hunt game 

import random
from tracemalloc import start

def lets_play_again():                                    #defining a function lets_play_again
    print("\nDO you want to play again? (Y or N)")

    answer = input(">").lower()                           #taking input from the user and storing it in a variable called answer

    if answer =='y':                                      #checking if the user input statisfy the condition
        start()
    elif answer =='n':
        exit()
    else:
        print("Wrong input")



def monster_room():                                       #defining the function named monster_room 
    print("\n Now you entered the room of a monster")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? ( 1 or 2)")
    print(" 1 ). Go through the door silently.")
    print(" 2 ). Kill the monster and show your courage!")
    n = input("> ")
    if(n=='1'):
        treasure_room()                                   #if the condtion is true the user will go to treasure room
    elif(n=='2'):
        game_over("Monster") 


def game_over(reason):
    if reason=="Monster":
        print("The Monster was hungry, he/it ate you.")
        print("Game Over!!! ")
        lets_play_again()
    elif(reason=="room"):
        print("You didn't any diamonds with you.")
        print("Game Over !!!!")
        lets_play_again()
    elif(reason=="snake"):
        print("You wanted the eggs not the treasure. Thats why the snake killed you !!!l")
        print("Game Over !!!!")
        lets_play_again()


def treasure_room():
    print("\n You are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("what would you do? ( 1 or 2 )")
    print("1) . Take some diamonds and go through the door.")
    print("2) . Just go through the door.")
    n = input("> ")
    if(n=='1'):
        print("You win !!! ")
        lets_play_again()
    elif(n=='2'):
        game_over("room")

def snake_room():
    print("\nThere is a sanke here.")
    print("Behind the Sanke is another door.")
    print("The sanke is having eggs!")
    print("What would you do? (1 or 2")
    print("1) . Take the eggs.")
    print("2) .Taunt the Snake")
    n = input("> ")
    if(n=="1"):
        game_over("snake")
    elif (n=='2'):
        treasure_room()



def start():                                                #defining the fuction start to start the game
    print("You are standing in a dark room.")
    print("There is a door to your left and right, which one do you take? ( l or r)")

    n = input(">").lower()
    if(n=='l'):
        snake_room()
    elif (n=='r'):
        monster_room()



start()                                                     #calling start function

