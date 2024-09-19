def addition (a,b):
    return a+b

def substruction(a,b):
    return a-b

def multiplication(a,b):
    return a*b


def division(a,b): 
    return (a/b)

def modulus(a,b): 
    return a%b





def calculator():
    print('''Select operation:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Modulus
        ''')
    operation = input('Enter choice (1/2/3/4/5): ')
    first_number = input('Enter first number: ')
    second_number = input('Enter first number: ')

    if(int(operation) == 1):
        result = addition(int(first_number),int(second_number))
        print(result)
        return 


    if(int(operation) == 2):
        result = substruction(int(first_number),int(second_number))
        print(result)


    if(int(operation) == 3):
        result = multiplication(int(first_number),int(second_number))
        print(result)
        return


    if(int(operation) == 4):
        result = division(int(first_number),int(second_number))
        print(result)
        return



    if(int(operation) == 5):
        result = modulus(int(first_number),int(second_number))
        print(result)
        return



calculator()