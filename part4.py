alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from cipher_art import logo



game = True

while game == True:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def ceaser(text_letter, shift_number, direction):
    alpha = ""
    for letter in text_letter:
        position = alphabet.index(letter)
        if direction == "encode":
            new_pos = position + shift_number
            if new_pos >= 26:
                new_pos = new_pos % 26
        elif direction == "decode":
            if position >= shift_number:
                new_pos = position - shift_number
            elif position < shift_number:
                new_pos = position + (26 - shift_number)
        new_letter = alphabet[new_pos]
        alpha += new_letter
    print(alpha)

  if shift > 26:
    shift_number1= shift % 26
  else:
    shift_number1 = shift

  yon = input("Would you like to try? ").lower()
  ceaser(text_letter=text, shift_number=shift_number1, direction = direction)
  if yon == "no":
    game = False
    print("See you Sonn!")
    
#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-3: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).