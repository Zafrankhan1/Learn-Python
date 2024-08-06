# How to put string in quatation

# In double Quatation

name = 'My name is "Zafran Khan"'
print(name)

# Single Quatation

name_1 = "My name is 'Zafran Khan'"
print(name_1)

# How to approach a string by while loop
 
string = "I love python"

l = len(string)

i = 0

while i<l:
    print(string[i] , end="")
    i +=1
print()

# How to reverse string

i = 1

l = len(string)

while i <=l:
    print(string[-i] , end="")
    i +=1
print()

# Using For Loop

for i in string:
    print(i , end="")
print()

# Reverse a String using For Loop

for i in string[ : : -1]:
    print(i , end="")
