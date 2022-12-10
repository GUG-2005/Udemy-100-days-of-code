from art import logo 
print(logo)

game = True

def auction(bid_amnt):
  hi_bid = 0
  winner = ""
  for name in bid_amnt:
    bid = bid_amnt[name]
    if int(bid) > hi_bid:
      hi_bid = bid
      winner += name
  print(f"The auction goes to {name} with the bid of {hi_bid}!")

bids = {}
while game == True:
  bidder = input("Who is the bidder? ")
  amnt = int(input("What is the amnt of bid? "))
  bids[bidder] = amnt

  yon = input("Are there any other bidders in the auction? ").lower()
  if yon == "no":
    auction(bids)
    game = False