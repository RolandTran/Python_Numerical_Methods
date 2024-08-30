#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ch1_PS_git_Bash
print("Ch1_PS_git_Bash")


# In[ ]:


# ex 1.1.2 getting started with Python
print("Hello World!")


# In[ ]:


# 1.2 Python as a calculator
#  TRY IT! Compute the sum of 1 and 2.
1 + 2


# In[ ]:


# TRY IT! Compute 3×4 / (2^2+4/2).
(3*4)/(2**2 + 4/2)


# In[ ]:


# TRY IT! Compute 3 divided by 4, then multiply the result by 2, and then raise the result to the 3rd power.
3/4


# In[ ]:


_*2


# In[ ]:


_**3


# In[ ]:


import math


# In[ ]:


# TRY IT! Find the square root of 4.
math.sqrt(4)


# In[ ]:


# TRY IT! Compute the sin (pi/2)
math.sin(math.pi/2)


# In[ ]:


# TRY IT! Compute e^ log 10
math.exp(math.log(10))


# In[ ]:


# TRY IT! Compute e^3/4
math.exp(3/4)


# In[ ]:


# TRY IT! Use question mark to find the definition of the factorial function.
get_ipython().run_line_magic('pinfo', 'math.factorial')


# In[ ]:


# TRY IT
1/0


# In[ ]:


# TRY IT! 1/inf and inf * 2 to verify that Python handles infinity as you would expect
1/math.inf


# In[ ]:


math.inf *2


# In[ ]:


# TRY IT! Compute inf / inf
math.inf / math.inf


# In[ ]:


# TRY IT! Comput 2 + 5i
2 + 5j


# In[ ]:


complex(2,5)


# In[ ]:


pip list


# In[ ]:


# 1.5 LOGICAL EXPRESSIONS AND OPERATORS
print("1.5 LOGICAL EXPRESSIONS AND OPERATORS")


# In[ ]:


# TRY IT! Compute the logical expression for "Is 5 equal to 4" and "Is 2 smaller than 3"
5 == 4


# In[ ]:


2 < 3


# In[ ]:


# TRY IT! Assuming P is true, let us use Python to determine if the expression (P AND NOT(Q))
# OR (P AND Q) is always true regardless of whether or not Q is true. Logically, can you see why
# this is the case? First assume Q is true (Fig 1.17):
(1 and not 1) or (1 and 1)


# In[ ]:


# Now assume Q is false
(1 and not 0) or (1 and 0)


# In[ ]:


# TRY IT! Compute (1+3)>(2+5)
1 + 3 > 2 + 5


# In[ ]:


# WARNING! In Python’s implementation of logic, 1 is used to denote true and 0 for false. But
# because 1 and 0 are still numbers, Python will allow abuses such as: (3 > 2) + (5 > 4), which will
# resolve to 2.
(3 > 2) + (5 > 4)


# In[ ]:


# TIP! A fortnight is a length of time consisting of 14 days. Use a logical expression to determine
# if there are more than 100,000 seconds in a fortnight
(14*24*60*60) > 100000


# In[ ]:


# 1.6.2 PROBLEMS
print("1.6.2 Problems")


# In[ ]:


# 1. Print a message: Print "Python is fun!" using the Python Shell.
print("Python is fun!")


# In[ ]:


# 3. Import a fun module: Type import this in the Python Shell and read the Zen of Python
import this


# In[ ]:


# 5 Calculate a rectangle's area: Write a Python program to calculate the area of 
# a rectangle with width 7 and height 5. Remember, area = width * height.
width = 7
height = 5
area = width * height
print("The area of a rectangle with a width of", width, "and a height of", height, "is", area)


# In[ ]:


# 5a Calculate a rectangle's area: Write a Python program to calculate the area of 
# a rectangle with width 7 and height 5. Remember, area = width * height.
width = int(input("Enter an integer for the width: "))
height = int(input("Enter an integer for the height: "))
area = width * height
print("The area of a rectangle with a width of", width, "and a height of", height, "is", area)


# In[ ]:


# 5 Calculate a circle's area: Write a Python program to compute the area of a circle with radius 3. 
# Use the formula: area = π * radius^2.

import math

r = 3
area = math.pi * r**2
print(area)


# In[ ]:


# 6a Calculate a circle's area: Write a Python program to compute the area of a circle with radius 3. 
# Use the formula: area = π * radius^2.

import math

r = int(input("Enter an integer for the radius: "))
area = math.pi * r**2
print("The area of a circle with a radius of", r, "is", area)


# In[ ]:


#7  Find the sum of numbers: Write a Python program to find the sum of all numbers from 1 to 10
# list comprehension
total_sum_list_comp = sum([num for num in range(1, 11)])

print("Sum using list comprehension:", total_sum_list_comp)


# In[ ]:


#7a  Find the sum of numbers: Write a Python program to find the sum of all numbers from 1 to 10
# for loops
total_sum_for = 0
for num in range(1, 11):
    total_sum_for += num

print("Sum using for loop:", total_sum_for)


# In[ ]:


#7b  Find the sum of numbers: Write a Python program to find the sum of all numbers from 1 to 10
# while loops
total_sum_while = 0
num = 1
while num <= 10:
    total_sum_while += num 
    num += 1

print("Sum using while loop:", total_sum_while)


# In[ ]:


#7b  Find the sum of numbers: Write a Python program to find the sum of all numbers from 1 to 10
# while loops
a = int(input("Enter a start integer for the a: "))
b = int(input("Enter an end integer for the b: "))
total_sum_while = 0
num = a
while num <= b:
    total_sum_while += num 
    num += 1

print("Sum of integers from", a, "to", b,"is", total_sum_while)


# In[ ]:


#7c  Find the sum of numbers: Write a Python program to find the sum of all numbers from 1 to 10
# built in python sum function
total_sum_builtin = sum(range(1, 11))
print("Sum using built-in sum function:", total_sum_builtin)


# In[ ]:


#8 Multiply numbers in a list: Create a list of numbers [2, 3, 4] 
# and find the product of all the numbers in the list.

from functools import reduce

# Create the list of numbers
numbers = [2, 3, 4]

# Find the product of all the numbers in the list
product = reduce(lambda x, y: x * y, numbers)

# Print the result
print("The product of all the numbers in the list is:", product)


# In[ ]:


#9 Simple calculator: Create a simple calculator in Python 
# that can add, subtract, multiply, and divide two numbers.
# single digits

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main program
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        x = input("Enter first single-digit number (0-9): ")
        y = input("Enter second single-digit number (0-9): ")

        # Check if inputs are single digits
        if x.isdigit() and y.isdigit() and 0 <= int(x) <= 9 and 0 <= int(y) <= 9:
            x = int(x)
            y = int(y)

            if choice == '1':
                print(f"{x} + {y} = {add(x, y)}")

            elif choice == '2':
                print(f"{x} - {y} = {subtract(x, y)}")

            elif choice == '3':
                print(f"{x} * {y} = {multiply(x, y)}")

            elif choice == '4':
                print(f"{x} / {y} = {divide(x, y)}")
        else:
            print("Invalid input! Please enter single-digit numbers only.")
    else:
        print("Invalid choice! Please enter a valid operation number.")

# Run the calculator
calculator()


# In[ ]:


#9 Simple calculator: Create a simple calculator in Python 
# that can add, subtract, multiply, and divide two numbers.
# Function to add two numbers

def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main program
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

            if choice == '1':
                print(f"{x} + {y} = {add(x, y)}")

            elif choice == '2':
                print(f"{x} - {y} = {subtract(x, y)}")

            elif choice == '3':
                print(f"{x} * {y} = {multiply(x, y)}")

            elif choice == '4':
                print(f"{x} / {y} = {divide(x, y)}")
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    else:
        print("Invalid choice! Please enter a valid operation number.")

# Run the calculator
calculator()


# In[ ]:


# Function to add two numbers
def add(x, y):
    return x + y

x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))

print("The sum of ", x,"and", y, "is : ", add(x,y))

# Function to subtract two numbers
def subtract(x, y):
    return x - y

x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))

print("The difference of ", x,"and", y, "is : ", subtract(x,y))

# Function to multiply two numbers
def multiply(x, y):
    return x * y

x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))

print("The product of ", x,"and", y, "is : ", multiply(x,y))

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))

print("The quotient of ", x,"and", y, "is : ", divide(x,y))

print(add(9,3))
print(subtract(9,3))
print(multiply(9,3))
print(divide(9,3))



# In[ ]:


#9 Simple calculator: Create a simple calculator in Python 
# that can add, subtract, multiply, and divide two numbers.
# Function to add two numbers

def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main program
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print(f"{x} + {y} = {add(x, y)}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    elif choice == '2':
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print(f"{x} - {y} = {subtract(x, y)}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    elif choice == '3':
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print(f"{x} * {y} = {multiply(x, y)}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    elif choice == '4':
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print(f"{x} / {y} = {divide(x, y)}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    else:
        print("Invalid choice! Please enter a valid operation number.")

# Run the calculator
calculator()



# In[ ]:


#10 Convert temperature: Write a Python program to convert a temperature of 25 degrees Celsius to Fahrenheit.
# Use the formula: F = C * 9/5 + 32.

# temp in Celsius 
C = 25

def C_to_F_calc(C):
    F = C * (9/5) + 32
    return F

# convert C to F
F = C_to_F_calc(C)

# print F
print(f"{C} degress Celsius is equal to {F} degrees Farenheit.")


# In[ ]:


#10 Convert temperature: Write a Python program to convert a temperature of 25 degrees Celsius to Fahrenheit.
# Use the formula: F = C * 9/5 + 32.

# temp in Celsius 
C = 25

def C_to_F_calc(C):
    F = C * (9/5) + 32
    return F

# convert C to F
F = C_to_F_calc(C)

# print F
print(f"{C} degress Celsius is equal to {F} degrees Farenheit.")


# In[ ]:


#10b Convert temperature: Write a Python program to convert a temperature of 25 degrees Celsius to Fahrenheit.
# Use bthe formula: F = C * 9/5 + 32.

# temp in Celsius 
C = float(input("Enter an integer for the value of C: "))

def C_to_F_calc(C):
    F = C * (9/5) + 32
    return F

# convert C to F
F = C_to_F_calc(C)

# print F
print(f"{C} degress Celsius is equal to {F} degrees Farenheit.")


# In[ ]:


#10a Convert temperature: Write a Python program to convert a temperature of 25 degrees Celsius to Fahrenheit.
# Use the formula: F = C * 9/5 + 32.

# temp in Celsius 
C = 25

# convert C to F
F = C * (9/5) + 32

# print F
print(f"{C} degress Celsius is equal to {F} degrees Farenheit.")


# In[ ]:


#10a Convert temperature: Write a Python program to convert a temperature of 25 degrees Celsius to Fahrenheit.
# Use the formula: F = C * 9/5 + 32.

# temp in Celsius 
C = float(input("Enter an integer for the value of C: "))

# convert C to F
F = C * (9/5) + 32

# print F
print(f"{C} degress Celsius is equal to {F} degrees Farenheit.")


# In[ ]:


#11 Leap year check: Write a Python program to check if a year is a leap year. 
# A year is a leap year if it is divisible by 4 but not divisible by 100, 
# except if it is divisible by 400.

# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input: Year to check
year = int(input("Enter a year: "))

# Check and display result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[ ]:


# 12 Check if a number is even or odd
#1 Check if a number is even or odd:

print("Check if a nunmber is even or odd. ")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")


# In[ ]:


# 12a Check if a number is even or odd; using def
#1 Check if a number is even or odd:    print(number, "is an odd number.")

# Function to check if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Input: Number to check
number = int(input("Enter a number: "))

# Check and display result
if is_even(number):
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# In[ ]:


# Function to check if a number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

# Input: Number to check
number = int(input("Enter a number: "))

# Check and display result
result = check_number(number)
print(f"The number is {result}.")


# In[ ]:


#13a Check if a number is positive, negative, or zero

# Input: Number to check
number = int(input("Enter a number: "))
if number > 0: 
    print(number, " is a positive number")
elif number < 0:
    print(number, " is a negataive number.")
else:
    print(number, "is zero.")





# In[ ]:


#13b Check if a number is positive, negative, or zero

# Input: Number to check
try:
    number = int(input("Enter a number: "))

    # Check if the number is positive, negative, or zero
    if number > 0:
        print(number, "is a positive number.")
    elif number < 0:
        print(number, "is a negative number.")
    else:
        print(number, "is zero.")
except ValueError:
    print("You didn't enter a number.")


# In[ ]:


#14 Check if two numbers are both even

# Function to check if two numbers are both even
def are_both_even(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return True
    else:
        return False

# Input: Two numbers to check
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check and display result
if are_both_even(num1, num2):
    print(f"Both {num1} and {num2} are even numbers.")
else:
    print(f"One or both of the numbers are not even.")


# In[ ]:


#14a Check if two numbers are both even

# Input: Two numbers to check
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a % 2 == 0 and b % 2 == 0:
    print(f"Both {a} and {b} are even numbers.")
else:
    print(f"One or both of the numbers are not even.")


# In[ ]:


#14b Check if two numbers are both even

# Input: Number to check
try:
    # Input: Two numbers to check
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    # Check if the number is positive, negative, or zero
    if a % 2 == 0 and b % 2 == 0:
        print(f"Both {a} and {b} are even numbers.")
    else:
        print(f"One or both of the numbers are not even.")
except ValueError:
    print(f"You didn't one or two numbers, {a} and {b}.")


# In[ ]:


#14c Check if two numbers are both even

try:
    # Input: First number to check
    a = int(input("Enter the first number: "))
except ValueError:
    print("You didn't enter a valid number for the first input.")
    a = None

try:
    # Input: Second number to check
    b = int(input("Enter the second number: "))
except ValueError:
    print("You didn't enter a valid number for the second input.")
    b = None

# Proceed only if both inputs are valid numbers
if a is not None and b is not None:
    # Check if both numbers are even
    if a % 2 == 0 and b % 2 == 0:
        print(f"Both {a} and {b} are even numbers.")
    else:
        print(f"One or both of the numbers are not even.")


# In[ ]:


#15 Check if two numbers are both odd

try:
    # Input: First number to check
    a = int(input("Enter the first number: "))
except ValueError:
    print("You didn't enter a valid number for the first input.")
    a = None

try:
    # Input: Second number to check
    b = int(input("Enter the second number: "))
except ValueError:
    print("You didn't enter a valid number for the second input.")
    b = None

# Proceed only if both inputs are valid numbers
if a is not None and b is not None:
    # Check if both numbers are even
    if a % 2 == 1 and b % 2 == 1:
        print(f"Both {a} and {b} are odd numbers.")
    else:
        print(f"One or both of the numbers are not odd.")


# In[ ]:


#16 Guess the number game: Write a simple number guessing game 
# where the computer randomly chooses a number between 1 and 10, 
# and the player has to guess it.

import random

def guess_the_number():
    # Computer randomly chooses a number between 1 and 10
    number = random.randint(1, 10)
    
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    # Set a flag to indicate when the user has guessed correctly
    guessed_correctly = False

    # Loop until the player guesses the correct number
    while not guessed_correctly:
        # Ask the player to make a guess
        guess = int(input("Take a guess: "))
        
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
            guessed_correctly = True

# Run the game
guess_the_number()


# In[ ]:


#16a Guess the number game: Write a simple number guessing game 
# where the computer randomly chooses a number between 1 and 10, 
# and the player has to guess it.

def computer_guesses_number():
    print("Think of a number between 1 and 10, and I'll try to guess it!")
    
    low = 1
    high = 10
    feedback = ""
    
    while feedback != "c":
        # Computer makes a guess
        if low != high:
            guess = (low + high) // 2
        else:
            guess = low  # If low and high converge, this is the only possible number
        
        # Get feedback from the player
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if lfeedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay! I guessed your number, {guess}!")

# Run the game
computer_guesses_number()


# In[ ]:


#17a Square numbers: Write a Python program to print the square of each number from 1 to 5
# for Loop through numbers from 1 to 5
for x in range(1, 6):
    square = x**2
    print(f"The square of {x} is {square}.")


# In[ ]:


#17b Square numbers: Write a Python program to print the square of each number from 1 to 5
# while Loop through numbers from 1 to 5

y = 1

# Use a while loop to iterate through numbers from 1 to 5
while y <= 5:
    square = y ** 2
    print(f"The square of {y} is {square}.")
    y += 1  # Increment the number


# In[ ]:


#17c Square numbers: Write a Python program to print the square of each number from 1 to 5
# list comprehension numbers from 1 to 5

# List comprehension to create a list of squares from 1 to 5
squares = [a**2 for a in range(1, 6)]

# Print each square from the list
for i, square in enumerate(squares, start=1):
    print(f"The square of {i} is {square}.")
Counting vowels: Write a Python program that counts the number of vowels in the string "Hello, Python!".


# In[ ]:


#18 Counting vowels: 
# Write a Python program that counts the number of vowels in the string "Hello, Python!".

# String to check for vowels
string = "Hello, Python!"

# Define a list of vowels
vowels = "aeiouAEIOU"

# Initialize a counter for vowels
count = 0

# Loop through each character in the string
for char in string:
    if char in vowels:
        count += 1

# Print the number of vowels found
print(f"The number of vowels in the string is: {count}")


# In[ ]:


#19 Reverse a string: Write a Python program to reverse the string "Python".

# String to reverse
string = "Python"

# Reverse the string using slicing
reversed_string = string[::-1]

# Print the reversed string
print(f"The reversed string is: {reversed_string}")


# In[ ]:


#20 Find the largest number: Write a Python program that finds the largest number 
# in a list of numbers [5, 8, 2, 4, 7].

# List of numbers
numbers = [5, 8, 2, 4, 7]

# Find the largest number using the max() function
largest_number = max(numbers)

# Print the largest number
print(f"The largest number in the list is: {largest_number}")


# In[ ]:


#21 Create a multiplication table: Write a Python program to generate and
# print the multiplication table for the number 5.

# Number for which to generate the multiplication table
number = 5

# Print the multiplication table
print(f"Multiplication table for {number}:")

# Loop through numbers 1 to 20
for i in range(1, 21):
    result = number * i
    print(f"{number} x {i} = {result}")



# In[ ]:


#22 Factorial calculation: Write a Python program to find the factorial of 5. 
# Remember, factorial of n (n!) is the product of all positive integers less than or equal to n.

# Number to calculate the factorial of
number = 5

# Initialize factorial result to 1 (as factorial of 0 is 1)
factorial = 1

# Loop through each number from 1 to the given number
for i in range(1, number + 1):
    factorial *= i  # Multiply factorial by each number

# Print the factorial result
print(f"The factorial of {number} is: {factorial}")



# In[ ]:


#23  Draw a shape: Use the turtle module in Python to draw a square.


import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1)  # Set the speed of the turtle

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)  # Move the turtle forward
        t.right(90)             # Turn the turtle right by 90 degrees

# Draw a square with each side of length 100
draw_square(100)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()


# In[ ]:


#24 Sum of even numbers: Write a Python program to find the sum of all even numbers from 1 to 20.
# list comprehension
total_sum_list_comp = sum([num for num in range(2, 21,2)])

print("Sum using list comprehension:", total_sum_list_comp)


# In[ ]:


#24a Sum of even numbers: Write a Python program to find the sum of all even numbers from 1 to 20.
# for loops
total_sum_for = 0
for num in range(2, 21,2):
    print (num)
    total_sum_for += num
    num += 1

print("Sum using for loop:", total_sum_for)


# In[ ]:


#24b Sum of even numbers: Write a Python program to find the sum of all even numbers from 1 to 20.
# while loops
total_sum_while = 0
num = 2
while num <= 20:
    print(num)
    total_sum_while += num 
    num += 2

print("Sum using while loop:", total_sum_while)


# In[ ]:


#25 Simple interest calculation: Write a Python program to calculate the simple interest for a principal amount of $1000 
# at a rate of 5% per year over 3 years. Use the formula: 
# Simple Interest = (Principal * Rate * Time) / 100.

# Define the principal amount, rate of interest, and time
principal = 1000  # Principal amount in dollars
rate = 5          # Annual interest rate in percent
time = 3          # Time in years

# Calculate the simple interest using the formula
simple_interest = (principal * rate * time) / 100

# Print the result
print(f"The simple interest for a principal amount of ${principal} at a rate of {rate}% per year over {time} years is: ${simple_interest}")



# In[ ]:


#26 Draw a star: Use the turtle module to draw a 5-point star.

import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(2)  # Set the speed of the turtle

# Function to draw a 5-point star
def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)  # Angle for a 5-point star

# Draw a star with a specified size
draw_star(100)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()


# In[ ]:


#27 Calculate age: Write a Python program that calculates 
# your age based on your birth year (e.g., 2012) and the current year (e.g., 2024).


# Input your birth year
birth_year = int(input("Enter your birth year (YYYY): "))

# Input the current year
current_year = int(input("Enter the current year (YYYY): "))

# Calculate age
age = current_year - birth_year

# Print the result
print(f"You are {age} years old.")


