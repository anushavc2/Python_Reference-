#Adding elemt into list

li =[50]
li.append(100)  #takes only 1 argument
#Appends element to the end of the list
print(li)  #[50, 100]

li.insert(0,500) #[500, 50, 100]
#insert (index,element) inserts elements at specific index and it doest return value 
#It takes only 2 arguments
print(li)

#pop(): This method removes and returns last element without any argument
ele = li.pop()
print(ele)
print(li)

# pop() with argument : It can remove specific index element from the list
ele1 = li.pop(0)
print(ele1)

li.append(700)

#remove(): Removes element from the list based on element (use when index element is not known) and wont return element 
li.remove(700)
print(li)

li.append(900)
print(li)
#del : removes the element by index and wont return
del li[1]
print(li)

del li  #Delets whole object from the memory
#print(li) error
