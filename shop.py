my_bag=[]



 
 
def shop_store():
    shoping_menu=input("Are you going to buy a potion? [Y] or [N]")
    if shoping_menu == "Y":
        print("Here is your potion great warriors")
        new_bag=my_bag.append("potion")
        print(my_bag)
    elif shoping_menu == "N":
        print("come again next time")

def healing_wizard(shop_store,Deagono_hp,Slados_hp,my_bag):
     heal_menu=input("I am the healing wizard do you have a potion for me? [Y] or [N]")
     healing_hp=100
     if heal_menu == "Y":
        print("Alakazam!! I summon the power of healing on the great warriors")
        New_hpD=Deagono_hp+healing_hp
        New_hpS=Slados_hp+healing_hp
        my_bag.remove("potion")
        print(my_bag)
        print(New_hpD)
        print(New_hpS)
     elif heal_menu == "N":
        print("come again next time")