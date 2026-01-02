num=int(input("Enter a number for factorial: "))
if num<0:
    print("error")
else:
    fac=1
    i=num
    while(i>=1):
        fac=fac*i
        i=i-1
    print(f"The factorial of {num}! is: {fac}")
