import random
win = 0
lose = 0
tie = 0


def main():

    print("Welcome to the ROCK PAPER SCISSORS Game.\n Winning rules of the 'Rock Paper Scissors Game' is as follows: \n"
                                    +"ROCK blunts SCISSORS \n"
                                    +"PAPER covers ROCK \n"
                                    +"SCISSORS cut PAPER \n")

    while True:
        comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'

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

        if((user_choice == 1 and comp_choice == 3)):
            result = 'win'
            print("You win!\n")

        elif((user_choice == 2 and comp_choice == 1)):
            result = 'win'
            print("You win!\n")

        elif((user_choice == 3 and comp_choice == 2)):
            result = 'win'

        elif(user_choice == comp_choice):
            result = 'tie'

        else:
            result = 'lose'

        score(user_choice,comp_choice,result)

        print("Do you want to play again? (Y/N)")
        ans = input()

        if ans == 'n' or ans == 'N':
            break


    print('Your total wins are: ', win)
    print('Your total losses are: ', lose)
    print('Your total ties are: ', tie)

    print("\nThanks for playing")

def score(user_choice,comp_choice,result):
    global win
    global lose
    global tie

    if result == 'win':
        win += 1
        print("<== User wins ==>")

    elif result == 'lose':
        lose += 1
        print("<== Computer wins ==>")

    else:
        tie += 1
        print("<== The game is tied ==>")

    return result



main()
