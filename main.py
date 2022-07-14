from art import logo

print(logo)
#Welcome to the secret auction program
print('Welcome to the secret auction program')

bidder_list = []

bidding_continue = True

while bidding_continue:

    #What the name
    get_name = input("What is your name?: ")
    #What is your bid?
    get_bid = input("What is your bid?: ")

    def add_bidder(name, bid):
        bidder = {}
        bidder["name"] = name
        bidder["amount"] = bid
        bidder_list.append(bidder)

    #Add bidder to list
    add_bidder(get_name, get_bid)

    def get_max_bid(list):
        max_bid = list[0]["amount"]
        max_bidder_name = list[0]["name"]
        for bidder in range(len(list)):
            if list[bidder]["amount"] > max_bid:
                max_bid = list[bidder]["amount"]
                max_bidder_name = list[bidder]["name"]
        max_bid_info = [max_bidder_name, max_bid]
        return max_bid_info
#Are there any other bidders? Yes or No
    any_other_bidder = input("Are there any bidder?: ")

    if any_other_bidder == "no":
        bidding_continue = False
    else:
        bidding_continue = True


# If yes, ask name, ask bid
winner = get_max_bid(bidder_list)
# If no, compare and get the highest bid
print("The Winner is {name} with a bid of ${bid_amount}".format(name = winner[0], bid_amount = winner[1]))
# 