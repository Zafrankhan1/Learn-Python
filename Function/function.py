# Syntax
# def functionName(param1, param2):

# Named function

def sum(a, b):
    
    print("Sum is =",a + b)

sum(2,2)

# Return Function


def subtract(a,b):
     
     c = a - b
     return f"Subtraction is = {c}"

result = subtract(5,2)

print(result)


def Demo_sum( a: int , b : int ) -> int :
       return a+b

jawab = Demo_sum(10,20)
print(jawab)