################# Frozen Set Methods #########################
#print(dir(frozenset))
#print(help(frozenset))
"""
fs = frozenset(["Automation", 5.678, 892])
print(fs)
print(type(fs))
"""

### copy()
"""
fs = frozenset(["Automation", 5.678, 892])
fs2 = fs.copy()
print(f'This is the frozen set of the variable fs: {fs}')
print(f'This is the frozen set using the copy method of the first variable: {fs2}')
"""
### differnce()

"""
fs = frozenset(["Automation", 5.678, 892])
fs2 = frozenset(["Network" , 654, 10.45,892])
print(f'This is the frozen set of the variable fs and fs2 before using the differnce method: \n{fs}\n{fs2}')
print(f'This is the frozen set of the variable fs and fs2 using the differnce method: \n{fs.difference(fs2)}\n{fs2.difference(fs)}')
"""

### symmetric difference
"""
fs = frozenset(["Automation", 5.678, 892])
fs2 = frozenset(["Network" , 654, 10.45,892])
print(f'This is the frozen set of the variable fs and fs2 before using the symmetric differnce method: \n{fs}\n{fs2}')
print(f'This is the frozen set of the variable fs and fs2 using the symmetric differnce method: \n{fs.symmetric_difference(fs2)}\n{fs2.symmetric_difference(fs)}')
"""

### union()
"""

fs = frozenset(["Automation", 5.678, 892])
fs2 = frozenset(["Network" , 654, 10.45,892])
print(f'This is the frozen set of the variable fs and fs2 before using the union method: \n{fs}\n{fs2}')
print(f'This is the frozen set of the variable fs and fs2 using the union method: \n{fs.union(fs2)}\n{fs2.union(fs)}')

"""
### intersection
"""
fs = frozenset(["Automation", 5.678, 892])
fs2 = frozenset(["Network" , 654, 10.45])
fs3 = frozenset([892])
print(f'This is the frozen set of the variable fs and fs2 and fs3 before using the intersection method: \n{fs}\n{fs2}\n{fs3}')
print(f'This is the frozen set of the variable fs and fs2 using the intersection method: \n{fs.intersection(fs3)}\n{fs2.intersection(fs)}')
"""

### isdisjoint()
"""
fs = frozenset(["Automation", 5.678, 892])
fs2 = frozenset(["Network" , 654, 10.45])
print(f'This is the frozen set of the variable fs and fs2 before using the isdisjoint method: \n{fs}\n{fs2}')
print(f'This is the frozen set of the variable fs and fs2 using the isdisjoint method: \n{fs.isdisjoint(fs2)}\n{fs2.isdisjoint(fs)}')
"""

### issubset()
"""
fs = frozenset(["Automation", 5.678, 892])
fs2 = frozenset(["Network" , 654, 10.45])
fs3 = fs.copy()
print(f'This is the frozen set of the variable fs and fs2 and fs3 before using the issubset method: \n{fs}\n{fs2}\n{fs3}')
print(f'This is the frozen set of the variable fs and fs2 and fs3 using the issubset method: \n{fs.issubset(fs3)}\n{fs2.issubset(fs)}')
"""


### issuperset()
"""
fs = frozenset(["Automation", 5.678, 892])
fs2 = frozenset(["Network" , 654, 10.45])
fs3 = fs.copy()
print(f'This is the frozen set of the variable fs and fs2 and fs3 before using the issuperset method: \n{fs}\n{fs2}\n{fs3}')
print(f'This is the frozen set of the variable fs and fs2 and fs3 using the issuperset method: \n{fs.issubset(fs3)}\n{fs2.issubset(fs)}')

"""