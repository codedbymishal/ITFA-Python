#Q1
name="mishal"
age=19
city="Karachi"
print("My name is ",name)
print(f"I am {age} years old and I live in {city}")
print("My name is "+name+" and i am "+" " +str(age)+" years old and i live in "+city)
print("My name is {} and I am {} years old".format(name,age))
 
username=input("Enter your name: ")
print(username)
print("hello",username)

#Q2)
num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))
sum=num1+num2
print("sum is ",sum)
print(f"Sum of {num1} and {num2} is {sum}")
print(f"Sum of {num1} and {num2} is {num1+num2}")
print("Sum of {} and {} is {}".format(num1,num2,num1+num2))