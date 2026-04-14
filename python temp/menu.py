
from dataclasses import FrozenInstanceError


total=0
#fmt_total = "{:.2f}".format(total)
sandwich = int(input("What kind of sandwich would you like? 1=Chicken 2=Beef 3=Tofu  "))
print (sandwich)
if sandwich < 1:
  print ("Please select 1,2, or 3")
elif sandwich > 3: 
  print( "Please select 1,2,or 3")
else:
  print (" ")
  

if sandwich == 1:
  sandwich_type = "Chicken"
  total += 5.25
  selected_sandwch = True
elif sandwich == 2:
  sandwich_type = "Beef"
  total += 6.25
  selected_sandwch = True
elif sandwich == 3:
  sandwich_type = "Tofu"
  total += 5.75
  selected_sandwch = True
else:
  selected_sandwch = False
#print ("You have chosen a " +str(sandwich_type) + " sandwich, and you owe $" + str(total) + " thank you")
#print ("\n")

choice = input("Would you like a drink? y=yes n= no  ")
if choice == ("y"):
  drink_selected = True
  size = input("What size drink would you like s= small m= medium l= large  ")
  if size == ("s"):
    size = "small"
    total += 1.00
  elif size == ("m"):
    size = "Medium"
    total += 1.75
  elif size == ("l"):  
    size = "Large"
    total += 2.25
else: 
  choice == ("n")
  drink_selected = False
  fmt_total = "{:.2f}".format(total)
  #print ("You have chosen a " +str(sandwich_type) + " sandwich, and you owe $ " + str(total) + " thank you")
fmt_total = "{:.2f}".format(total)
#print ("You have chosen a " +str(sandwich_type) + " sandwich, with a " + str(size) +" drink and you owe $ " + str(total) + " thank you")



fries = input("Would you like fries y=yes n=no ")
if fries == ("y"):
  fries_selected = True
  fries_size = input( "what size of fries would you like s=small m=medium l=large ")
  if fries_size == ("s"):
    supersize = input("would you ike to super size your fries y=yes n=no ")
    if supersize == ("y"):
      fries_size = "supersize"
      total += 2.00
    else:
      supersize == ("n")
      fries_size = "small"   
      total += 1.00
  elif fries_size == ("m"):
    fries_size = "medium"
    total += 1.50
  elif fries_size == ("l"):
    fries_size = "large"
    total += 2.00  
else :
  fries == ("n")
  fries_selected = False
  fmt_total = "{:.2f}".format(total)
  #print ("You have chosen a " +str(sandwich_type) + " sandwich, with a " + str(size) +" drink and you owe $ " + str(total) + " thank you")
fmt_total = "{:.2f}".format(total)
#print ("You have chosen a " +str(sandwich_type) + " sandwich, " + str(size) +" drink, with a " +str(fries_size) + " fry and you owe $ " + str(total) + " thank you")

if (selected_sandwch == True) :
  if (drink_selected == True) :
    if (fries_selected == True) :
      total = total - 1.00
      print("You bought fries, a sandwich and a drink making you eligiable for a dollar off of your total. This will be deducted from you total at the end.")
else:
  if (selected_sandwch == False) :
    if (drink_selected == False) :
     if (fries_selected == False) :
       total = total 
               

ketchup = input("Would you like any ketchup packets with your order y=yes n=no ")
if ketchup == ("y"):
  ketchup_amount = int(input("how many ketchup packets would you like "))
  if ketchup_amount == ketchup_amount:
    total = total + ketchup_amount * .25
else:
  ketchup == ("n")
  ketchup = ("no")
  fmt_total = "{:.2f}".format(total)
  print ("You have chosen a " +str(sandwich_type) + " sandwich, " + str(size) +" drink, with a " +str(fries_size) + " fry and you owe $ " + str(fmt_total) + " thank you")
fmt_total = "{:.2f}".format(total)
print("You have chosen a " +str(sandwich_type) + " sandwich, " + str(size) +" drink, with a " +str(fries_size) + " fry and " + str(ketchup_amount) + " ketchup packet(s) and you owe $ " + str(fmt_total) + " thank you")
