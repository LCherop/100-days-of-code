from os import system

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bids = {}

end_bidding = False
highest_bid = 0
highest_bidder = []

system('cls')
while not end_bidding:
    print(logo)
    print("Welcome to todays Blind Auction! Please enter your details:")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    
    add_bidder = input("Are there any other bidders? Type Y or N ")
    
    if add_bidder == "N":
        end_bidding = True
        system('cls')
    else:
        system('cls')

for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        highest_bidder = [key,highest_bid]

print(f"The winner is {highest_bidder[0]} with a bid of ${highest_bidder[1]}")