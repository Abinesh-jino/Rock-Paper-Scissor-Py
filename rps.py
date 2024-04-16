import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3



print(" ")

print(" Welcome To Rock Paper Scissor Game 🎮 " .center(60,"-") )

print("")

#Options for RPS 

playerchoice = input("Select from Below \n\t 1 for Rock 🪨 \n\t 2 for Paper 📃, or \n\t 3 for Scissors ✂️ \n \n Enter Your Choice : ")


#Casting into Int Values

player = int(playerchoice)

computerchoice = random.choice("123")
computer = int(computerchoice)

print(" ")

print(" You Chose " + str(RPS(player)).replace('RPS.', ' ').title() )
print(" Python Chose " + str(RPS(computer)).replace('RPS.', ' ').title() )

print("")

if player<1 or player > 3 :
    sys.exit(" You Have to Only Enter 1 , 2 or 3 \n\n" )
elif player ==1 and computer==3 :
    print(" Rock Beats Scissor \n")
    print(" You win 🏆 🥳 \n\n  ")
elif player==2 and computer==1 :
    print(" Paper Wraps Rock \n")
    print(" You win 🏆 🥳\n\n  ")
elif player==3 and computer==2 :
    print(" Scissor Cuts Paper \n")
    print(" You win 🏆 🥳 \n\n  ")

elif player==computer:
    print(" You Chose Same as Python  \n")
    print( " 😲 It is a Tie , Play Again !! \n\n ")
else:
    print(" 🐍 Python Wins , Try Again 🥹 \n\n ")
