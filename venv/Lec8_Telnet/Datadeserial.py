##############################################################

## Deserialize using JSON Example 1

##############################################################
"""
import json

with open('Contacts.json', 'rt') as dsfile:
    pobj = json.load(dsfile)
    print(type(pobj))
    print(pobj)
# The "load" deserializes from a JSON file

json_String =
{
    "Joey": [
        "New York",
        3478972555,
        "brother"
    ],
    "Fran": [
        "Florida",
        8812014478,
        "Wife"
    ],
    "Mom": [
        "California",
        3654781094,
        "Mom"
    ]
}


#This data is taken from the JSON prdouced file

obj = json.loads(json_String)
print(type(obj))
print(obj)
#The "loads" is used to deserialize from a JSON string

"""
##############################################################

## Deserialize using JSON Example 2

##############################################################
"""
import json

with open('Contacts.json', 'rt') as dsfile:
    pobj = json.load(dsfile)
    print(type(pobj))
    print(pobj)

# Tuple type was not preserved, it became a list instead of a tuple
# Json defines its own data type accordingly
# Some data types from python aren't compaatible with JSON
# Set is a data type that is NOT serializable at all in JSON, in that case use Pickle
"""


