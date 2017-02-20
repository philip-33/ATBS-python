'''
Automate the Boring Stuff with Python - Chapter 4: Comma Code Project

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string
with all the items separated by a comma and a space, with and inserted before
the last item. For example, passing the previous spam list to the function
would return 

'apples, bananas, tofu, and cats'. 

But your function should be able to work with any list value passed to it.

'''

def commacode(listo):
	oxford = ''
	list_len = len(listo)

	for index, list_item in enumerate(listo, start=0):
		if (index < list_len - 1):
			oxford += list_item + ", "
		elif (index == list_len - 1):
			oxford += "and " + list_item
	return(oxford)

list1 = ['Harold', 'John', 'Shaw', 'Root', 'Fusco', 'Carter', 'Bear']
print(commacode(list1))
