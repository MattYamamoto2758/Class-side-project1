starterHP = 23
starter_attack = 10
level = 5

opp_starterHP = starterHP
opp_starter_attack = starter_attack

battle_counter = 0
if battle_counter == 10:
    starterHP += 2
    starter_attack += 2
    starter_level += 1




print("Your getting your starter today.")
choose_name = True
while choose_name:
    name = input("Whats your name. ")
    confirm_name = input("So it's " + name + "? ")
    if confirm_name == "yes":
        choose_name = False
    else:
        print("Please try again.")

print("So",name,"you go to the lab to pick up your starter.")
print("In the lab you see the professor.")
print("He tells you that you can choose from Charmander,Squirtle,Bulbasaur.")

first_chose = True
while first_chose == True:
    
    starter = input("Please choose. ")

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
your_turn = True
attack = input ("You can use tackle and leer.")
while your_turn == True:

    if attack == "tackle":
        opp_starterHP1 -= starter_attack
        your_turn = False

    elif attack == "leer":
        opp_starter_attack - 2

    else:
        print("try agian")

if opp_starterHP >= 0 :
    print("You win")
    starterHP += 2
    starter_attack += 2
    level +=1
print("Your",starter,"leveled up. Now it has",starterHP,"HP.")
print("Its attack is also",starter_attack)
print("Your",starter,"is now level",level)


    




    
