cards = open("cards.txt").read().splitlines()
cards = [card.replace("-","") for card in cards]

# function that converts a binary into string
def binary_to_string(binary):
    string = ''
    for i in range(0, len(binary), 8):
        string += chr(int(binary[i:i+8], 2))
    return string

binary = ''
for card in cards:
    if card[0] == '4':
        binary += '0'
    else:
        binary += '1'

print(binary_to_string(binary))
