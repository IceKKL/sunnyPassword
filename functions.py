import os
import sys
import string
from mmap import error

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
    cipheredPassword = ""
    for char in text:
        cipheredPassword += chr(ord(char) + 5)
    return cipheredPassword

def caesarDecipher(text):
    decipheredPassword = ""
    for char in text:
        decipheredPassword += chr(ord(char) + -5)
    return decipheredPassword

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

    with open("passwords.txt", "r", encoding="utf-8") as file: # opens as read only
        for line in file:
            words = line.strip().split(" ")
            if words[0] == accountName and words[1] == chosenApp:
                masterPinInput = input("Input master pin, to unlock your password: ")
                if masterPinInput == masterPin:
                    print(caesarDecipher(words[2]))
                else:
                    print("Incorrect master pin")
                break
        else:
            print("No password found")

def save(accountName, passwordDestination, password):
    fileExists = os.path.isfile("passwords.txt") and os.path.getsize("passwords.txt") > 0
    with open("passwords.txt", "a", encoding="utf-8") as file: # open as append
        if fileExists:
            file.write("\n")
        file.write(f"{accountName} {passwordDestination} {caesarCipher(password)}")


