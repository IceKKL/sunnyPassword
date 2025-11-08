import os
import sys
import string
import pwinput

masterPin = "1234"

def contextMenu():
    print("What would you like to do?")
    print("1. Add a password")
    print("2. Read a password")
    userChoice = input("Choose one of the options: ")
    if userChoice == "1":
        addPassword()
    if userChoice == "2":
        checkPassword()

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

def addPassword():
    accountName = input("What is the name of your account? ")
    passwordDestination = input("What is the password for? ")
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
            save(accountName, passwordDestination, passwordFirstTry)
            print("Passwords match, saving")
            break
        else:
            print("Passwords do not match")

def checkPassword():
    accountName = input("What is the name of your account? ")
    chosenApp = input("What app do you want to check the password for? ")

    with open("passwords.txt", "r") as file: # opens as read only
        for line in file:
            words = line.strip().split(" ")
            if words[0] == accountName and words[1] == chosenApp:
                masterPinInput = input("Input master pin, to unlock your password: ")
                if masterPinInput == masterPin:
                    print(caesarDecipher(words[2]))
                break

def save(accountName, passwordDestination, password):
    with open("passwords.txt", "a") as file: # open as append
        file.write(accountName + " " + passwordDestination + " " + caesarCipher(password))


