num1 = int(input('Enter num1  :'))
num2 = int(input('Enter num2  :'))
choice = input('Enter Choice : Add-1, Sub - 2 , Mul - 3, Div = 4 , SquareOfNumber = 5 ,FloorDivivsion = 6 , Modulus = 7')
if choice == '1':
    print("Addition is:", num1 + num2)
elif choice == '2':
    print("Substraction is:", num1 - num2)
elif choice == '3':
    print("Multiplication is:", num1 * num2)
elif choice == '4':
    print("Division is:", num1 / num2)
elif choice == '5':
    print("Squareofnumber is:", num1 ** 2)
elif choice == '6':
    print("Floor Division is:", num1 // num2)
elif choice == '7':
    print("Modulus is:", num1 % num2)
else:
    print("Invalid choice....")
