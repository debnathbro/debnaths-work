#Author -> Abhiit_Debnath
#Project name -> Stone-Paper-Scissor
#Date -> 03/05/2023

import random
def check(comp, user):
    if(comp == 0 and (user == "Stone" or user == "stone")):
        return 0
    if(comp == 1 and (user == "Paper" or user == "paper")):
        return 0
    if(comp == 2 and (user == "Scissor" or user == "scissor")):
        return 0
    if(comp == 0 and (user == "Scissor" or user == "scissor")):
        return -1
    if(comp == 1 and (user == "Stone" or user == "stone")):
        return -1
    if(comp == 2 and (user == "Paper" or user == "paper")):
        return -1
    return 1
def prnt(comp):
    if(comp == 0):
        print("Computer chose stone")
    elif(comp == 1):
        print("Computer chose paper")
    elif(comp == 2):
        print("Computer chose scissor")
#-----------------------------------------------------program starts-----------------------------------------------------#
comp = random.randint(0, 2)
print("*********************************")
print("Wanna play Stone-Paper-Scissor!!!")
user = input("Chose any of three: ")
if(check(comp, user) == -1):
    print("You lose")
    prnt(comp)    
elif(check(comp, user) == 0):
    print("its draw!")
    prnt(comp)
else:
    print("You win")
    prnt(comp)
print("*********************************")