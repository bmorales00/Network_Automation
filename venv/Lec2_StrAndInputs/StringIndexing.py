####################################
## String Indexing, Operations and Slicing
####################################

## A string can be treated like a list of characters. Indexing starts from 0
language = 'Python 3'
language[0]  # => 'P'
language[1]  # => 'y'
language[-1]  # => '3'
language[-2]  # => ' '
"This is a string"[0]  # => 'T'

# language[100]          # => IndexError: string index out of range

# Cannot modify a string, it's immutable
# language[0] = 'J'      # => TypeError: 'str' object does not support item assignment


# You can find the length of a string
len("This is a string")  # => 16

## Strings can be concatenated with + and repeated with *
print('Hello ' + 'world!')  # => 'Hello world!'
print('Hello ' * 3)  # => 'Hello Hello Hello '
print('PI:' + str(3.1415))  # => Can concatenate only strings

## Slicing returns a new string
## start index is included, end index is excluded
movie = 'Star Wars'
movie[0:4]  # => 'Star' -> from index 0 included to index 4 excluded
movie[:4]  # => 'Star' -> start index defaults to zero
movie[2:]  # => 'ar Wars' -> end index defaults to the index of the last char of the string
movie[::]  # => 'Star Wars'
movie[2:100]  # => 'ar Wars -> slicing doesn't return error when using index out of range
movie[1:6:2]  # => 'trW' -> the 3rd index is the step (from index 2 included to 6 excluded in steps of 2)
movie[6:1:-1]  # => 'aW ra' -> from index 6 included to index 1 excluded in steps of -1 (backwards)
movie[::-1]  # => 'sraW ratS -> reverses the string