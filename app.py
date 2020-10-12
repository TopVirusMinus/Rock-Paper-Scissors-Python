import random
import os

#! Input Validation
play= "Y"
countH= int(0)
countC= int(0)
while(play == "Y"):
    while(play=="Y"):
        get_user_choice= input("Rock, Paper, Scissors ? : ")
        get_user_choice= get_user_choice.lower()
        if(get_user_choice=="rock" or get_user_choice=="paper" or get_user_choice=="scissors" ):
            break

#! Computer Choice
    options=["rock", "paper", "scissors"]
    choice= random.randint(0, 2)
    final_choice= options[choice]
    print("Computer Choice: ", final_choice )

#! Win/Loss Conditions

    if(final_choice=="rock" and get_user_choice=="paper"):
        print("You Won")
        countH+= 1
    elif(final_choice=="paper" and get_user_choice=="scissors"):
        print("You Won")
        countH+= 1
    elif(final_choice=="scissors" and get_user_choice=="rock"):
        print("You Won")
        countH+= 1
    elif(final_choice=="paper" and get_user_choice=="rock"):
        print("You Lost")
        countC+= 1
    elif(final_choice=="rock" and get_user_choice=="scissors"):
        print("You Lost")
        countC+= 1
    elif(final_choice=="scissors" and get_user_choice=="paper"):
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
