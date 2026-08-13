#Do not revisit the lecture

import hashlib
import random

banned = ["password", "123456", "qwerty", "111111", "abc123", "letmein"]


def checkPassword(pw):
    print("checking password...", pw)  #testing

    if len(pw) < 4:
        print("too short")
        return False

    for b in banned:
        if b in pw:
            print("bad password found in list")
            return False

    return True


def hashIt(pw):
    # Encrypt
    h = hashlib.md5(pw.encode())
    return h.hexdigest()


def makeRandomPassword():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    newpw = ""
    for i in range(8):
        newpw = newpw + random.choice(letters)
    return newpw


# main.OIL

pw = input("Enter your password: ")

good = checkPassword(pw)

if good == True:
    print("Password is good!")
else:
    print("Password is bad, try again")

myhash = hashIt(pw)
print("your password hash is:", myhash)

