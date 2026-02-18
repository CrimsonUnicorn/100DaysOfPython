import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
list=[rock, paper, scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice=random.randint(0,2)
print("You chose:"+ str(user_input) + list[(user_input)])
print("Computer chose:"+ list[computer_choice])

if user_input >=3 or user_input <0:
    print("You typed an invalid number, choose correctly!")
elif user_input == computer_choice:
    print("It's a draw!")

#Method using multiple elif statements    
# elif user_input == 0 and computer_choice == 1:
#     print("You lose!")
# elif user_input == 0 and computer_choice == 2:
#     print("You win!")
# elif user_input == 1 and computer_choice == 0:
#     print("You win!")
# elif user_input == 1 and computer_choice == 2:
#     print("You lose!")
# elif user_input == 2 and computer_choice == 0:
#     print("You lose!")
# elif user_input == 2 and computer_choice == 1:
#     print("You win!")

##Method using nested elif statements
# elif user_input == 0 :
#     if computer_choice == 1 :
#         print("You lose!")
#     else:
#         print("You win!")
# elif user_input == 1 :
#     if computer_choice == 2 :
#         print("You lose!")
#     else:
#         print("You win!")
# elif user_input == 2 :
#     if computer_choice == 0 :
#         print("You lose!")
#     else:
#         print("You win!")

#Method using greater than and less than operators
if user_input == 0 and computer_choice ==2 :
    print("You win!")
elif computer_choice == 0 and user_input ==2 :
    print("You lose!")
elif computer_choice > user_input :
    print("You lose!")
elif user_input > computer_choice :
    print("You win!")
elif user_input == computer_choice :
    print("It's a draw!")