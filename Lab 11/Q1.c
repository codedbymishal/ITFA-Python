num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))
op=int(input("Enter operator (1/2/3): "))
if op==1:
    print(f"The sum of {num1} and {num2} is {num1+num2}")
elif op==2:
    print(f"The subtraction of {num1} and {num2} is {num1-num2}")
elif op==3:
    print(f"The product of {num1} and {num2} is {num1*num2}")
else:
    print("Invalid operator!")
