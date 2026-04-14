name = input("What is you first and last name? ")
lunch = int(input("Which lunch do you have 4= fourth lunch 6= sixth lunch "))
if lunch == ("6"):
    lunch = ("sixth")
else :
    lunch == ("4")
    lunch =("fourth")
choice = input(str(name) + " Would you like to reserve a table for lunch tomorrow? y=yes n=no ")
if choice == ("y"):
    choice = ("yes")
    where = (input("Where would you like to eat lunch? 1= inside the cafetria 2=outside ramadas "))
    if where == ("1"):
        where = ("inside the cafetria")
    else:
        where == ("2")
        which = int(input("Which ramda whould you like to eat at? 1= the East Ramada located by the 300s buliding 2= the West Ramada located by the lions den? "))
    if which == ("1"):
        which = ("in the East Ramada located by the 300s building")
        where == which
        where = ("in the East Ramada located by the 300s building")
    else:
        which == ("2")
        which = ("in the West Ramada located by the lions den")
        where == which
        where = ("in the West Ramada located by the lions den")
        amount = (input("Plese enter the amount of people you would like to eat lunch with.    Be sure to include you self because you are not automatically included in the count. If it is just you type a 1."))
    if amount == ("1"):
        amount = (" one ")
        print("\n")
    else :
        amount += 1
        counter = 1
        while counter < amount:
            input("what is person" + str(counter) + "'s name? ")
            counter += 1
            print("\n")
    print (" you have made a reservation for " + str(lunch) + " " + str(where) + " for " + str(amount) + " people. Please look for " + str(name) + "'s name and have your student id. IF YOU DO NOT HAVE YOUR STUDENT ID YOU WILL NOT BE ABLE TO SIT AT THE TABLE!!!. Enjoy your lunch and have a great rest of your day.")
else:
    choice == ("n")
    choice = ("no")
    print("Ok have a nice day")

