n1 = int(input("Enter the First Number: "))
n2 = int(input("Enter the Second Number: "))

print("""Here are the operators: 
Addition: '+'
Substraction: '-'
Multiply: 'x'
Division: '/'
""")

operators = ['+', '-', 'x', '/']
while True:
    operator = input("Which Operator to choose: ")
    if(operator in operators):
        break
    else:
        print("Please enter a valid operator")

result = 0

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if(b == 0):
        return "Error! Division by zero."
    return a / b


if(operator == '+'):
    result+= add(n1, n2)
elif(operator == '-'):
    result+= subtract(n1, n2)
elif(operator == 'x'):
    result+= multiply(n1, n2)
else:
    result+= divide(n1, n2)

print(f"The result is: {result}")