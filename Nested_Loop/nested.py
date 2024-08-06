# Print this pattrn
# *******
# *******
# *******
# *******


# Print triangle
print("Square")

for i in range(1 , 7):
    for j in range(1 , i+1):
        print("*" , end="")
    print()


print("This is Triangle")

for i in range(1 , 7):
    for j in range(1 ,i):
      
        print("*" , end="")
    print()


print("Another Triangle")

n = 5

for i in range(n , 0 , -1):
    for j in range(i):
        print("*" , end="")
    print()


# Print Number in Triangle form

print("Triangle in Number")

for i in range(1 , 5):
    for j in range(1 , i + 1):
        print(j , end="")
    print()


# Another Triangle in Number

print("Another Triangle in Number")
n = 5

for i in range(n , 0 , -1):
    for j in range(i):
        print(j , end="")
    print()