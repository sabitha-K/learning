import random

User_choice = int(input("Enter the Number [0 for Rock, 1 for Paper, 2 for Scissors]: "))

if User_choice > 3 or User_choice < 0:
    print("You enter a invalid number, You Lose!")
else:

    Computer_choice = random.randint(0,2)
    print("Computer_choice", Computer_choice)
    if User_choice == Computer_choice:
        print("Its a draw!")
    elif User_choice == 0 and Computer_choice == 2:
        print("You Win")
    elif User_choice == 2 and Computer_choice == 0:
        print("You Lose")
    elif Computer_choice > User_choice:
        print("You Lose")
    elif User_choice > Computer_choice:
        print("You Win")

