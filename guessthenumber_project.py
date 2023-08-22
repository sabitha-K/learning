import random
easy_level=10
hard_level=5

def set_difficulty(level_chosen):
    if level_chosen== "easy":
        return easy_level

    elif level_chosen=="hard":
        return hard_level

def check(guessed_num,answer,attempts):
    if guessed_num>answer:
        print("You are too high")
        return attempts - 1

    elif guessed_num<answer:
        print("You are too low")
        return attempts-1
    else:
        print(f"You are right....The answer is {answer}")

def game():
    print("let me think a number between 1 to 50")
    answer= random.randint(1,50)
    # print(answer)

    level=input("choose a difficulty level.... Type easy or hard: ").lower()
    attempts=set_difficulty(level)
    guessed_num=0
    while guessed_num!=answer:
        print(f"you have {attempts} attempts balance")
        guessed_num= int(input("Make a guess: "))
        attempts=check(guessed_num,answer,attempts)
        if attempts==0:
            print("Out of Guesses....You Lose")
            return

        if guessed_num!=answer:

           print("guess again")
game()
