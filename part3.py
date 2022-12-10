alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def ceaser(text_letter, shift_number, direction):
  alpha = ""
  for letter in text_letter:
    position = alphabet.index(letter)
    if direction == "encode":
        new_pos = position + shift_number
    elif direction == "decode":
        if position >= shift_number:
            new_pos = position - shift_number
        elif position < shift_number:
            new_pos = position + (26 - shift_number)
    new_letter = alphabet[new_pos]
    alpha += new_letter
  print(alpha)
   
ceaser(text_letter=text, shift_number=shift, direction = direction)
 
 #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.