#Check string is Pallindrome or not
a=input("Enter a word: ").lower()
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]

if b==a:
    print("It is palindrome")
else:
    print("It is not a palindrome")    