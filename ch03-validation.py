'''
Add try and except statements to the previous project (collatz.py) to detect whether the user types in a noninteger string. 
Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). 
In the except clause, print a message to the user saying they must enter an integer.
'''

retval = 0
num = 1
number = 0

def collatz(number):
    try:
        int(number)
    except ValueError:
        print("You must enter an interger")
        return ('')
    number = int(number)
    if (number % 2 == 0):
        retval = number//2
        return (retval)
    elif (number % 2 == 1):
        retval = 3 * number + 1
        return (retval)
    else:
        return (0)

while (bool(num)):
    num = input("Enter your number: ")
    print(collatz(num))
