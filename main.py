def add(n1,n2):
    print(f"Result= {n1+n2}")
    return

def subtract(n1,n2):
    print(f"Result= {n1-n2}")
    return

def multiply(n1,n2):
    print(f"Result= {n1*n2}")
    return

def divide(n1,n2):
    if n2==0:
        print("Cannot divide by Zero!")
        return
    else:
        print(f"Result= {n1/n2}")
        print(f"Remainder= {n1%n2}")
        return

def exponent(n1,n2):
    print(f"Result= {n1**n2}")
    return


choice=input('''
Choose the operation: 1/2/3/4/5
1) Add
2) Subtract
3) Multiply
4) Divide
5) Exponent
 
''')
valid=False
while not valid:
    num1 = input("Enter number 1: ")
    num2 = input("Enter number 2: ")
    if num1.isnumeric() and num2.isnumeric():
        valid=True
        num1=int(num1)
        num2=int(num2)
    else:
        print("Please enter valid numbers")

if choice=="1":
    add(num1,num2)
elif choice=="2":
    subtract(num1,num2)
elif choice=="3":
    multiply(num1,num2)
elif choice=="4":
    divide(num1,num2)
elif choice == "5":
    exponent(num1, num2)
