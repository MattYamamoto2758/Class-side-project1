starterHP = 23
starter_attack = 10

opp_starterHP = starterHP
opp_starter_attack = starter_attack


print("Your getting your starter today.")
choose_name = True
while choose_name:
    name = input("Whats your name. ")
    confirm_name = input("So it's " + name + "?")
    if confirm_name == "yes":
        choose_name = False
    else:
        print("Please try again.")

print("So",name,"you go to the lab to pick up your starter.")
print("In the lab you see the professor.")
print("He tells you that you can choose from Charmander,Squirtle,Bulbasaur.")

first_chose = True
while first_chose == True:
    
    starter = input("Please choose.")

    if starter == "Charmander":
        first_chose = False

    elif starter == "Squirtle":
        first_chose = False

    elif starter == "Bulbasaur":
        first_chose = False

    else:
        print("Try again")

print("Good choice. Said the professor. I too like",starter)

if starter == "Charmander":
    opp_starter = "Squirtle"

if starter == "Squirtle":
    opp_starter = "Bulbasaur"

if starter == "Bulbasaur":
    opp_starter = "Charmander"

print("Your friend and rival choose's",opp_starter,".")
print("You battle your rival.")
opp_name = input("Whats your rival's name? ")
print("Your rival",opp_name,"sends out",opp_starter,".")


print("You start.")
print("Your",starter,"can use tackle")
your_turn = True
attack = input ("You can also use leer.")
while your_turn == True:
    
    if attack == "tackle":
        opp_starterHP1 = opp_starterHP - starter_attack
        your_turn = False
        
    elif attack == "leer":
        opp_starter_attack - 2

    else:
        print("try agian.")

print("Your starter uses",attack)
print(opp_name+"'s",opp_starter,"is at",opp_starterHP1)
print(opp_name,"uses tackle")
starterHP1 = starterHP - opp_starter_attack
print("Your",starter,"is at",starterHP1)
print("Your",starter,"can use tackle")
your_turn1 = True
attack1 = input("or leer")
while your_turn == True:

    if attack1 == "tackle":
        opp_starterHP2 = opp_starterHP1 - starter_attack

    elif attack1 == "leer":
        opp_starter_attack - 2

    else:
        print("Try again")

print(opp_name,opp_starter,"is at",opp_starterHP2)
print(opp_starter_attack)

    







    