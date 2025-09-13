#Accept name and age from the user. Check if the user is a valid voter or not.
# Ex- “hello shery you are a valid voter”

name=input("Enter your name: ")
age= int(input("Enter your age: "))

if age>=18:
    print(f"Hello {name} you are a valid voter")
else:
    print(f"Hello {name} you are a chotu")    


