# password_cracker
# Jack Burns
# October 2020

A password cracker capable of performing dictionary and brute force attacks

Usage: python3 cracker.py [input hashes.txt] [optional input guesses.txt]
       where guesses can be a list of plain text passwords.
       
This program takes in password hashes that are in the format: username:$algorithm$salt$hash (A typical hash for a /etc/shadow file).
It can then hash a list of password guesses using the algorithm and salt contained in the password hash, and check it against the hash to crack.
The other option would include no input guess file, but rather initiate a brute force attack.
The character set and the length of the password can be directly edited for a brute force attack, as it can become very slow.

If a password is cracked, the program outputs the following message:
"Password for [username] cracked!
username:password"
