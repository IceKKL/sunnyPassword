import os
import sys
import string
import pwinput

def caesarCipher(text):
    alphabet = string.ascii_lowercase # set used
    shifted_alphabet = alphabet[5:] + alphabet[:5] # by how many to shift the letter
    table = str.maketrans(alphabet, shifted_alphabet) # make a table of shifts
    return text.translate(table)

def caesarDecipher(text):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[-5:] + alphabet[:-5]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def password():
    while True:
        # both options used for testing, will change to only "pwinput" at the end
        # uses pwinput if the file is opened in a terminal
        if sys.stdin.isatty():
            passwordFirstTry = pwinput.pwinput()
            passwordSecondTry = pwinput.pwinput("Repeat Password: ")
        else:
            passwordFirstTry = input("Enter your password: ")
            passwordSecondTry = input("Repeat password: ")

        if passwordFirstTry == passwordSecondTry:
            print("Passwords match")
            passwordDestination = input("What is the password for? ")
            save(passwordFirstTry, passwordDestination)
            break
        else:
            print("Passwords do not match")

def save(password, passwordDestination):
    with open("passwords.txt", "a+b") as file: # open as append and binary
        try:
            file.seek(-2, os.SEEK_END) # set coursor to 2 bites before end of file
            while file.read(1) != b'\n': # read one sign, if it's not new line continue
                file.seek(-2, os.SEEK_CUR) # go another two
        except OSError: # if file is too short, set coursor to 0
            file.seek(0)
        lastLine = file.readline().decode()

        lineNumber = "" # get lineNumber from the file
        for char in lastLine:
            if char.isnumeric(): # as long as there are continuous numbers
                lineNumber += char
            else:
                break

        if lineNumber: # if lineNumber exists, add 1 to it
            newLineNumber = int(lineNumber) + 1
            file.write(("\n" + str(newLineNumber) + ". " + caesarCipher(password) + " | " + passwordDestination).encode("utf-8"))
        else: # else set it to 1
            newLineNumber = 1
            file.write((str(newLineNumber) + ". " + caesarCipher(password) + " | " + passwordDestination).encode("utf-8"))


