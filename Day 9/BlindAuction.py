from logo import logo
print(logo)

def find_highest_bidder(bidding_dictionary):
  max_bid=0
  max_bid_name=''
  for key in Bid_details:
    if(Bid_details[key]>max_bid):
      max_bid=Bid_details[key]
      max_bid_name=key
  print(f"The winner is {max_bid_name} with a bid of {max_bid}")
  # max(Bid_details, key=Bid_details.get)

Bid_details={}

again = True
while again:
  name = input("What is your name? ")
  bid = int(input("Enter your bid amount: $"))
  Bid_details[name]=bid

  add_people=input("Are there any other bidders? Type 'Yes' or 'No'\n").lower()
  if(add_people=='no'):
    again=False
    find_highest_bidder(Bid_details)
  elif(add_people=='yes'):
    print("\n" * 20)