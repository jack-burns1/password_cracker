# Author: Jack Burns
# October 2020
# cracker.py
# A program that takes in a list of password hashes and
# Can either check them against another inputted list of guesses,
# or crack them with brute force.
# Hashes must be in the format username:$algo$salt$hash

import sys
import array
import crypt
import itertools

# Sets of characters to use in a brute force attack
alphaNum = "abcdefghijklmnopqrstuvwxyz0123456789"
num = "0123456789"
alpha = "abcdefghijklmnopqrstuvwxyz"

# Parse through the input file of guesses and check each 
# guess against the current hash
def check_password(salt, hashed, username):
    passwords = sys.argv[2]

    with open(passwords, "r") as fp:
        newline = str(fp.readline()).rstrip()
        while newline:

            if hashPass(newline, salt, hashed, username):
               return

            newline = str(fp.readline()).rstrip()

# Uses the salt and algorithm to hash a given string,
# and checks it against the hashed password.
# Prints the username:password if found
def hashPass(newline, salt, hashed, username):
    check = crypt.crypt(newline, salt=salt)
    if check == hashed:
       print("Password for", username, "cracked!")
       print(username + ":" + newline)
       return True
    return False

# Recursively check password with selected set of chars 
def brute_force(guess, salt, hashed, username):
    global num
    global alphaNum
    global alpha
    passLength = 6 # Set how long password is
    chars = alphaNum #change which set of chars to use
    if (len(guess) == passLength):
        return

    for i in chars:
       newguess = guess + i
       if hashPass(newguess, salt, hashed, username):
          return
       brute_force(newguess, salt, hashed, username)
       
# Check if program was run properly
if len(sys.argv) > 3 or len(sys.argv) < 2:
    print("Usage: cracker.py [hashed passwords] [optional password guesses]")
    print("If option two is blank, it is a brute force attack")

inFile = sys.argv[1]

try:
    with open(inFile) as fp:
        line = str(fp.readline())
        while line:
            username = ""
            algo = ""
            salt = ""
            hashed = ""

            # Parse hash for username/hash
            username = line.split(':')[0]
            hashed = line.split(':')[1]

            if hashed[0] == "$":
             # Find the salt and algorithm
              salt = "$".join(hashed.split("$", 3)[:3])
              print(salt)

              if len(sys.argv) == 3:
                check_password(salt, hashed, username) # check against a list
              else: brute_force("", salt, hashed, username) # check with brute force
            print("done")
            line = fp.readline()
except:
    print("Something went wrong reading hashes.")
    print("Are you sure they are formatted correctly?")


