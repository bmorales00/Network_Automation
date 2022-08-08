################# Set Methods #########################
#print(dir(set))
#print(help(set))

### add()

"""
set_1 = {'Network Automation', 100, (57, "Python is Fun"), 3.14}
#set_2 = {'Networking', 384, (1.5, "Python is not Fun"), 29}
print(f'this is the set before using the add method {set_1}' )
print(id(set_1))
set_1.add(("This is a tuple added to a set", 123))
print(f'this is now the set after using the add method {set_1}')
print(id(set_1))

"""

### clear()

"""
set_1 = {'Network Automation', 100, (57, "Python is Fun"), 3.14}
print(f'this is the set before using the clear method: \n{set_1}' )
set_1.clear()
print(f'this is the set after using the clear method: \n{set_1}' )

"""

### copy()

"""
set_1 = {'Network Automation', 100, (57, "Python is Fun"), 3.14}
print(f'this is the set before using the copy method: \n{set_1}' )
print(id(set_1))
set_2 = set_1.copy()
print(f'this is the set after using the copy method using another variable: \n{set_2}' )
print(id(set_2))
"""

### discard()
"""
set_1 = {'Network Automation', 100, (57, "Python is Fun"), 3.14}
print(f'this is the set before using the discard method: \n{set_1}' )
set_1.discard(6989485)
print(f'this is the set after using the discard method with an element not originally in the set: \n{set_1}' )
set_1.discard('Network Automation')
print(f'this is the set after using the discard method with an element in the set: \n{set_1}' )
"""

### remove()


set_1 = {'Network Automation', 100, (57, "Python is Fun"), 3.14}
print(f'this is the set before using the remove method: \n{set_1}' )
set_1.remove(6989485)
print(f'this is the set after using the remove method with an element not originally in the set: \n{set_1}' )
set_1.remove('Network Automation')
print(f'this is the set after using the remove method with an element in the set: \n{set_1}' )


### pop()
"""
set_1 = {'Network Automation', 100, (57, "Python is Fun"), 3.14}
print(f'this is the set before using the pop method: \n{set_1}' )
set_1.pop()
print(f'this is the set after using the pop method with an element in the set: \n{set_1}' )
"""
### differnce()

"""
set_1 = {'Network Automation', 100, (57, "Python is not Fun"), 3.14}
set_2 = {'Networking', 384, (1.5, "Python is Fun"), (57, "Python is not Fun")}
print(f'this is the sets before using the differnce method \n{set_1}\n{set_2}' )
print(f'this is the set after using the differnce method\n{set_1.difference(set_2)}\n{set_2.difference(set_1)}')
"""

### symmetric differnce()

"""
set_1 = {'Network Automation', 100, (57, "Python is not Fun"), 3.14}
set_2 = {'Networking', 384, (1.5, "Python is Fun"), (57, "Python is not Fun")}
print(f'this is the sets before using the symmetric differnce method \n{set_1}\n{set_2}' )
print(f'this is the set after using the symmetric differnce method\n{set_1.symmetric_difference(set_2)}\n{set_2.symmetric_difference(set_1)}')
"""

### union()

"""
set_1 = {'Network Automation', 100, (57, "Python is not Fun"), 3.14}
set_2 = {'Networking', 384, (1.5, "Python is Fun"), (57, "Python is not Fun")}
print(f'this is the sets before using the union method \n{set_1}\n{set_2}' )
print(f'this is the set after using the union method\n{set_1.union(set_2)}\n{set_2.union(set_1)}')
"""

### intersection()

"""
set_1 = {'Network Automation', 100, (57, "Python is not Fun"), 3.14}
set_2 = {'Networking', 384, (1.5, "Python is Fun")}
print(f'this is the sets before using the intersection method \n{set_1}\n{set_2}' )
print(f'this is the set after using the intersection method\n{set_1.intersection(set_2)}\n{set_2.intersection(set_1)}')
"""

### isdisjoint

"""
set_1 = {'Network Automation', 100, (57, "Python is not Fun"), 3.14}
set_2 = {'Networking', 384, (1.5, "Python is Fun")}
set_3 = {'Networking', 384, (1.5, "Python is Fun"), 100}
print(f'this is the sets before using the isdisjoint method \n{set_1}\n{set_2}' )
print(f'this is the set after using the isdisjoint method\n{set_1.isdisjoint(set_2)}\n{set_3.isdisjoint(set_1)}')
"""

### update()
"""
set_1 = {'Network Automation', 100, (57, "Python is not Fun"), 3.14}
set_2 = {'Networking', 384, (1.5, "Python is Fun")}
print(f'this is the sets before using the update method \n{set_1}\n{set_2}' )
print(f'this is the set after using the update method\n{set_1.update(set_2)}\n{set_1}')
"""
### issubset

"""
set_1 = {'Network Automation', 100, (57, "Python is not Fun"), 3.14}
set_2 = {'Networking', 384, (1.5, "Python is Fun")}
set_3 = {'Network Automation', 100, (57, "Python is not Fun"), 3.14}
print(f'this is the sets before using the update method \n{set_1}\n{set_2}' )
print(f'this is the set after using the update method\n{set_1.issubset(set_3)}\n{set_2.issubset(set_1)}\n{set_3.issubset(set_2)}')
"""

