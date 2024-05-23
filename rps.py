import random
import sys
from enum import Enum
import argparse


parser=argparse.ArgumentParser(
    description="Says Hello to User"
)

parser.add_argument(
    "-n", "--name" ,"--jin" , metavar="name" ,
    required=True , help="The Name of user Playing the Game "
)

args= parser.parse_args()

realname=args.name


def play_rps(name='Player'):
    
    
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3


    print(f"\n{name}, Welcome To Rock Paper Scissor Game 🎮 \n" .center(60,"-") )

    #Options for RPS 

    playagain = True

    while playagain:
        

        playerchoice = input(f"\n {name} , please select from Below \n\t 1 for Rock 🪨 \n\t 2 for Paper 📃, or \n\t 3 for Scissors ✂️ \n \n Enter Your Choice : ")

        if int(playerchoice) >3 or int(playerchoice)<1:
            print(f" \n\n {name} , please Only Enter 1 , 2 or 3 \n\n" )
            playerchoice = input(f"\n {name} , please select from Below \n\t 1 for Rock 🪨 \n\t 2 for Paper 📃, or \n\t 3 for Scissors ✂️ \n \n Enter Your Choice : ")
        
        #Casting into Int Values

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(" ")

        print(f" {name} , you Chose {str(RPS(player)).replace('RPS.', ' ').title()} ")
        print(f" Python Chose {str(RPS(computer)).replace('RPS.', ' ').title()}" )

        print("")

        if player ==1 and computer==3 :
            print(" Rock Beats Scissor \n")
            print(f" {name} , you won 🏆 🥳 \n\n  ")
        elif player==2 and computer==1 :
            print(" Paper Wraps Rock \n")
            print(f" {name} , you won 🏆 🥳 \n\n ")
        elif player==3 and computer==2 :
            print(" Scissor Cuts Paper \n")
            print(f" {name} , you won  \n\n  ")

        elif player==computer:
            print(f" Ouch  {name} , you Chose Same as Python  \n")
            print( " 😲 It is a Tie , Play Again !! \n\n ")
        else:
            print(f" Sorry {name} 🐍 Python Won , Try Again 🥹 \n ")
            
        playagain = input(f" \n {name} , do You Wanna Play Again ? (Y/N) : ").lower()
        if playagain=='y':
            playagain = True
        else:
            playagain = False
            print(" \n Thank You For Playing Rock Paper Scissor Game 🎮 \n".center(60,"-") )
            sys.exit(" \n\n Game Exited Successfully !! \n\n")

play_rps(realname)