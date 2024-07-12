################# Dictionary Methods #########################
#print(dir(dict))
#print(help(dict))

### clear()
"""
class1 = {"Student 1":"Joey", "Student 2": "Gerard", "Student 3": "Tommy"}
class2 = {"Student 4": "Andy", "Student 5": "Tina", "Student 6": "Tamera"}
print(f'The dictionary for both class1 and class2 before using the clear method: \n{class1}\n{class2}')
class1.clear()
class2.clear()
print(f'The dictionary for both class1 and class2 after using the clear method: \n{class1}\n{class2}')
"""

### copy()
"""
class1 = {"Student 1":"Joey", "Student 2": "Gerard", "Student 3": "Tommy"}
class2 = {"Student 4": "Andy", "Student 5": "Tina", "Student 6": "Tamera"}
class3 = class1.copy()
class4 = class2.copy()
print(f'The dictionary for all the classes after using the copy method: \n{class1}\n{class2}\n{class3}\n{class4}')
"""

### get()
"""
class1 = {"Student 1":"Joey", "Student 2": "Gerard", "Student 3": "Tommy"}
class2 = {"Student 4": "Andy", "Student 5": "Tina", "Student 6": "Tamera"}
print(f'The principle is asking for the student {class1.get("Student 2")} from class 1 and {class2.get("Student 6")} from class 2 ')
"""

### items()
"""
class1 = {"Student 1":"Joey", "Student 2": "Gerard", "Student 3": "Tommy"}
class2 = {"Student 4": "Andy", "Student 5": "Tina", "Student 6": "Tamera"}
print(f'The items found in both dictionaries class 1 and 2 are: \n{class1.items()}\n{class2.items()}')
print(f'The amount of items in class 1 and 2 are: {len(class1.items())} items for class 1 and {len(class2.items())} items for class 2')
"""

### keys()
"""
class1 = {"Student 1":"Joey", "Student 2": "Gerard", "Student 3": "Tommy"}
class2 = {"Student 4": "Andy", "Student 5": "Tina", "Student 6": "Tamera"}
print(f'The keys found in both dictionaries class 1 and 2 are: \n{class1.keys()}\n{class2.keys()}')
"""
### pop()
"""
class1 = {"Joey": 24, "Gerard": 19, "Tommy": 32}
print(f'The current dictionary for class 1 correspond with the name of the student and their age as followed: {class1}')
print(f'The age of each student are as followed: Joey is {class1.pop("Joey")} years old, Gerard is {class1.pop("Gerard")} years old, and Tommy is {class1.pop("Tommy")} years old')
"""
### popitem()
"""
class1 = {"Joey": 24, "Gerard": 19, "Tommy": 32}
print(f'The current dictionary for class 1 is as followed: {class1}')
class1.popitem()
print(f'This is the current dictionary after using the pop item method {class1}')
class1.popitem()
print(f'This is the current dictionary after using the pop item again method {class1}')
class1.popitem()
print(f'This is the current dictionary after using the pop item again method {class1}')
"""

### setdefault()
"""
class1 = {"Joey": 24, "Gerard": 19, "Tommy": 32}
print(f'The current dictionary for class 1 is as followed: {class1}')
print(f'Darn the age for one of our students was never entered since she is new, now we don\'t know her age now' )
class1.setdefault("Sara")
print(f'This is how the dictionary looks like after the addtion of the new student without an age specificed {class1}')
"""

### values()
"""
class1 = {"Student 1":"Joey", "Student 2": "Gerard", "Student 3": "Tommy"}
class2 = {"Student 4": "Andy", "Student 5": "Tina", "Student 6": "Tamera"}
print(f'The names of the values found in both class 1 and 2 are:\n{class1.values()} from class 1 and {class2.values()} from class 2')


"""

### update()
"""
class1 = {"Joey": 24, "Gerard": 19, "Tommy": 32}
class1.update({"Sara" : 20})
print(f'We finally found the age for the newly added girl for class 1 its: {class1["Sara"]}')
print(f'So now the updated dictionary looks like: {class1}')
"""

