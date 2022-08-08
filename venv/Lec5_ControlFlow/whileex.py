##############################################
##              While Loop
############################################
"""
# we will store the current largest number here
largest_number = -999999999

# input the first value
number = int(input("Enter a number or type -1 to stop: "))

# if the number is not equal to -1, we will continue
while number != -1:
    # is number larger than largest_number?
    if number > largest_number:
        # yes, update largest_number
        largest_number = number
    # input the next number
    number = int(input("Enter a number or type -1 to stop: "))

# print the largest number
print("The largest number is:", largest_number)
"""
"""
#########################
# Example 1 without else
#########################

i = 0
while i < 10:

    print(f'The current number in i is {i}')
    i += 1

######################
# Example 2 with else
######################

i = 0
while i < 10:

    print(f'The current number in i is {i}')
    i += 1
else:
	print(f'the else statement will display the i that didnt make the loop which is {i}')

#################################
## While Loops
#################################

a = 10
## Infinite Loop, it prints 10 indefinitely

# while a:  #it tests the truthiness of a or bool(a) which is always True
#    print(a)

## Prints numbers from 10 to 1
while a:  # => "while a:" is equivalent to "while a > 0:"
    print(a)
    a -= 1
else:  # => executes the below block of code after finishing the while looop (and if no "break" statement has been executed)
    print('Finishing printing numbers. a is now 0')

## it prints only odd numbers between 1 and 20
a = 0
while a < 20:
    a += 1
    if a % 2 == 0:
        continue  # go the the beginning of the while loop
    print(f'Odd number {a}')  # it reaches this line only if the continue statement hasn't been executed

## it prints numbers greater than 2
a = 7
while a > 0:
    a -= 1
    if a == 2:
        break  # => it breaks out of the while loop and executes the next instruction after the while block of code
    print(a)

print('Loop ended.')
"""
"""


















########################################################################################
beatles = []
############################################################
print("Step 1:", beatles)
beatles.append('Paul McCartney')
beatles.append('Pete Best')
beatles.append('George Harrison')
beatles.append('Stu Sutcliffe ')
beatles.append('John Lennon')
############################################################
print("Step 2:", beatles)
beatles[1] = beatles[4]
print(beatles)

############################################################
print("Step 3:", beatles)
del beatles[3]
print(beatles)
############################################################

print("Step 4:", beatles)
del beatles [3]
print(beatles)

#########################################################
print("Step 5:", beatles)
beatles.insert(0, "Ringo Starr")
print(beatles)
print("The Fab", len(beatles))
"""
"""

class1 = [input(), input(),input(),input(),input()]
print(class1)
print("Please add one more student")
class1.append(input())
print(class1)
class1.append(int(input()))
print(class1[6])
class2 = ["John Smith", "Mary Miller"]
class1 = class2 + class1
print(class1)

"""