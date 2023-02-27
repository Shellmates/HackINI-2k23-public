import random


def generate_credit_card_number(prefix):
    credit_card_number = prefix
    for i in range(15):
        credit_card_number += str(random.randint(0, 9))
    return credit_card_number

def format_credit_card_number(number):
    formatted = ''
    for i in range(0, len(number), 4):
        formatted += number[i:i+4] + '-'
    return formatted[:-1]

# function that converts a string into binary
def string_to_binary(string):
    binary = ''
    for char in string:
        binary += bin(ord(char))[2:].zfill(8)
    return binary

flag = "shellmates{V15a_0r_M4573rC4rd_101}"
bin_flag = string_to_binary(flag)
for i in bin_flag:
    if i == '0':
        credit_card_number = generate_credit_card_number('4')
    else:
        credit_card_number = generate_credit_card_number('5')
    formatted_number = format_credit_card_number(credit_card_number)
    print(formatted_number)
