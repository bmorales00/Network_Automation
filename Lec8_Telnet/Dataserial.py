##############################################################

## Example of Showing Serialization

##############################################################
"""
contacts = {"Joey": ['New York', 3478972555, 'brother'],
            "Fran": ['Florida', 8812014478, 'Wife'],
            "Mom":['California', 3654781094, 'Mom'] }

with open ("Contacts.txt",'w') as file:    #This will give an error since a dict cannont be saved in  a txt file only
    file.write(contacts)                   # a string
"""
##############################################################

## Serialize and Deserialize using Pickle Example 1

##############################################################
"""
import pickle

contacts = {"Joey": ['New York', 3478972555, 'brother'],
            "Fran": ['Florida', 8812014478, 'Wife'],
            "Mom":['California', 3654781094, 'Mom'] }

with open ("Contacts.dat", 'wb') as file: #.dat is a binary file extension
    pickle.dump(contacts, file) #dump takes two arguments, the data and the file in which the data is stored in

with open ("Contacts.dat", 'rb') as file:
    dataobj = pickle.load(file)
    print(type(dataobj))
    print(dataobj)
"""

##############################################################

## Serialize and Deserialize using Pickle Example 2

##############################################################
"""
import pickle

contacts1 = {"Joey": ['New York', 3478972555, 'brother'],
            "Fran": ['Florida', 8812014478, 'Wife'],
            "Mom":['California', 3654781094, 'Mom'] }

contacts2 = {"Bill": ['Texas', 3478972555, 'Instructor'],
            "Danny": ['Arizona', 8812014478, 'Stepbrother'],
            "Dad":['Virginia', 3654781094, 'Dad'] }

contacts = (contacts1, contacts2)

with open ("Contacts.dat", 'wb') as file: #.dat is a binary file extension
    pickle.dump(contacts, file) #dump takes two arguments, the data and the file in which the data is stored in

with open ("Contacts.dat", 'rb') as file:
    dataobj = pickle.load(file)
    print(type(dataobj))
    print(dataobj)
"""

##############################################################

## Serialize using JSON Example 1

##############################################################
"""
import json

contacts = {"Joey": ['New York', 3478972555, 'brother'],
            "Fran": ['Florida', 8812014478, 'Wife'],
            "Mom":['California', 3654781094, 'Mom'] }

with open('Contacts.json', 'w') as file:
    json.dump(contacts, file, indent=4)  #Takes two args: python obj, file obj
#This creates a new file in JSON, it contains a string representation of the dict in JSON format

jsonString = json.dumps(contacts)
print(jsonString) #This produces the string representation of the dictionary encoded in JSON format
"""

##############################################################

## Serialize using JSON Example 2 and follows deserialize Example 2

##############################################################

import json

contacts = {"Joey": ('New York', 3478972555, 'brother'),
            "Fran": ('Florida', 8812014478, 'Wife'),
            "Mom":('California', 3654781094, 'Mom') }

with open('Contacts.json', 'w') as file:
    json.dump(contacts, file, indent=4)  #Takes two args: python obj, file obj
#This creates a new file in JSON, it contains a string representation of the dict in JSON format

jsonString = json.dumps(contacts, indent= 4)
print(jsonString) #This produces the string representation of the dictionary encoded in JSON format
