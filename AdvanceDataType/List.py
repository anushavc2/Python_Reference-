#how to create the list

'''
List is advanced data type
Features:
1.In List we can store homogenous(Same Data Type) as well heterogenous(Different Data Type) type of data

2.List maintains order of insertion in the output so it is called ordered collection of data.

3.In List we can store duplicate values.

4.List is mutable
'''

li1 = [10,20,30, 'Code',True,66.7]
print(li1)
print(type(li1))

print(li1[1]) #index of element
print(li1[2]) #accessing specific element from list

li1[3] = 'MyCode'
print("After update:",li1)
