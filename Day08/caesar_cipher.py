alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(text, shift):
    encoded_text = ''
    for letter in text:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                if i + shift > 25:
                    i = -1
                # print(alphabet[i + shift])
                for char in alphabet[i + shift]:
                    encoded_text += char
    print(encoded_text)

encrypt(text=text, shift=shift)