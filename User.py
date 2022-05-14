donate_start=0


def user_login(database,username,password):
    if username not in database:
        print("username is not registered")
        return ""
    elif username in database and database[username] == password:
        print("Welcome")
        return username 
    else:
        print("user name or password not correct")
        return ""

def register(database,new_username,new_password):
    if new_username in database:
        print(f"{new_username} already registered")
        return ""
    else:
        database[new_username] = new_password
        print(f'{new_username} has been registered')
        return new_username
   
def donate(username):
    donation_amt=float(input("Enter amount to donate"))
    if donation_amt == 0 :
        return ""
    else: 
         donation_string= username + " donated " + str(donation_amt)
         print("Thank you so much")
         return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")
    if(len(donations)==0):
        print("Currerntly, there are no donations ")
    else:
        for x in donations:
            print(x)    