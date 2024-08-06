mylist = ["apple", "banana", "cherry"]

print(mylist)

# List Length

mylist = ["apple", "banana", "cherry"]

print(len(mylist))

# type()

mylist = ["apple", "banana", "cherry"]

print(type(mylist))

# Access Items

mylist = ["apple", "banana", "cher"]

print(mylist[1])

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Note: The search will start at index 2
#  (included) and end at index 5 (not included).


# By leaving out the start value, the range will start at the first item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# By leaving out the end value, the range will
#  go on to the end of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Append Items
# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items
# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert( 3,"orange")
print(thislist)

# Extend List
# To append elements from another list to the current list, 
# use the extend() method.

hislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

thislist = ["apple", "banana", "cherry","ddddddd"]
del thislist[2]

print(thislist)


import list 

print(list.__package__)