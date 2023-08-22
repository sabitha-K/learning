import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
         "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","y","Z"]
symbols=["!","@","#","$","%","^","&","*","(",")","+"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
print("Welcome to password generator")
n_letters=int(input("Enter a number of letters you want in your password: "))
n_symbols=int(input("Enter a number of symbols you want in your password: "))
n_numbers=int(input("Enter a number of numbers you want in your password: "))
password=[]
for i in range(0,n_letters):
    char=random.choice(letters)
    password+=char
for i in range(0, n_symbols):
    char = random.choice(symbols)
    password += char
for i in range(0, n_numbers):
    char = random.choice(numbers)
    password += char
random.shuffle(password)
password_shuffle=""
for char in password:
    password_shuffle+=char
print(password_shuffle)





