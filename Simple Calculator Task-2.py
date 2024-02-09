#* How to bulid a simple calculator *
# 1. Addition
# 2. substration
# 3. multiplication
# 4. Divison
print("select an operation to perform: ")
print("1. Addition ")
print("2. Substration ")
print("3. Multiplication ")
print("4. Division ")
operation= input()
if operation == '1':
    num1=input("Enter the first number:")
    num2=input("Enter the second number:") 
    print("the sum is" + str(int(num1) + int(num2)))
elif operation == '2':
    num1=input("Enter the first number:")
    num2=input("Enter the second number:")
    print("the difference is" + str(int(num1) - int(num2)))
elif operation== '3':
    num1=input("Enter the first number:")
    num2=input("Enter the second number:")
    print("the product is" + str(int(num1) * int(num2)))
elif operation == '4':
    num1=input("Enter the first number:")
    num2=input("Enter the second number:")
    print("the result is" + str(int(num1) / int(num2)))
else:
    print("Invaild input") 