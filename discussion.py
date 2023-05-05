# Python allows for user input, with this users can give inputs to the program
# [Section]The input() method allows users to give inputs to the program
# \n for next line
userName = input("Please enter your username: \n")

print(f"Hello {userName}! Welcome to the Python Course!")

num1 = int(input("\nEnter 1st number: "))
num2 = int(input("Enter 2nd number: "))
# the output is the concatination of num1 and num2
# How: Because the input() method assign any value as strings
# To use typecasting to convert to string into number and proceed with the operation
print(f"The sum of two numbers is {num1 + num2}")

# With the user inputs, user can give inputs for the program to be used to contriol the application using control structure
# [Section]Control Structure
'''
    This is the multiple comment in python
'''
'''
    Constrol sturcture can be devided into:
    a. selection structure (decision base on condition)- are used to execute specific set of statement
        base on whether a centern condition is true or false.
        1. If statement is the most commonly used selecture structure. The if-statement
            evauates a condition and execute a block of code if the condition is true.
                If-else Syntax:
                if<condition>:
                    statements to execute if the condition is true
                else:
                    statements to execute if the condition is false
    b. repetition structure (repeat code multiple times)- also known as loops. Use to repeat a
        block of code multiple times until a certain condition is met.
        1. For loop - use to iterate over a sequence of values
        2. while loop - use to repeat a block of code as long as a certain condition
            is true
'''
# [Section] If-else Statement
# If-else statements are used to choose between two or more code blocks depending of the condition

# Example 1: Declare a variable to use for the conditional statement
num3 = 75

if num3 >= 60:
    print("\nCongratulations! You Passed the senior program")
else:
    print("\nThank you. You are not qualified to the senior program.")
# Note that in Python, curly braces ({}) are not needed to distinguish the code blocks inside the if or else block.
# Hence, indentation are important as python use indentations to distuising parts of code as needed.
test_num = int(input("\nPlease enter a number: "))

if test_num > 0:
    print(f"{test_num} is a prositive number.")
elif test_num == 0:
    print(f"{test_num} is a zero.")
else:
    print(f"{test_num} is a negative number.")
# The elif is the shorthand for "else if" in other programming language

'''
    Mini Act:
Mini Exercise 1: 15 minutes
Create an if-else statement that determines if a number is divisible by 3, 5, or both. 
If the number is divisible by 3, print "The number is divisible by 3"
If the number is divisible by 5, print "The number is divisible by 5"
If the number is divisible by 3 and 5, print "The number is divisible by both 3 and 5"
If the number is not divisible by any, print "The number is not divisible by 3 nor 5"

Screenshot your code solution and result and paste it in our Lecture Discussion Link
'''
print("\nMini-Activity")
numact = int(input("Enter a number: "))
if numact % 3 == 0 and numact % 5 == 0:
    print(f"{numact} divisible by both 3 and 5.")
elif numact % 5 == 0:
    print(f"{numact} is divisible by 5.")
elif numact % 3 == 0:
    print(f"{numact} is divisible by 3.")
else:
    print(f"{numact} is NOT divisible by 3 nor 5.")


# Section: Loops
# Python has loops that can repeat block of code: While Loops are used to execute a set of statements as long as the condition is true
'''
    Syntax:
    while condition:
        code to be executed while the condition is true
        - the condition is a boolean expression that determines whether the loop should continue executing or not
'''
print("\nLoop")
i = 1

while i <= 5:
    print(f"Current count {i}")
    i += 1

while False:
    print('This is infinite loop!')

# To Exit an infinite loop, press ctrl + C

# Section: For Loops are used for iterating over a sequence
'''
    FOr ELement in sequence:
        code to be executed for each element in sequence
        - element is variable that will take on the value of each element in the sequence
        - Sequence any iterabke object, such as lists or strings that contains the elements we want to iterate
'''
print("\nLoop Example for fruits")
fruits = ['apple', 'banana', 'cherry']

# the 'in' keywords is used to specify the sequence or iterable object that you want to iterate over.

for fruit in fruits:
    print(fruit)

# range() function to create a sequence of numbers
print("\nRange Function")
for count in range(1, 5):
    print(count)
print("\nRange Function: printing values from 6 to 9")
for x in range(6, 10):
    print(f"The current value is {x}")
# This prints the values from 6 ro 9. Always remember that the range always prints to n-1.

print("\nRange Function: Specifying the increment of loops")
for x in range(6, 20, 2):
    print(f"The current value is {x}")
# This third argument can be added to specify the increment of loop.

# Enumerate() function to iterate over both elements and their indices in a sequence
# fruits = ['apple', 'banana', 'cherry']
print("\nEnumerate Function")
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Section: Break Statement - Used to stop the loop
print("\nBreak Function")
j = 1

while j < 6:
    print(j)
    if j == 3:
        break
    j += 1
'''
PROGRAM: SHOPPING CART

Create a program that allows a user to add items to their shopping cart. The user should be able to add items and their respective prices.
The program should also display the total cost of the items in the shopping cart.

Instructions:

	Create an empty dictionary called shopping_cart to hold the items and their respective prices.
	Use a while loop to allow the user to add items to the shopping cart.
	Inside the while loop, use the input() function to ask the user for the item name and price. The item name should be a string, and the price should be a float.
	Add the item and price to the shopping_cart dictionary.
	After the user adds an item, display a message to confirm that the item was added to the shopping cart.
	Ask the user if they want to add another item. If they do, continue the while loop. If they do not, exit the while loop.
	After the user is finished adding items, display the total cost of the items in the shopping cart.


Here is an example output of the program:

Welcome to the online store! Let's start shopping!

Please enter the name of the item: T-shirt
Please enter the price of the item: 20.00
T-shirt was added to your shopping cart.

Do you want to add another item? (y/n): y

Please enter the name of the item: Jeans
Please enter the price of the item: 50.00
Jeans was added to your shopping cart.

Do you want to add another item? (y/n): n

Thank you for shopping with us! Your total cost is $70.00

Note: Make sure to validate user input to ensure that the item name is not empty and that the price is a positive number.
If the user enters invalid input, display an error message and ask them to enter the information again.
Screenshot your solution code-based and results and paste in our sb lecture account

Grading:
  	First 1-2 submission without errors --> 100 points
		Second 3-5 submission without errors --> 90 points
		Third 5-10 submission without errors --> 85
		the rest without errors --> 80
		Late submission or submission with error --> 60
'''
print("\n==================================================================")
print("\nWelcome to the FPau Online Store! Let's start shopping!")
print("Items Available: ")
print("\n==================================================================")
print("Fresh Goods: \n1. Fish 1kg\t180.00 \n2. Meat 1kg\t200.00")
print("\nFrozen Goods: \n1. Nuggets\t300.00 \n2. TJ Hotdog\t140.00\n3. Ham\t350.00")
print("\nVegtables: \n1. Carrots\t50.00 \n2. Potatoes \t40.00\n3. Lettuce\t70.00")
print("\nToiletries: \n1. Detergent\t100.00 \n2. Bar Soap \t40.00\n3. Shampoo\t200.00")
print("\n==================================================================")
name = input("Costumer Name: ")

items = []
prices = []
total = 0


while True:
    ans = input("\nDo you want to add an item Y/N? ")
    if (ans.capitalize() == 'N'):
        print("Thank you for your visit.")
        break
    elif (ans.capitalize() != 'Y'):
        print("Invalid Input. Please try again on your next visit to our store.")
        break
    elif (ans.capitalize() == 'Y'):
        item = input(f"Please enter the name of the item: ")
        price = float(input(f"Please enter the price of the item: "))
        print(item, " was added to your shopping cart.")
        items.append(item)
        prices.append(price)

    print("\n==================================================================")
    print("Shopping Cart: ")

    for item in items:
        print(item, end=", ")

    total += price

    print(f"\nThank you for shopping with us, ", name, "! ")
    print(f"Your total cost is ₱{total}")
    print("\n==================================================================")
