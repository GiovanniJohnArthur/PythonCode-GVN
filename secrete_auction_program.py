import os
print('****** WELCOME TO THE SECRETE AUCTION *******')
def find_winner(bidders_details):
    highest_bid = 0
    winner = ""
    for bidder in bidders_details:
        bidding_price = bidders_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(bidders_details)
    print(f"The winner is {winner} with the highest bid of {highest_bid}")

bidders = {}

end_of_biding = False
while not end_of_biding:
    name = input('Enter your name: ')
    bid_price = int(input('Enter the bid price: '))
    bidders[name] = bid_price

    more_bidders = input("Are there more bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == 'no':
        end_of_biding = True
        find_winner(bidders)
    elif more_bidders == 'yes':
        os.system('cls')