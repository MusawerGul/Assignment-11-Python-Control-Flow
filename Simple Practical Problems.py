'''1. Design a Python program that calculates the total cost of items purchased by a customer based on the provided unit price and quantity, applying a discount of 10% if the total cost exceeds $1000.
unit_price=int(input('Enter Unit Price:'))
quantity=int(input('Enter Quantity:'))
def calculate_total_cost(unit_price, quantity):
    total_cost = unit_price * quantity
    if total_cost > 1000:
        total_cost *= 0.9  
    return total_cost
total_cost =calculate_total_cost(unit_price, quantity)
print("The total cost is:",total_cost)'''

'''2. Develop a program that prompts the user to enter their current temperature in Celsius and prints out whether they should wear a jacket (if temperature is below 20°C) or not.
temperature = int(input('Enter current temperature : '))

if temperature < 20:
    print("You should wear a jacket.")
else:
    print("The temperature is comfortable. No need for a jacket.")'''

'''3. Write a Python script that takes a user's input of three sides of a triangle and determines whether it is equilateral, isosceles, or scalene.
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 == side2 == side3:
    print("It's an equilateral triangle!")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("It's an isosceles triangle!")
else:
    print("It's a scalene triangle!")'''

'''4. Create a program that simulates a simple ATM machine. It should ask the user for their PIN, verify it, and then allow them to withdraw money if the balance is sufficient.

pin = 7860
balance = 1780
user_pin =int(input("Please enter your PIN: "))

if user_pin == pin:
    amount = int(input("Enter the amount you want to withdraw: "))
    
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful. Remaining balance: $",balance)
    else:
        print("Insufficient balance.")
else:
    print("Invalid PIN. Please try again.")'''

'''5. Develop a Python script that takes a user's input of a month (as a number) and prints out the number of days in that month.
month = int(input("Enter Month Numbr: "))

if month == 2:
    print("February has 28 days.")
elif month in [4, 6, 9, 11]:
    print("This month has 30 days.")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("This month has 31 days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")'''

'''6. Implement a program that takes a user's input of a year and month and prints out the number of days in that month, considering leap years.'''

year = int(input("Enter the year: "))
month = int(input("Enter Month Number: "))

if year % 4 == 0:
    leap_year = True
else:
    leap_year = False

if month == 2:
    if leap_year:
        print("February has 29 days in a leap year.")
    else:
        print("February has 28 days in a non-leap year.")
elif month in [4, 6, 9, 11]:
    print("This month has 30 days.")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("This month has 31 days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
