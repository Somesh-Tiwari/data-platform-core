#Day 5 - Condditionals and Booleans 

name = input("Enter your name: ").lower().strip()

if name == "somesh":
    print("Welcome Sir")
elif name == "tiwari":
    print("Welcome Sir")
else:
    print("Welcome Guest")   


user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print("Welcome Admin")
elif user == 'Admin' and not logged_in:
    print("Please log in Admin")
elif user=='Admin'or logged_in:
    print("Try again")
else:
    print("Welcome Guest")

