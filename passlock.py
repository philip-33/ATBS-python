#! python3

'''
passlock.py

You probably have accounts on many different websites. 
It’s a bad habit to use the same password for each of them because 
if any of those sites has a security breach, the hackers will learn 
the password to all of your other accounts. It’s best to use password 
manager software on your computer that uses one master password to 
unlock the password manager. Then you can copy any account password 
to the clipboard and paste it into the website’s Password field.

The password manager program you’ll create in this example isn’t secure, 
but it offers a basic demonstration of how such programs work.
'''

'''
You want to be able to run this program with a command line argument 
that is the account’s name—for instance, email or blog. That account’s 
password will be copied to the clipboard so that the user can paste it 
into a Password field. This way, the user can have long, complicated 
passwords without having to memorize them.
'''

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python passlock.py [account] - copy accound password')
	sys.exit()

account = sys.argv[1]	#first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)
	