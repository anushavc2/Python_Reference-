print("*",end =' ')
print("*")

print("*" * 5)

print("* " * 5)

for i in range(5): #rows
    print("* " * 4) #columns

rows = int(input("Enter row"))
cols = int(input("Enter cols"))
for i in range(rows):
    print("* " * cols)

rows = int(input('Enter Rows: '))
for i in range(1, rows+1):
    for j in range(i):
        print("*", end = " ")
    print()

rows = int(input('Enter Rows: '))
for i in range(rows):
    for j in range(i+1):
        print("*" , end = " ")
    print()

#decreasing pattern
rows = int(input('Enter Rows: '))
for i in range(rows):
    for j in range(i,rows):
        print("*" , end = " ")
    print()

#for hill pattern
for i in range(rows):
    for j in range(i,rows):
        print(" " , end = " ")
    for j in range(i+1):
        print("*" , end = " ")
    for j in range(i):
        print("*" , end = " ")
    print()
        
#for iverted hill pattern
for i in range(rows):
    for j in range(i+1):
        print(" " , end = " ")
    for j in range(i,rows):
        print("*" , end = " ")
    for j in range(i,rows-1):
        print("*" , end = " ")
    print()
   