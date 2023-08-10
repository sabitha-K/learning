import os

def find_winners(Bidders_details):
    highest_price=0
    winner=""
    for bidder in Bidders_details:
        price= Bidders_details[bidder]
        if price > highest_price:
            highest_price=price
            winner=bidder
    print(Bidders_data)
    print(f"{winner} is the winner of bid price {highest_price}")



Bidders_data={}

end_of_auction=False
while not end_of_auction:



    name=input("Enter your Name: ")
    bid_price=int(input("Enter your Bid Price: "))
    Bidders_data[name]=bid_price
    more_bidders=input("Are there more bidders, Type 'yes' or 'No'").lower()
    if more_bidders=='no':
        end_of_auction=True
        find_winners(Bidders_data)
    elif more_bidders=='yes':
        os.system('cls')


