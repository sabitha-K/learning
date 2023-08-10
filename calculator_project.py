import os

def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiple(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)

def calculator():
    operations={"+":add,"-":subtract,"*":multiple,"/":divide}

    num1=float(input("Enter first number: "))
    with_output=True
    while with_output:
        for symbol in operations:
            print(symbol)
        symbol=input("Pick an symbol: ")
        num2= float(input("Enter second number: "))
        calculation=operations[symbol]
        output=calculation(num1,num2)
        print(f"{num1} {symbol} {num2} = {output}")
        should_continue=input("y to continue with the output,n to start fresh, x to exit: ").lower()
        if should_continue=="y":
            num1=output
        elif should_continue=="n":
            with_output=False
            os.system("cls")
            calculator()
        elif should_continue=="x":
            with_output=False
            print("bye")
calculator()