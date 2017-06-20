#! python3
'''
This program takes a string and performs the same function
as the strip() string method, but uses regexes to do so.

If no other arguments are passed other than the string to strip,
whitespace characters are removed from the start and end of the string.

Otherwise, the characters specified in the second argument are removed from the string.
'''

import re

def regStrip(targetString, pattern=' '):
    ''' This function takes a target string and strips the 'pattern' from the target.
        if the default pattern (whitespace) is used, it is removed from both ends.'''

    if pattern == ' ':
        '''If a single argument is passed to the function,
        just strip the whitespace on both sides'''

        # find whitespace at front ^[ ]*
        charLeft = re.compile(r'^[%s]+' % pattern)
        # sub() it with '' to erase it.
        targetString = charLeft.sub('', targetString)

        # find whitespace at back [ ]$*
        charRight = re.compile(r'[%s]+$' % pattern)
        # sub() it with '' to erase it.
        targetString = charRight.sub('', targetString)

    else:
        '''If two arguments are passed to the function,
        remove all instances of the pattern from the string'''

        # find all patterns in string [pattern]*
        targetRegex = re.compile(r'%s*' % pattern)
        # sub() it with '' to erase it
        targetString = targetRegex.sub('', targetString)

    return targetString

print(regStrip("   test string with 3 spaces on each side   "))
print(regStrip("@@@test string with 3 at symbols on each side to remove@@@", '@'))
print(regStrip("This #has so#me# nonsen#se all# #u#p# in ###it.", '#'))
print(regStrip("SpamSpamBaconSpamEggsSpamSpam", 'Spam'))
