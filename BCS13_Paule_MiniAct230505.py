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
total = 0


while True:
    ans = input("\nDo you want to add an item Y/N? ")
    if (ans.capitalize() == 'N'):
        print("Thank you for your visit.")
        break
    elif (ans.capitalize() != 'Y'):
        print("Invalid Input. Please try again on your next visit to our store.")
    elif (ans.capitalize() == 'Y'):
        item = input(f"Please enter the name of the item: ")
        price = float(input(f"Please enter the price of the item: "))
        if (price <= 0):
            print("Invalid input. Please enter a positive number.")
            price = float(input(f"Please enter the price of the item: "))
        else:
            print(item, " was added to your shopping cart.")
        items.append(item)

    print("\n==================================================================")
    print("Shopping Cart: ")

    for item in items:
        print(item, end=", ")

    total += price

    print(f"\nThank you for shopping with us, ", name, "! ")
    print(total)
    print("\n==================================================================")
