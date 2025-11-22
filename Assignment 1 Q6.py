fruits=["apple","mango","banana","orange","peach","pineapple","strawberry"]
index=int(input("Enter an index (0-5) to display a fruit!: "))
print(f"fruit at index {index} is {fruits[index]}")

print(fruits[2:5]) #display from index 2 to 4
fruits[3:6]= ["abc","def","xyz"] #change values from index 3 to 5
print(fruits)