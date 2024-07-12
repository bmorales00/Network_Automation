########### Sequential examples ###################
"""
print("Hello")
print("there")
print("this print")
print("comes after the one above")
print(f'On three let\'s do this from the top !!!!!!!!!!\n... {1}')
print(f'... {2}')
print(f'... {3}')
"""
################################
##         if examples
################################
"""
x = 50
y = 34
if x > y:    
    print(f'This will be printed because the statement x is greater than y is TRUE as:\nx represents {x} and y represents {y}')
"""
"""
a = 3
if 1 < a <= 9:
    print('a is greater than 1 and less than of equal to 9')
"""
"""
# equivalent to
if a > 1 and a <= 9:
    print('a is greater than 1 and less than of equal to 9')
"""
"""
# read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# we check if the second number is larger than current largest_number
# and update largest_number if needed
if number2 > largest_number:
    largest_number = number2

# we check if the third number is larger than current largest_number
# and update largest_number if needed
if number3 > largest_number:
    largest_number = number3

# print the result
print("The largest number is:", largest_number)

"""
"""
## 2nd Example: and operator -> it returns True if both expressions are True, False otherwise
if a % 2 == 0 and a % 3 == 0:
    print('Example 2: a is divisible by 2 and 3 (or by 6)')

## 3rd Example
if not (a % 2 and a % 3):  # the truthniness of an expression: a % 2 is equal to bool(a %2)
    print('Example 2: a is divisible by 2 and 3 (or by 6)')

"""
################################
##         if .. else examples
################################
"""
x = input("What is your name?  ")
y = input("What Class are you in?  ")

if y == "CSN 140":
    print(f'Your in the right class since I see the name {x} in the attendance sheet of {y}')
else:
    print(f'{x}, I do not see your name in my attendance sheet')
"""
"""
# read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# choose the larger number
if number1 > number2: 
    larger_number = number1
else: 
    larger_number = number2

# print the result
print("The larger number is:", larger_number)
"""
"""
goodweather = 85
badweather = 30
theweatherisgood = goodweather > badweather

if theweatherisgood:
    print(f'Lets go out for a walk since the weather is {goodweather} degrees fahrenheit')
else:
    print(f'Shoot! we can\'t go out since its {badweather} degrees fahrenheit and that\'s too cold')
"""
"""

## The truthiness of a variable
b = 0
if b:  # it test the truthiness of b or bool(b)
    print('The truthiness of b: True')
else:
    print('The truthiness of b: False')

my_str = 'some string'
if my_str:  # it test the truthiness of my_str or bool(my_str)
    print('The truthiness of my_str: True')
else:
    print('The truthiness of my_str: False')

name = 'Andrei'
## Pythonic version
print('Hello Andrei') if name == 'Andrei' else print('You are not Andrei!')

# equivalent to:
if name == 'Thomas':
    print('Hello Thomas')
else:
    print('You are not Thomas')
"""



######################################
## if ... elif ... else Statements
######################################

"""

number = 23
guess = int(input('Enter an integer: '))

if guess == number:
# New block starts here
    print(f'Yay!, you guessed the right number. It was the number {guess}')
# New block ends here
elif guess < number:
# Another block
    print('No, Please guess a little higher.')
# You can do whatever you want in a block ...
else:
	print('No, Please guess a little lower.')
# you must have guessed > number to reach here

"""

"""
a, b = 3, 5
if a < b:  # if a is less that b execute the indented block of code under the if clause, otherwise go and test the elif condition
    print('a is less than b')
elif a == b:  # if a is equal to b execute the indented block of code that fallows, otherwise execute the block of code under the else clause
    print('a is equal to b')
else:
    print('a is greater than b')
"""
"""
## or / and operators
your_age = 14
if your_age < 0 or your_age > 99:  # if ANY of the expression is True execute the indented block of code under the if clause
    print('Invalid age!')
elif your_age <= 2:
    print('You are an Infant')
elif your_age < 18:
    print('You are a child')
else:
    print('You are an adult')

"""

############################################
## if ... elif ... else nesting Statements
############################################
"""
a = 12

if a % 2 == 0:
    if a % 3 == 0:
        print(f'{a} is divisible by 2 and 3')

    else:
        print(f'{a} is divisible by 2 but not by 3 ')
else:
    print(f'{a} is not divisible by 2 or 3')

"""
"""
plant = input('Enter the name of the Plant Here: ')

if plant == "Spathiphyllum":
	print(f'Yes!!! {plant} is the best plant ever! ')
elif plant == "spathiphyllum":
	print(f'No!! I want a BIG Spathiphyllum not {plant}' )
else:
	print(f'Spathiphyllum! Not {plant}' )
"""