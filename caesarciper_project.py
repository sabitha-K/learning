alphapet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encryption(plain_text,shift_key):
    cipher = ""

    for char in plain_text:
        if char in alphapet:
            position= alphapet.index(char)
            new_position = (position + shift_key) % 26
            cipher += alphapet[new_position]
        else:
            cipher+=char
    print(f"This is your cipher text: {cipher}")

def decryption(ciper_text,shift_key):
    plain = ""
    for char in ciper_text:
        if char in alphapet:
            position= alphapet.index(char)
            new_position = (position - shift_key) % 26
            plain += alphapet[new_position]
        else:
            plain+=char
    print(f"This is your cipher text: {plain}")
wanna_end=False
while not wanna_end:
    what_to_do=input("Enter 'encrypt' for encryption, 'decrypt' for decryption: ")
    text= input("Enter your message: ").lower()
    shift= int(input("Enter the shift number: "))
    if what_to_do=="encrypt":
        encryption(plain_text= text,shift_key=shift)
    if what_to_do=="decrypt":
        decryption(ciper_text=text, shift_key=shift)
    wanna_continue=input("Enter 'Yes' to continue, 'No' to exit: ")
    if wanna_continue=="No" :
        wanna_end=True
        print("Bye")
