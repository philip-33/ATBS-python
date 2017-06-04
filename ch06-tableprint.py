#! python3
# ch06-tableprint.py
'''
Write a function named printTable() that takes a list of lists of strings 
and displays it in a well-organized table with each column right-justified. 
Assume that all the inner lists will contain the same number of strings. 
For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):

#create list variable to hold longest item in each list
  colWidths = [0] * len(tableData)

#find the longest word in each list by storing the length of the largest one
  for x in range(len(tableData)):
    for sublist in tableData[x]:
      if len(sublist) > colWidths[x]:
        colWidths[x] = len(sublist)

# now that I have the longest string in each list, I can print the table correctly.
  for x in range(len(tableData[x])):
    for y in range(len(tableData)):
      print(tableData[y][x].rjust(colWidths[y]), end=' ')
    print('')

printTable(tableData)