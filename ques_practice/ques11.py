#Take a number as input and print its table
n=int(input("Enter a table: "))
# for i in range(n,(n*10)+1,n):
for i in range (1,11):
   print(f"{n} * {i} = {n*i}")