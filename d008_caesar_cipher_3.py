alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(input_text, shift_amount, chosen_direction):
  print_text = ""
  if chosen_direction == "decode":
    shift_amount *= -1
  for letter in input_text:
    position = alphabet.index(letter)
    # if chosen_direction == "encode":
    #   new_position = position + shift_amount
    # elif chosen_direction == "decode":
    #   new_position = position - shift_amount
    # if chosen_direction == "decode":
    #   shift_amount = -abs(shift_amount)
    new_position = position + shift_amount
    print_text += alphabet[new_position]
  print(f"The {chosen_direction}d text is {print_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)