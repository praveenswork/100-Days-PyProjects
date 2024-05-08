print("Welcome to the secret auction program.")

store={}
others_bid=False

#def func(n,b):
#    store.append({n:b})

def highest_bid(bidding_record):
    highest_bid=0
    winner=0
    for bidder in bidding_record:
        bid_amt=bidding_record[bidder]
        if bid_amt>highest_bid:
            highest_bid=bid_amt
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    

while not others_bid:
    name=input("What is your name?: ").lower()
    bid=int(input("What is your bid?: "))
    store[name]=bid
    others=input("Are there any other bidders? Type yes or no. ").lower()
    
    if others=="no":
        others_bid=True
        highest_bid(store)
    elif others=="yes":
        others_bid=False
    else :
        print("correct your input") 



  
    
    
