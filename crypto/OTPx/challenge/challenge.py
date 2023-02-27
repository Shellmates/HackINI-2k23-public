#!/usr/bin/env python3
import os
from config import FLAG , key


def xor(a, b):
    len_a = len(a)
    len_b = len(b)
    # Determine the length of the longer array
    max_len = max(len_a, len_b)
    # Determine the length of the shorter array
    min_len = min(len_a, len_b)
    # Repeat the shorter array to match the length of the longer array
    if len_a < len_b:
        a = bytearray((a * (max_len // min_len + 1))[:max_len])
    elif len_b < len_a:
        b = bytearray((b * (max_len // min_len + 1))[:max_len])
    # XOR the bytes and return the result as a bytes object
    result = bytearray(a_byte ^ b_byte for a_byte, b_byte in zip(a, b))
    return bytes(result)

def generate_pad(length):
    pad = os.urandom(length)
    return pad

def encrypt_OTP(text, pad):
    result = xor(text,pad)
    return result


def main():
    print('Welcome H4cK3r')
    while True:
        print('now choose your side:\n\t1) encrypt data\n\t2) get the flag\n\t3) exit')
        choice = input('>>').strip()
        if choice == "1": 
            print('What do you want to encrypt?')
            pt = input('> ').encode()
            pad = generate_pad(len(pt))
            print(encrypt_OTP(pt, pad))
            
        elif choice == "2":
            print(f"Did you really tought I would easily give you the flag, but since you asked for it here is the encrypted flag: ")
            print(f'The encrypted flag is: {encrypt_OTP(FLAG,key)}')
            
        elif choice == "3":
            print('Bye Bye')
            exit()
        else:
            print("you should choose one of the options")
   
 
if __name__ == "__main__":
        main()
