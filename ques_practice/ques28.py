#Check if List is sorted or not.

# l=[12,23,41,41,34,43]
l=[12,13,21,23,144]

for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        print("Your list is not sorted: ")
        break
else:
    print("Your list is sorted")

