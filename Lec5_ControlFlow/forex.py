##############################################
##              For Loop
############################################
"""
fruit = input(f'Please enter the name of a fruit here please: ')

for x in fruit:
    print(f'The current object in x that extracts the collection of fruit is: {x}')
"""
"""
for tempvar in range(100):
    print(f'The current value that\'s in the tempvar is {tempvar}')
"""
"""
movies = ['Star Wars', 'The Avengers', 'Harry Potter ', 'Lord of the Rings']

for m in movies:  # it iterates over a sequence and executes the code indented under the "for" clause for each element in the sequence
    print(f'One of my favorites movie is {m}')
else:  # the indented code below "else" will be executed when "for" has finished looping over the entire list (no "break" statement executed)
    print('This is the end of the list')

"""
"""
for i in range(100):
    pass  # => empty instruction or "no nothing"


"""
"""

for i in range(10):  # => from 0 (default, included) to 10 excluded
    print(i, end=' ')
# it prints:  0 1 2 3 4 5 6 7 8 9

"""
"""
for i in range(3, 9):  # => from 3 included to 9 excluded
    print(i, end=' ')
# it prints: 3 4 5 6 7 8

"""
"""
for i in range(3, 20, 3):  # => from 3 included to 20 excluded in steps of 3
    print(i, end=' ')
# it prints: 3 6 9 12 15 18

"""
"""
for i in range(8, -4 , -2):  # => from 8 included to -4 excluded in steps of -2
    print(i, end=' ')
# it prints: 8 6 4 2 0 -2
# 8 7 6 5 4 3 2 1 0 - 1 - 2 - 3
"""

##############################################
##              For Loop Break and Continue
##############################################
"""
## for ... continue -> it prints all letters of the string without 'o'
for letter in 'Python is so good':
    if letter == 'o':
        continue  # go to the beginning of the for loop and do the next iteration
    print(letter, end='')
"""
"""
## for ... break
sequence = [1, 5, 19, 3, 31, 100, 55, 34]
for item in sequence:
    if item % 17 == 0:
        print('A number divisible by 17 has been found! Breaking the loop...')
        break  # breaks out of the loop (executes the first instruction (if any) after the else block of code)
else:
    print('There is no number divisible by 17 in the sequence')
"""
"""
##############
# Example 1
##############
for x in range(15):
	print("The current number in x is:",x)

##############
# Example 2
##############

for x in range(10):
    print (x, end='')
"""
"""
# break - example

print("The break instruction:")
for i in range(1, 6):
	if i == 3:
		break
	print("Inside the loop.", i)
print("Outside the loop.")
"""


# continue - example

print("The continue instruction:")

for i in range(1, 6):

    if i == 3:

        continue

    print("Inside the loop.", i)

print("Outside the loop.")
