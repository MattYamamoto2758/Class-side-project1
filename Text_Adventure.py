import random

starterHP = 23
starter_attack = 10
level = 5
rare_candy = 0

opp_starterHP = starterHP
opp_starter_attack = starter_attack

battle_counter = 0
if battle_counter == 5:
    starterHP += 2
    starter_attack += 2
    level += 1
import time

print("You are getting your starter today.")
choose_name = True
while choose_name:
    name = input("What's your name? ")
    confirm_name = input("So it's " + name + "? ")
    if confirm_name == "yes":
        choose_name = False
    else:
        print("Please try again.")

print("So",name,"you go to the lab to pick up your starter.")
time.sleep(0.6)
print("In the lab you see the professor.")
time.sleep(0.6)
print("He tells you that you can choose from Charmander, Squirtle, Bulbasaur.")
time.sleep(0.6)
first_chose = True
while first_chose == True:
    
    starter1 = input("Please choose. ")

    if starter1.lower() == "charmander":
        starter = "Charmander"
        first_chose = False

    elif starter1.lower() == "Squirtle":
        starter = "Squirtle"
        first_chose = False

    elif starter1.lower() == "Bulbasaur":
        starter = "Bulbasaur"
        first_chose = False

    else:
        print("Try again")

print("Good choice. Said the professor. I too like",starter)
time.sleep(0.5)
# Nick name
nick_name = True
while nick_name == True:
    nickName = input("Do you want to give " + starter + " a Nick name? ")
    if nickName.lower() == "yes":
        nickname = input("What will it be then? ")
        nick_name = False
    elif nickName.lower() == "no":
        print("That is ok")
check = input ("So it's "+ nickname + " ? " )
        

if starter == "Charmander":
    opp_starter = "Squirtle"

if starter == "Squirtle":
    opp_starter = "Bulbasaur"

if starter == "Bulbasaur":
    opp_starter = "Charmander"

print("Your friend and rival chooses",opp_starter+".")
print("You battle your rival.")
opp_name = input("What's your rival's name? ")
print("Your rival",opp_name,"sends out",opp_starter,".")
print("Your",starter,"has",starterHP,"HP.")
print(opp_name+"'s",opp_starter,"has",opp_starterHP,"HP")


print("You start.")
print("Your",starter,"can use tackle")

#first battle

your_turn = True

while your_turn == True:
    
    attack = input ("You can also use growl. Please choose. ")
#turn one
    if attack == "tackle":
        opp_starterHP1 = opp_starterHP - starter_attack
        opp_starter_attack1 = opp_starter_attack + 0
        your_turn = False
        
    elif attack == "growl":
        opp_starter_attack1 = opp_starter_attack - 2
        opp_starterHP1 = opp_starterHP
        your_turn = False

    else:
        print("Try agian.")

print("Your starter uses",attack)
print(opp_name+"'s",opp_starter,"is at",opp_starterHP1,"HP.")
if attack == "tackle":
    print("Your attack did",starter_attack,"damage")
# end of turn one    
print(opp_name,"uses tackle")
starterHP1 = starterHP - opp_starter_attack1
print("Your",starter,"is at",starterHP1,"HP. The attack did 10 damage.")
your_turn = True

while your_turn == True:
#turn 2    
    attack = input ("You can use tackle and growl. ")

    if attack == "tackle":
        opp_starterHP1 -= starter_attack
        your_turn = False

    elif attack == "growl":
        opp_starter_attack1 -= 2
        opp_starterHP1 = opp_starterHP1 + 0
        your_turn = False

    else:
        print("try agian")


print("Your",starter,"is at",starterHP1,"HP.")
print(opp_name+"'s",opp_starter,"is at",opp_starterHP1,"HP.")
print(opp_name+"'s",opp_starter,"missed.")
# end of turn 2 

    
if opp_starterHP1 > 0:
# turn 3    
    your_turn = True
    while your_turn == True:
        attack = input("You can use growl or tackle. Which one will you use? ")
        if attack == "tackle":
            opp_starterHP1 -= starter_attack
            your_turn = False

        elif attack == "growl":
            opp_starter_attack -= 2
            your_turn = False

        else:
            print("Try agian.")

print("Your",starter,"uses",attack)
print(opp_name+"'s",opp_starter,"is at",opp_starterHP1,"HP.")
if opp_starterHP1 >= 0 :
    print(opp_name+"'s",opp_starter,"uses growl")
    print(starter+"'s attack fell")
# end of turn 3

#if not win
# turn 4
elif opp_starterHP1 > 0:
    your_turn = True
    while your_turn == True: 
        attack = input("You can use growl or tackle. ")
        if attack == "tackle":
            opp_starterHP1 -= starter_attack
            your_turn = False

        elif attack == "growl":
            opp_starter_attack -= 2
            your_turn = False

        else:
            print("Try agian.")

if opp_starterHP1 > 0:
    print(opp_name+"'s",opp_starter,"is at",opp_starterHP1,".")
    print(opp_name,"uses tackle.")
    print("Its a critical hit")
    starterHP1 = 0
    input("Feels bad. ")
    if starterHP1 <= 0:
        lol = True
        while lol == True:
            print("YOU LOSE")
elif opp_starterHP1 <= 0:
    print("YOU WIN!!!")
    print("YOU WIN!!!")
    print("YOU WIN!!!")
    starterHP += 2
    starter_attack += 2
    level +=1
    print("Your",starter,"leveled up.",starter,"is now level",level,".")
    print("Now",starter," has",starterHP,"HP.")
    print("Its attack is also",starter_attack)
    print("You should go to the next town, Adventure town.")


    

#after battle
#next town or rare candy


  
town_ = True
while town_ == True:
    town = input("Please choose.(next town or Adventure town) or go home for a treat!")

    go_home = True
    while go_home == True:

        if town == "go home":
            if rare_candy < 1:
                print("Your mom is very greatful that you said goodbye.")
                print("Your mom gives you a rare candy.")
                rare_candy += 1
                print("You have",rare_candy,"rare candy")
                go_home = False
                town = True
                rare_candy1= input("Do you want to use the candy? ")
                if rare_candy1 == "yes":
                    starterHP += 2
                    starter_attack += 2
                    level += 1
                    rare_candy -= 1
                    print("Your",starter,"leveled up.",starter,"is at",level,"level")
                    print(starter,"now has",starterHP,"HP")
                    print("and",starter_attack,"attack")
                    print("You now have",rare_candy,"rare candies left.")

            else:
                print("Fail")

        if town == "next town":
            go_home = False
            town_ = False

        elif town == "Adventure town":
            go_home = False
            town_ = False


        
        else:
            print("Try agian")

print("You are walking along the path.")
print("You can go in the grass.")
grass = True
while grass == True:
    battle = input("Do you want to go in the grass?")

    if battle == "yes":
        print("You battle Weedle")
        grass = False

    




    
