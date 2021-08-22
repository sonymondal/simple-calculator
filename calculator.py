# simple calculator 

# instructions head line
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("-------FOLLOW THE INSTRUCTIONS--------")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# rules of calculation
instructions = "A is for Addition,\n B is for Subtraction, \n C is for Multiplication, \n D is for Division,"
print(instructions)

# choose an option
print('Select A / B / C / D :')
option = input()

# choose a right options
if option == "A" or option == "a" or option == "b" or option == "B" or option == "c" or option == "C" or option == "D" or option == "d":
    print("Let's Calculate.....")

# for error 
else:
    print(" Sorry! You choose a wrong option.")
    exit()

# new instructions
print("-----------------------------------")
print("Always type large number at  first.")
print("-----------------------------------")


# enter first number
print("Enter first number: ")
num = input()
num1 = int(num)

# enter second number 
print("Enter second number: ")
num = input()
num2 = int(num)

# conditions of calculation 
# for addition
if option == "A" or option == "a":
    print("Sum of two numbers is", num1 + num2)

# for substraction
elif option == "b" or option == "B":
    print("Subtraction of two numbers is", num1 - num2)

# for multiplication
elif option == "c" or option == "C":
    print("Multiplication of two numbers is", num1 * num2)

# for division 
else:
    print("Division of two numbers is", num1 / num2)

