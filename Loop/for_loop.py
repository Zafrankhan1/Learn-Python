    # For Loop fundamental 
# For loop work in range
# Start
# Stop
# step
# Syntax 
""""for i in range(start , stop , steip):
           statement
"""""


m = int(input("Enter your start number = "))
n = int(input("Enter your end number = "))



for m in range(m , n +1):
    print(m)


# now we make a program which show in reverse order


y = int(input("Enter your start number = "))
z = int(input("Enter your end number = "))



for y in range(y+1 ,z , -1):
    print(y-1)

    

# Print number form    1 to 30 if divisble by 3

for i in range(1 , 30+1):
    if i %3 == 0:
        print(i)
