"""
var1 = int(input("Enter a number here:\n "))
var2 = int(input("Enter another number here:\n "))
var3 = int(input("Enter a third number here:\n "))
total_var = var1 +var2 +var3
print("The total value is: ", float(total_var))
print(type(total_var))


x = 56
y= "a string"
z = True
list_name = [x, y, z]
print(dir(list))
print(help(list))
print(list_name)
list_name.reverse()
print(list_name)

my_candy = ['Skittles' , 'M&M', 'Trident', 'Gummy Bears']
for snacks in my_candy:
	print(f'The candy I\'m currently eating is {snacks}')
"""
"""
print(dir(tuple))
print(help(tuple))

tuple_name = (True, "hello", 30)
print(tuple_name)
"""
beatles = ["Pual", "pete", "ge", 'st', "joh"]
beatles[1] = beatles[4]
print(beatles)
del beatles[3]
del beatles[3]
print(beatles)
beatles.insert(0, "Ringo Starr")
print(beatles)

hour = int(input("Starting time (hours): "))
minute = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

endmins = (minute+dura)%60
endhours = ((hour*60 + minute + dura)//60)%24
print(f'The current time now after {dura} minutes is {endhours}:{endmins}')

import datetime

#hour = int(input("Enter the hours: "))
#min = int(input("Enter the Minutes: "))
#dur = int(input("Enter the duration of minutes that passed: "))

#time = datetime.timedelta(hours=hour, minutes=min)
#duration = datetime.timedelta(minutes=dur)

#print(time + duration)

print(help(datetime.timedelta))