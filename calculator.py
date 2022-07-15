def addition(*k):
    return sum(k)
def subraction(n, b):
    return n-b
def multiplication(n, b):
    return n*b
def division(n, b):
    return n/b
def remainder(n, b):
    return n % b
def square(n, b):
    return n**b
def and1(n, b):
    return n and b
def or1(n, b):
    return n or b
a = int(input("Enter the number"))
b = int(input("Enter another number"))
print("operations:\n +\n -\n *\n /\n %\n**\nand\nor\n")
operation = input("pick an operation:")
if operation == '+':
    y = addition(a, b)
    c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
elif operation == '-':
    y = subraction(a, b)
    c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
elif operation == '*':
    y = multiplication(a, b)
    c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
elif operation == '/':
    y = division(a, b)
    c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
elif operation == '%':
    y = remainder(a, b)
    c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
elif operation == '**':
    y = square(a, b)
    c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
elif operation == 'and':
    y = and1(a, b)
    c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
for i in range(5*6*5*5*98*65**5):
    if c == 'y':
        b = int(input("Enter another number"))
        print("operations:\n +\n -\n *\n /\n %\n")
        operation = input("pick an operation:")
        if operation == '+':
            y = addition(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '-':
            y = subraction(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '*':
            y = multiplication(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '/':
            y = division(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '%':
            y = remainder(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '**':
            y = square(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == 'and':
            y = and1(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == 'or':
            y = or1(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        else:
            break
    elif c == 'n':
        a = int(input("Enter the number"))
        b = int(input("Enter another number"))
        print("operations:\n +\n -\n *\n /\n %\n**\n")
        operation = input("pick an operation:")
        if operation == '+':
            y = addition(a, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '-':
            y = subraction(a, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '*':
            y = multiplication(a, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '/':
            y = division(a, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '%':
            y = remainder(a, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == '**':
            y = square(a, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == 'and':
            y = and1(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
        elif operation == 'or':
            y = or1(y, b)
            c = input(f'The solution you get is {y},if you want to continue with {y} enter "y",or you want to start new calculaton enter "n"')
    else:
        break
