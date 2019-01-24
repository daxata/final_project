import random
print("Welcome to the ROCK PAPER SCISSORS Game.\n Winning rules of the 'Rock Paper Scissors Game' is as follows: \n"
                                +"Rock blunts Scissors \n"
                                +"Paper covers Rock \n"
                                +"Scissors cut Paper \n")

comp_choice = random.randint(1, 3)

if comp_choice == 1:
    comp_choice_name = 'Rock'
elif comp_choice == 2:
    comp_choice_name = 'Paper'
else:
    comp_choice_name = 'Scissors'

while True:
    print("\n1. ROCK\n2. PAPER\n3. SCISSORS \n")
    user_choice = int(input("Enter your choice: "))

    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter a valid input: "))

    if user_choice == 1:
        user_choice_name = 'Rock'

    elif user_choice == 2:
        user_choice_name = 'Paper'

    else:
        user_choice_name = 'Scissors'

    print("User's choice is: ",user_choice_name)

    print("\nNow its computer's turn.......\n")

    print("Computer's choice is: ",comp_choice_name)

    print(user_choice_name, " V/S " ,comp_choice_name)
    print("\n")

    if((user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice ==1 )):
        result = "Paper"

    elif((user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1)):
        result = "Rock"
    else:
        result = "Scissor"

    if(user_choice == comp_choice):
        print("<== The game is tied ==>")

    elif result == user_choice_name:
        print("<== User wins ==>")

    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break


print("\nThanks for playing")
