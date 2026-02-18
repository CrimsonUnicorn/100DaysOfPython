import random
from hangma_words import word_list 
from hangman_ascii import HANGMAN_PICS
from hangman_ascii import LOGO

print(LOGO)

lives = 6

word = random.choice(word_list)
print(word)

placeholder=""
word_length=len(word)
for letter in range(word_length):
    placeholder+="_"
print(placeholder)


game_over=False
correct_letters=[]


while not game_over:
    print(f"********* ${lives}/6 LIVES LEFT******")
    guess=input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display=""

    for letter in word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print("Word to guess: "+ display)

    if guess not in correct_letters:
        lives-=1
        print(f"You guessed{guess}, that's not in word.You lose a life.")
        if lives == 0:
            game_over=True       
            print(f"********IT WAS {word}! YOU LOSE********")



    if "_" not in display:
        game_over=True
        print("********You win!********")

    print(HANGMAN_PICS[lives])