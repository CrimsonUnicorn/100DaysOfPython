#https://docs.python.org/3/library/random.html
import random
random.randint(1, 10)  # returns a random integer between 1 and 10 (inclusive)
random.random()     # returns a random float between 0.0 and 1.0
random.uniform(1.5, 10.5)  # returns a random float between 1.5 and 10.5

list=["apple", "banana", "cherry"]
random.choice(list)  # returns a random element from the list

rand = random.randint(1, 2)
if rand == 1:
    print("Heads")
elif rand == 2:
    print("Tails")