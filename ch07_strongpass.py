#! python3
'''
This program uses regexes (regi?) to check
the strength of a given password, then reports
the result to the user. Also, this module follows
PyLint conventions (except C0103).

A strong password:
-is at least eight characters long
-contains both uppercase and lowercase characters
-has at least one digit
(and my own addition)
-has at least one non-character, non-numeral symbol
'''
import re

userpass = input("Please enter a password to test: ")

charRegex = re.search('.{8,}', userpass)
lcaseRegex = re.search('[a-z]+', userpass)
ucaseRegex = re.search('[A-Z]+', userpass)
digiRegex = re.search('[0-9]+', userpass)
symbolRegex = re.search('[^a-zA-Z0-9]+', userpass)

print("Your password...")
if charRegex is None:
    print("Is too short (less than 8 characters)")
if None in [lcaseRegex, ucaseRegex]:
    print("Does not contain both uppercase and lowercase characters")
if digiRegex is None:
    print("Does not contain any numbers")
if symbolRegex is None:
    print("Does not contan any non-alphanumeric symbols, such as !@#$%^&*")

if not None in [charRegex, lcaseRegex, ucaseRegex, digiRegex, symbolRegex]:
    print("Is strong enough for general use.")
