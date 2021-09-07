# Simple Calculator by Sony [First Project]

print("\n\tPYTHON SIMPLE CALCULATOR")
instraction = "Read the rules carefully:\n 1. A is for Addition.\n 2. B is for Subtraction.\n 3. C is for Multiplication.\n 4. D is for Division."
print(instraction)

# Addition function
def Addition(x, y):
    return x + y
# Subtraction function
def Subtraction(x, y):
    return x - y
#Multiplication function
def Multiplication(x, y):
    return x * y
#Division function
def Division(x, y):
    return x / y

# enter your option
option = input("Choose a option: ")
option = option.upper()

# Check if option is valid or not 
def checkOption(x):
    if option == "A" or option == "B" or option == "C" or option == "D":
        
        # collect input from user
        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))
        
        # calculation function
        def calculation(x, y):
           if option == "A":
               print(f"Addition of {firstNumber} & {secondNumber} is {firstNumber + secondNumber}") # print addition of numbers
           elif option == "B":
               print(f"Subtraction of {firstNumber} & {secondNumber} is {firstNumber - secondNumber}") # print subtraction of numbers
           elif option == "C":
               print(f"Multiplication of {firstNumber} & {secondNumber} is {firstNumber * secondNumber}") # print multiplication of numbers
           else:
               print(f"Division of {firstNumber} & {secondNumber} is {firstNumber / secondNumber}") # print division of numbers
       
        calculation(firstNumber, secondNumber)
    
    # if option is invalid then print this
    else:
        print("Invalid Option")
checkOption(option)
