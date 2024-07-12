##################################################################
##         User Defined Functions
##################################################################

"""
def plant_function(x):
    if x == "SPATHIPHYLLUS":
        print(f'YES!!! {x} is my favorite plant EVERRRRR')
    elif x == "spathiphyllus":
        print(f'I want a big SPATHIPHYLLUS not {x}')
    else:
        print(f'NOOOO {x} is not the plant at all!!!')
"""

##################################################################
##          User-Defined Fnctions with Parameters
##################################################################
"""
def fun_with_para(num_add):
    print(f'the addition of both floats is {num_add}')

x = float(input(f'Enter a float here: '))
y = float(input(f'Enter another float here: '))
z = x + y
fun_with_para(z)

"""
"""
def name_func(x, y, z):
    print(f'Hello my name is {x} {y} and I am enrolled in the class {z}')

firstName = input(f'What is your First Name: ')
lastName = input(f'What is your Last Name: ')
className = input(f'What is your Class Name: ')
name_func(firstName,lastName, className)
"""

"""
def dict_func(k1,v1,k2,v2,k3,v3):
    a_dict = {k1:v1,k2:v2,k3:v3}
    sum_of_v = v1 +v2 +v3
    print(f'\nThis is how the Dictionary looks like {a_dict}')
    print(f'\nThe sum of all the values in the Dictionary is {sum_of_v}')


######### Postional Argument Example ############
dict_func("Num1",5,"Num2",3,"Num3",100)


######### Keyword Argument Example ############
dict_func("x", v1 = 9,k2 = "y", v2 = 32, k3 ="z" , v3= 54 )
"""
"""
###########################################################
######### return without an expression Example ############
###########################################################

def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")
happy_new_year()

###########################################################
######### return with an expression Example ############
###########################################################
def my_function():
    return 15+5

x = my_function()

print(f'The return value of my function is {x}')
"""
###########################################################
######### *args Example ############
###########################################################
"""
def sum_Function(*x):
    total = []
    for temp in x:
        total += temp
    return total

print(sum_Function([0,1,2], ["A","b"], ["CSN", 563]))
"""
"""
###########################################################
######### **kwargs Example ############
###########################################################

def ip_add(**ip):
    print(f'The data type that **kwargs produces is {type(ip)}')
    for k, v in ip.items():
        print(f'\nThe ip address {v} is registered to {k}\n')
    print(ip)

ip_add(Station1 = "192.168.0.10" , Station2 = "192.168.0.12", Station3 = "192.168.0.14" )

"""
"""
###########################################################
######### Lambda Example ############
###########################################################


exp = lambda x: x * 5

print(exp(5))

## Similar to writing

def mult(x):
    return x*5

print(mult(5))

"""

###########################################################
######### Class Example ############
###########################################################
"""
class Dog():
    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
    def bark(self):
        print(f'{self.name} started to bark')
    def sleep(self):
        print(f'{self.name} started to sleep')
    def eat(self):
        print(f'{self.name} started to eat')
dog_One = Dog("Jake", "Doberman", "Black", "3 Years Old")
dog_Two = Dog("Leo", "Husky", "White", "7 Years Old")

#print(dog_One.name, dog_One.breed, dog_One.color, dog_One.age )

dog_One.bark()
dog_Two.bark()

"""