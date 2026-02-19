#solution with basics
import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
chosen_num = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
  attemp = 10
elif difficulty == 'hard':
  attemp = 5

while attemp>0 :
  print(f"You have {attemp} attempts remaining to guess the number.")
  user_guess = int(input("Make a guess: "))
  if user_guess == chosen_num:
    print(f"You got it! The answer was {user_guess}.")
    attemp=0
  else:
    attemp = attemp - 1
    if user_guess>chosen_num:
      print("Too high.")
      print("Guess again.")
    else:
      print("Too low")
      print("Guess again.")
  if attemp == 0:
    print("You've run out of guesses. Refresh the page to run again.")
