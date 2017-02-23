'''
Imagine that a vanquished dragon’s loot is represented as a list of strings like this:


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the inventory 
parameter is a dictionary representing the player’s inventory (like in the previous 
project) and the addedItems parameter is a list like dragonLoot. The addToInventory() 
function should return a dictionary that represents the updated inventory. Note that 
the addedItems list can contain multiples of the same item. Your code could look
something like this: (code added below)

The previous program (with your displayInventory() function from the previous project) 
would output the following:

Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
'''

def addToInventory(inventory, addedItems):
    # step through loot to add
    for l in addedItems:
    	# is loot (key) to add already in the list?    	
    	if l in inventory.keys():
    		#if so, add 1 to the current total (value) of the loot already in the list
    		inventory[l] += 1
    	else:
    		#if not, add the loot (key) name to the end of the list, and set the count (value) to 1
    		inventory[l] = 1
    return(inv)

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():

        print(k + ": " + str(v))
        item_total += v

    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)