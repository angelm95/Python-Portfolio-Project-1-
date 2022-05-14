from Battles import DragonFight
from Battles import Final
from Battles.shop import shop_store,healing_wizard
from Battles.User import user_login,register,donate,show_donations 
from Battles.Start_menu import start_prompt
from Battles.DragonFight import dragon_duel

database = {"Admin":"password123"}
donations = [] 
authorized_user = ""
donate_start=0
value_donate=0
my_bag=[]




import random 



## The four dragons 

WaterDragon_attack = 100
WaterDragon_hp=400

EarthDragon_attack = 100
EarthDragon_hp=600

FireDragon_attack = 100
FireDragon_hp=800

AirDragon_attack = 100
AirDragon_hp = 1000

## Items 

treasure_chest = ["diamonds", "gold", "silver", "sword"]



## Start menu 


while True:
    player1_start=input("Hey player 1 are you ready for this dangerous quest? [Y] or [N]")
    if player1_start == "Y": 
        print("Welcome Deagono The Legendary Thunder Warrior and thank you for your bravery")
        break
    elif player1_start == "N":
        print("We are sorry to see you Deagono The Legendary Thunder Warrior, Please Come Again")
        break
    else:
        print("please select Y or N Deagono")
        
while True:
    player2_start=input("Hey player 2 are you ready for this dangerous quest? [Y] or [N]")
    if player2_start == "Y": 
        print("Welcome Slados God of Lightning and thank you for your bravery")
        break
    elif player2_start == "N":
        print("We are sorry to see you Slados God of Lightning, Please Come Again")
        break
    else:
        print("please select Y or N Slados")




while True:
    start_prompt()
    option=input("choose an option : ")
    if option == "1":
        username = input("please enter your username : ")
        password = input("please enter your password : ")
        authorized_user= user_login(database,username,password)
    elif option == "2":
        new_username = input("please enter your username : ")
        new_password = input("please enter your password : ")
        authorized_user = register(database,new_username,new_password)
        print(database)
    elif option == "3":
        if authorized_user == "":
            print("You are not logged in ")
        else:    
            donated_string = donate(authorized_user)
            donations.append(donated_string)
    elif option == "4":
        print(my_bag)
        if len(my_bag) == 0:
           print("You need to buy potions in order to see the healing wizard")
           continue
        else:
            healing_wizard(shop_store)
            continue
    elif option == "5":
           shop_store()
           continue
    elif option == "6":
           print("hello")
           continue
    elif option == "7":
           dragon_duel()
           continue
    elif option == "8":
           print("Goodbye")
           exit()
    elif authorized_user == "":
       print("You must be logged in to donate.")
    else: 
       print(f"Logged in as:{authorized_user}")
       continue

