retval = 0
num = 0
def collatz(number):
    if (number % 2 == 0):
        retval = number/2
        print(int(retval))
        return (int(retval))
    elif (number % 2 == 1):
        retval = 3 * number + 1
        print(int(retval))
        return (int(retval))
    else:
        return (0)

print("-1 exits, all other values are calculated")
num = int(input("Enter your number: "))
while (num != -1):
    collatz(num)
    num = int(input("Enter your number: "))
