alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_letter, shift_number):
  alpha = ""
  for letter in text_letter:
    position = alphabet.index(letter)
    new_pos = position + shift_number
    new_letter = alphabet[new_pos]
    alpha += new_letter

  print(alpha)
   
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text_letter, shift_number):
  alpha = ""
  for letter in text_letter:
    position = alphabet.index(letter)
    if position >= shift_number:
          new_pos = position - shift_number
          new_letter = alphabet[new_pos]
          alpha += new_letter
    elif position < shift_number:
        new_pos = position + (26 - shift_number)
        new_letter = alphabet[new_pos]
        alpha += new_letter
        
  print(alpha)

if direction == "encode":
  encrypt(text_letter = text, shift_number = shift)
elif direction == "decode":
  decrypt(text_letter = text, shift_number = shift)
else:
  print("Check your input")
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.