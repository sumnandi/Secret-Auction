
from os import system
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

bidding_dict={}

val=True
while val:
  name=input("What is your name ?")
  bidd_amount=float(input("What's your bid ? \n$"))
  bidding_dict[name]=bidd_amount
  other_bidders=input("Are there any other bidders ? Type 'Yes' or 'No'")
  
  if other_bidders=="Yes":
    pass
  else:
    val=False

max_value=-100
bidder=""
print(f"The bidder Name along with their bidding amount is as follows: \n{bidding_dict}")
print("\n\n")
for key in bidding_dict:
  if bidding_dict[key]>max_value:
    max_value=bidding_dict[key]
    bidder=key

print(f"The winner is {bidder} with a bid of : $ {max_value}")
