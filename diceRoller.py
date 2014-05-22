#Dice roll program
#This program rolls a virtual dice then shows you the number.
import random
import time
rollit=0
def roll():
    global rollit
    print("rolling...")
    rollit=random.randint(1,6)
def show_dice():
    global rollit
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    if rollit==1:
        print("---------\n|       |\n|   O   |\n|       |\n---------\n")
    elif rollit==2:
        print("---------\n| O     |\n|       |\n|     O |\n---------\n")
    elif rollit==3:
        print("---------\n| O     |\n|   O   |\n|     O |\n---------\n")
    elif rollit==4:
        print("---------\n| O   O |\n|       |\n| O   O |\n---------\n")
    elif rollit==5:
        print("---------\n| O   O |\n|   O   |\n| O   O |\n---------\n")
    elif rollit==6:
        print("---------\n| O   O |\n| O   O |\n| O   O |\n---------\n")
    answer=input("again? ")
    if answer=="yes":
        roll()
    if answer=="yes":
        show_dice()
    elif answer=="no":
        print("fine.")
roll()
time.sleep(1)
show_dice()
