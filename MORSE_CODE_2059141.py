#Student name: AnilPanjiyar
#Student number :2059141

import os
import sys

MORSE_CODE = {
    "A": "-...", "B": ".-", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---",

    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
    "T": "-",

    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", ".": ".-.-.-", "0": "-----",
    "1": ".----",

    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "(": "-.--.",

    ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "#": ".-.-.", "-": "-....-", "_": "..--.-",

    '"': ".-..-.", "$": "...-..-", "@": ".--.-.", "?": "..--..", "!": "-.-.--"
}


# TO GET ONLY THE KEYS (LETTERS) FROM THE DICTIONARY
LETTERS = list(MORSE_CODE.keys())
# TO GET THE MORSE CODE VALUES FROM THE DICTIONARY
MORSE_VALUES = list(MORSE_CODE.values())

# FUNCTION TO GET USER INPUT


def get_input():
    # AN INFINITE LOOP FOR TAKING USER INPUT TO RUN AS MUCH AS USER WANT
    while True:  
        # GET WHICh MODE USER WANT TO 
        mode = input('Would you like to encode (e) or decode (d): ')
        if mode == 'e':
            choice = input(
                'Would you like to read from a file (f) or the console (c)? ')
            if choice == 'c':
                message = input('What message would you like to encode: ')
                print(encode(message))
                choice = input(
                    'Would you like to encode/decode another message (y/n)? ')
                if choice == 'y':
                    continue
                elif choice == 'n':
                    sys.exit('Thank you for using the program, goodbye!')
                else:
                    print('Invalid choice!')

            elif choice == 'f':
                filename = input('Enter filename: ')
                if file_exists(filename):
                    content = read_lines(mode, filename)
                    print(content)
                else:
                    print("File does not exist, Try Again!")

            else:
                print("Invalid choice!")

        elif mode == 'd':
            choice = input(
                'Would you like to read from a file (f) or the console (c)? ')
            if choice == 'c':
                message = input('What message would you like to decode: ')
                print(decode(message))
                choice = input(
                    'Would you like to encode/decode another message (y/n)? ')
                if choice == 'y':
                    continue
                elif choice == 'n':
                    sys.exit('Thank you for using the program, goodbye!')
                else:
                    print('Invalid choice!')

            elif choice == 'f':
                filename = input('Enter filename: ')
                if file_exists(filename):
                    content = read_lines(mode, filename)
                    print(content)
                else:
                    print("File does not exist, Try Again!")

            else:
                print("Invalid choice!")

        else:
            print('Invalid mode!')
            continue


# FUNCTION TO ENCODE MESSAGE (USER INPUT)
def encode(message):
    cipher = ''
    # CONVERTING USER INPUT TO UPPERCASE
    message = message.upper()
    # SAVING EACH CHARACTER IN USER INPUT IN A LIST
    message = list(message) 
    for i in message:
        # IF NO SPACE BETWEEN LETTERS, ADD SPACES
        if i != ' ':
            cipher = cipher + MORSE_CODE.get(i, i) + ' '
        else:
            cipher += ' '
    return cipher


# FUNCTION TO DECODE MESSAGE
def decode(message):
    decipher = ''
    message = message.split()

    for i in message:
        decipher += LETTERS[MORSE_VALUES.index(i)] + ''
    return decipher


# FUNCTION TO CHECK IF FILE EXISTS
def file_exists(filename):
    #  WE CAN  USE ABSOLUTE FILE PATH (c:\\users\\filename) OR JUST THE FILENAME (filename.txt)
    return os.path.exists(filename)


# FUNCTION TO READ LINES OF FILE
def read_lines(mode, filename):
    # OPEN FILE
    with open(filename, 'r') as file:       
        # READ FILE CONTENTS AND STORE THEM IN "CONTENT" VARIABLE
        content = file.read()
    # IF MODE IS encode (e), RETURN ENCODED MESSAGE
    if mode == 'e':
        return encode(content)
    elif mode == 'd':                       
        return decode(content)
    else:                                   
        return "Invalid mode!, Try again"
    # IF MODE IS NOT VALID...


def print_intro():
    print("Welcome to Wolmorse")
    print("This program encodes and decodes Morse code.")
    message = get_input()


# MAIN METHOD
def main():
    print_intro()

if __name__ == '__main__':
    main()
