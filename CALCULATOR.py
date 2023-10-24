def add(no1, no2):

    return no1 + no2
 
# Function to subtract two numbers

def subtract(no1, no2):

    return no1 - no2
 
# Function to multiply two numbers

def multiply(no1, no2):

    return no1 * no2
 
# Function to divide two numbers

def divide(no1, no2):

    return no1 / no2
 

print("Please select operation-\n " 

        "1. Add\n" 

        "2. Subtract\n" 

        "3. Multiply\n" 

        "4. Divide\n")
 
 
# Take input from the user

select = int(input("Select operations from 1, 2, 3, 4 :"))

no_1 = int(input("Enter first number: "))

no_2 = int(input("Enter second number: "))
 

if select == 1:

    print(number_1, "+", no_2, "=",

                    add(no_1, no_2))
 

elif select == 2:

    print(no_1, "-", no_2, "=",

                    subtract(no_1, no_2))
 

elif select == 3:

    print(no_1, "*", no_2, "=",

                    multiply(no_1, no_2))
 

elif select == 4:

    print(no_1, "/", no_2, "=",

                    divide(no_1, no_2))

else:

    print("Invalid input")