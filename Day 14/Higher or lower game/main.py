import random
from art import logo,vs
from game_data import data

def format_data(person):
  """Format the account data into printable form"""
  name = person["name"]
  description = person["description"]
  country = person["country"]
  return f"{name} , a {description}, from {country}"

def check_answer(guess, a_folloer_count, b_follower_count):
  """Take a user's guess and follower count and return if they got right """
  if a_folloer_count > b_follower_count:
    return guess == 'a'
  else:
    return guess == 'b'
# using XNOR gate
# X = a_follower_count>b_follower_count
# G = guess =="a"
# return (X and G) or (~X and G)



print(logo)
score =0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)
  if account_a==account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  guess=input("Who has more followers? Type 'A' or 'B' : ").lower()

  print("\n" * 20)
  print(logo)

  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  if is_correct:
    score+=1
    print(f"You're right. Current score:{score}")
  else:
    print(f"Sorry, that's wrong. Final score:{score}")
    game_should_continue = False