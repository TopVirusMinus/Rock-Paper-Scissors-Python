import random
import os

#! Input Validation
play= "Y"
# You don't need to set the type of a variable
countH= 0
countC= 0
while(play == "Y"):
    get_user_choice= input("Rock, Paper, Scissors ? : ")
    get_user_choice= get_user_choice.lower()
    # Use the "in" operator to check for multiple string comparisons at once
    # Check if the input is not valid, instead of checking if its valid
    if(get_user_choice not in ("rock", "paper", "scissors")):
       print("This is not a valid option!") 
       break
#! Computer Choice
    options=["rock", "paper", "scissors"]
    # Use the built in Function choice to get a random element of a list
    final_choice= random.choice(options)
    print("Computer Choice: ", final_choice )

#! Win/Loss Conditions
    # You can check for multiple statements at once with the "or" operator
    if(final_choice=="rock" and get_user_choice=="paper" or final_choice=="paper" and get_user_choice=="scissors" or final_choice=="scissors" and get_user_choice=="rock"):
        print("You Won")
        countH+= 1
    elif(final_choice=="paper" and get_user_choice=="rock" or final_choice=="rock" and get_user_choice=="scissors" or final_choice=="scissors" and get_user_choice=="paper"):
        print("You Lost")
        countC+= 1
    elif(final_choice==get_user_choice):
        print("Draw")
    print("----------------------")
    print(f"Human Score: {countH}")
    print(f"Computer Score: {countC}")
    print("----------------------")
    print("")
    play= input("Play Again Y/N : ")
    play= play.upper()
    print("")
    os.system('cls')
    if(play=="N"):
        break
countH= int(0)
countC= int(0)
