li = [10, 20, 30, 40, 57]


#square of a list
ref = [i ** 2 for i in li]
print(ref)


#add +5 to each element of list
print([i+5 for i in li])

#even numbers of a list
even = [i for i in li if i % 2 == 0]
print(even)

'''List comprehension
Syntax:
    [experssion for control variable in iterable object]
    [experssion for control variable in iterable object condition]'''


