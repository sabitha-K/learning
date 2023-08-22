import random
lives=6
words=["apple", "orange", "grapes"]
print("Guess a fruit name , You have six lives!")
chosen_word=random.choice(words)
# print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display+="_"
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Enter a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
          display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        print("You Have",lives, "lives")
        if lives==0:
            game_over=True
            print("You Lose")
    if "_" not in display:
        game_over=True
        print("You Won")






