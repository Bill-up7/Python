def check_guesses(guess, answer):
    global score
    attempts=0
    still_guessing = True
    
    while (still_guessing and attempts < 3):
        if guess == answer:
            score += 1
           # attempts += 1
            still_guessing = False
            print( "Correct!")
        else:
          if attempts < 2:
            guess = input("Try again ->") 
          attempts +=1
    if attempts == 3:
         print("the correct answer is " + str(answer))

score = 0
guess1 = input("What color is a Cardinal?   ")
check_guesses(guess1, "red")
guess2 = input("What is the fastest animal?   ")
check_guesses(guess2, "cheetah")
guess3 = input("What animal is associated with the desert?    ")
print(check_guesses(guess3, "camel"))
print( "Thats all, your final score was " + str(score))