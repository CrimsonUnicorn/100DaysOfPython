from logo import logo
print(logo)

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text,shift,direction):
  new_text=''
  for char in text:
    if(char in alphabet):
      shifted_position =alphabet.index(char)
      shifted_position +=shift
      shifted_position %=  len(alphabet) #0-25
      new_text +=alphabet[shifted_position]
    else:
      new_text+=char

  print(f"Here is encoded result: {new_text}")

def decrypt(text,shift,direction):
  new_text=''
  for char in text:
    if(char in alphabet):
      shifted_position =alphabet.index(char)
      shifted_position -=shift
      shifted_position %=  len(alphabet) #0-25
      new_text +=alphabet[shifted_position]
    else:
      new_text+=char

  print(f"Here is decoded result: {new_text}")

def ceaser(text,shift,direction):
  if(text=='decode'):
    shift = -shift
  new_text=''
  for char in text:
    if(char in alphabet):
      shifted_position =alphabet.index(char)
      shifted_position +=shift
      shifted_position %=  len(alphabet) #0-25
      new_text +=alphabet[shifted_position]
    else:
      new_text+=char

  print(f"Here is {direction}d result: {new_text}")

should_continue=True
while should_continue:
  text=input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
  message=input("Type Your Message:")
  shift=int(input("Type the shift number:"))


  ceaser(message,shift,direction=text)
  
  restart=input("Type 'Yes' if you want to go again. Otherwise, type 'No'.").lower()
  if restart == 'no':
    should_continue=False
    print("Goodbye")