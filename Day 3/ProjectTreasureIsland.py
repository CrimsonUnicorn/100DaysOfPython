# Treasure Island Game
#ascii art https://ascii.co.uk/art
print('''
      

     _.--""--._
    /  _    _  \
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}  
      
''')
print("********************************************")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input1=input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n ").lower()



if input1=="left":
    input2=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n ").lower()
    if input2 == "wait":
        input3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n ").lower()
        if input3 =="yellow":
            print("You found the treasure! You Win!")
        elif input3 == "red":
            print("It's a room full of fire. Game Over.")
        elif input3 == "blue":
            print("You enter a room of beasts. Game Over.")
    elif input2=="swim":
        print("Attacked by trout. Game Over.")
elif input1=="right":
    print("You fell into a hole. Game Over.")
    