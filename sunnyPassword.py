import sys
import pwinput

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
        print("Passwords match, saving")
        break
    else :
        print("Passwords do not match")

with open("password.txt", "w") as f:
    f.write(passwordFirstTry)

