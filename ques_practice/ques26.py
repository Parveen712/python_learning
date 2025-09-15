# Find the greatest element and print its index too?

l=[2,3,5,6,4]
largest=0
index=0
for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
print(f"Your largest number is {largest} and index is {index}")        
    