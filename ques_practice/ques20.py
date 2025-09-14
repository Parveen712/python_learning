'''Count all letters, digits, and special symbols from a given
string
Given: str1 = "P@#yn26at^&i5ve"
Expected Outcome:
Total counts of chars, digits, and symbols
Chars = 8
Digits = 3
Symbol = 4'''

a=input("Enter a string: ")

char=0
digit=0
symbol=0

for i in a:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        char+=1
    else:
        symbol+=1
print(f"your digit is {digit} , your char is {char} and your symbols is {symbol} ")
