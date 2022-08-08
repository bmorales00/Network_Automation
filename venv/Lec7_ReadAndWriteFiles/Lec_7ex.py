"""

file = open("Network_Scripting", 'r')

print(file.read())

######### The text file will contain ##########

# Hello there, the IP address in Workstation 1 is: 192.168.3.23



#################################################

print(file.closed)
file.close()
print(file.closed)



####################################################

###          With Statement

#####################################################


with open('Network_Scripting', 'r') as file:
    print(file.read())



####################################################

## With Example

####################################################

### Example1:

with open('assignment.txt', 'r') as tempfile:
	a_list = tempfile.read().splitlines()
	print(a_list)

### Example2:

with open('assignment.txt', 'r') as file:
	a_list = file.readlines()
	print(a_list)
print(help(file))
### Example3:

with open('assignment.txt', 'r') as file:
	for line in file:
	    print(line, end = '')


#############################################

## Write Method Examples

#############################################

with open('newfile.txt', 'w') as file:
    file.write(f'This is how you manipulate over a new file')
    file.write(f'\nThis')
    file.write(f'\nis')
    file.write(f'\nwriting in a new file')


############################################

##  Appending Example:

############################################


with open('exfile.txt', 'w') as file:
	file.write('This is the current contents in the example file for now\n')


#After is has been created then do the following changes:

with open('exfile.txt', 'a') as file:
	file.write('This is what happens with the content after using the appending mode \'a\'')



#########################################################

## Reading and Writing a file at the same time examples

#########################################################

###Example 1:

with open('exfile.txt', 'r+') as file:
    file.write('This is the new line added')
    print(file.read())



###Example 2: To add a file in a specific location using the cursor the seek method must be used.

with open('exfile.txt', 'r+') as file:
    file.seek(2)
    file.write('NEWER LINE ADDED FROM HERE')
    file.seek(0)
    print(file.read())


############################################################

### Exercise Answer

############################################################

with open('ipadd', 'r+') as file:
    #file.write('192.168.0.1\n192.168.0.1\n192.168.0.3\n192.168.0.4\n192.168.0.5')
    file.seek(23)
    file.write('2')
    file.seek(0)
    print(file.read())

############################################################

### CSV Files

############################################################

import csv

with open('IPadd.csv', 'r') as file:
    reader = csv.reader(file)
   # next(reader) #Skips the header or first line of the csv
    for row in reader:
        print(row)

############################################################

### CSV Files Writer Method

############################################################

import csv
with open('information.csv', 'a', newline='') as csvfile: #newline by default uses a \n
    #a for append is to add the new created text to end of the csv file
    writer = csv.writer(csvfile)
    csvdata = ('George', 22, 'London' )
    writer.writerow(csvdata)

############################################################

### CSV Files using different delimeters

############################################################

import csv
with open('passwd.csv', 'r') as file:
    reader = csv.reader(file, delimiter=':', lineterminator = '\n') #lineterminator is used to terminate lines
    # produced by the writer module. The reader recognises it and would ignore the lineterminator
    for a in reader:
        print(a)

############################################################

### CSV Files using dialects

############################################################

#Example:

import csv

#Reader
csv.register_dialect('Msign', delimiter='$', quoting=csv.QUOTE_NONE, lineterminator='\n')
with open('dialect', 'r') as f:
    reader = csv.reader(f, dialect='Msign')
    for row in reader:
        print(row)

#Writer
with open('dialect', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='Msign', lineterminator='\n')
    writer.writerow(('Root Beer', '5.00' ,'32-oz'))

############################################################

### Assignment Answer

############################################################

import csv
with open('assignment.txt','r') as f:
    reader = csv.reader(f, delimiter=':')
    mylist = list()
    for row in reader:
        mylist.append(row)

    print(mylist)
"""