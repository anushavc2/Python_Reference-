user_data = input("Enter the values separated by comma")
print(user_data)
print(type(user_data))


#use split to convert string to list
li = user_data.split()
print(li)
new_li = []
for i in li:
    new_li.append(int(i))  # convert string to int

print(new_li)
