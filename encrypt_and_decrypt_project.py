alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
    print(f"Encryption text: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabets[new_position]
        else:
            plain_text += char
    print(f"Decryption text: {plain_text}")

wanna_end = False
while not wanna_end:
    what_to_do = input("Enter 'E' for encryption and 'D' for decryption:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Enter the shift key:\n"))
    if what_to_do == "e":
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "d":
        decryption(cipher_text=text, shift_key=shift)
    play_again = input("Type 'yes' to continue and 'no' to exit:\n")
    if play_again == 'no':
        wanna_end = True
        print('BYE!..')
