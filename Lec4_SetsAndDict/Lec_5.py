"""
Create a code based off of the scenario below, type it below the Sample Code:



Scenario:

Your task with two databases of information, one containing a list of animals and another containing a list of bugs. Your job is to transfer the existing list of animals to a new container list, then erasing the elements of the existing bug list and lastly in the new list of animals, adding a new element called "Bear"

Sample Code:
Hint: Remember the Methods from class
oldAnimalList = ["Dog", "Cat", "Snake", "Parrot", "Tiger"]
bugList = ["Beetle" ,"Lady Bug", "Bee", "Moth" , "Tarantula" ]
newAnimalList =
"""
"""
oldAnimalList = ["Dog", "Cat", "Snake", "Parrot", "Tiger"]
bugList = ["Beetle" ,"Lady Bug", "Bee", "Moth" , "Tarantula" ]

newAnimalList = oldAnimalList.copy()
bugList.clear()
newAnimalList.append("Bear")

print(newAnimalList)
"""
"""
var1 = int(input("Please enter the first integer here: "))
var2 = int(input("Please enter another integer here: "))
totalVar = var1 + var2
print(f'The totalVar which represents the number {totalVar} is greater than 10, that is: {totalVar > 10}')
print(f'The totalVar which represents the number {totalVar} is equal to 10, that is: {totalVar == 10}')
print(f'The totalVar which represents the number {totalVar} is less than 10, that is: {totalVar < 10}')

"""
"""

var1 = float(input("Please enter the first float here: "))
var2 = float(input("Please enter another float here: "))

total = var1 + var2
diff = var1 - var2
prod = var1 * var2
quot = var1 / var2

print(f'\nThe total of both floats is {total}')
print(f'\nThe difference of both floats is {diff}')
print(f'\nThe product of both floats is {prod}')
print(f'\nThe quotient of both floats is {quot}\n\nThat\'s all, folks!')

"""

"""

fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")
fullName = fname + ' ' +   lname
print(f'So your first name is {fname} and your last name is {lname}, so that means your full name is: {fullName}')
print(f'So your name backwards looks like this: {fullName[::-1]}')

"""

"""
hour = int(input("Starting time for (hours) is: "))
minute = int(input("Starting time for (minutes) is: "))
dura = int(input("The duration in (minutes) is: "))

endingmin = (minute+dura)%60
endinghour =((hour*60+ minute+dura)//60)%24
print(f'The current time {hour}:{minute} after {dura} minutes is {endinghour}:{endingmin}')
"""
"""

#this_is_a_dict = {"Student 1": "Josh", "Height": "6ft/2in"}
#print(this_is_a_dict["Height"])

class1 = {"Student 1":"Joey", "Student 2": "Gerard", "Student 3": "Tommy"}

class2 = {"Student 4": "Andy", "Student 5": "Tina", "Student 6": "Tamera"}

print(f'The amount of items in class 1 and 2 are: {len(class1.items())} items for class 1 and {len(class2.items())} items for class 2')


print(f'The items found in both dictionaries class 1 and 2 are: \n{class1.items()}\n{class2.items()}')
"""

