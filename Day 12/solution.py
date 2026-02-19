# solution using function and using "scope" concept
import random
import art
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual, turns):
  """Checks answer against guess , return number of turns left"""
  if user_guess>actual:
    print("Too high.")
    return turns - 1
  elif user_guess<actual:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {actual}")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  chosen_num = random.randint(1,100)

  turns = set_difficulty()

  user_guess=0
  while turns>0 or chosen_num != user_guess:
    print(f"You have {turns} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    turns = check_answer(user_guess, chosen_num, turns)
    if turns == 0:
      print("You've run out of guesses, you lose!")
      return
    elif user_guess!= chosen_num:
      print("Guess again")

game()