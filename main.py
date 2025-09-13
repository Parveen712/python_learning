'''Comments'''
#this is single line comments
'''This is a
 multiline 
comments 
method'''

'''Variables'''

# name=parveen
# age=20

# You can not use numbers at variable start
# You can not use spaces in variables.
# You should not use special characters in variables.

'''Naming conventions'''
# ParveenKumar = pascal case
# parveenKumar = camel case
# parveen_kumar = snake case

'''Data Types'''
# #integers   all real number
# a=-39
# print(type(a))
# #float    all decimal number and p/q form
# b=54.3
# c=12/3
# print(type(b))
# #complex number  
# d=30j
# print(type(d))
# #boolean  only true and false
# e=True
# print(type(e))
# #string  all which are wriiten in quotes
# f="PArveen kumar 20"
# print(type(f))

'''Strings'''
# #print ascii/unicode value code
# a='A'
# print(ord(a))
# #print char value bu ascii value
# a=65
# print(chr(a))

'''String indexing'''

# a = 'HEllo'    
# print(a[0])        idx from staring = 0 1 2 3
# a='Hello'
# print(a[-1])         reversing indexing= -4 -3 -2 -1

'''String slicing'''

# a='Parveen Kumar'  
# print(a[0:7:1])      a[star:end:step]

# print(a[::])         by default staring se start hota hai

'''Type conversion'''

#EXPLICIT CONVERSION

# #str to int

# a='12'
# print(type(a))
# a = int(a)
# print(type(a))

#int to float

# a=12
# print(type(a))
# a = float(a)
# print(type(a))

# #float to int

# a=12.33
# print(type(a))
# a = int(a)
# print(type(a))

#invalid  error  only numeric value can be tranverse
# a='qebdj'
# a=int(a)
# print(type(a))

# int to bool only true and false value given
# a=12
# a=bool(a)
# print(type(a),a)

# false value written = 0, 0.0, [],{},(),"",false,

#IMPLICIT CONVERSION     which ARE automatically covert by python

# a=12
# print(a/3)   #int to float beacuse form in p/q


# name="parveen"
# age=21
# print(name,age)

# name=input("Enter your name: ")   #input from user
# print(f"My name is {name}")        #f string method

# name=input("Enter your name: ")
# age=21
# print("my name is ",name,"my age is ",age,)    #one way writing

# name = "Parveen"
# age = 21
# print("My name is {} and I am {} years old".format(name, age))     #format string example

'''Operators'''

# a = 5
# b = 32


# print(a + b)
# print(b - a)
# print(a * b)
# print(b//a)
# print(b/a)
# print(5**100)
# print(32%5)


# print(12+4/2)


#assignment operators 

# a = 23

#compound assignment operators

a=20
# a += 20      shortform --->  a = a +20
# a += 40
# a += 60
# a-=20
# a*=20
# a/=20
# a//=20
# a% = 20
# a**=20

# print(a)

'''Comparison operator'''

a = 12.1
b = 12 

# print(a == b)

# print(a != b)

# print(a > b)
# print(45 < 67)
# print(23 >= 23)
# print(45 <= 45)

# print("ABC" > "ACD")

# print(ord("A")>38)

'''Logical operators'''

# print(22>2 and 22>4)                    #  and - Return True if both condition are Tru\
# print(22>3 or 22>28)                    #  or - Return True if at least one condition is True
# print(not 22==2)                    #  not - Reverse the boolean value

# print(12 !=12 or 23 ==45 or 67 == 56 or 10 > 5)

'''Trivial Questions'''

# Answer True and False

# print(126 > 130)
# print((456 == 456) != (235 == 236))
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
# print(True and bool(0))

'''Conditional statements'''

# #if

# a=20
# if a>10:
#     print("True")

#if-else

# a=20
# if a<10:
#     print("True")
# else:
#     print("false")    

#if-elif-else

# m =int(input("Enter your marks: "))

# if m>90:
#     print("Grade A")
# elif 60<m<90:
#     print("Grade B") 
# elif 60>m>40:
#     print("Grade C")    
# else:
#     print("fail")           


'''FOr loops'''

#range

# #print 1 to 10
# for i in range(1,11,1):
#     print(i)

# #print reverse 10 to 0
# for i in range (10,0,-1):
#     print(i)

# #print -5 to -15
# for i in range(-5,-16,-1):
#     print(i)

#print table by for loop range

# n=int(input("Enter a table: "))

# for i in range(n,(n*10)+1,n):
#     print(i)


# a = "Hello PArveen Kumar, How are you?"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])

#direct itelator

# a = "Hello PArveen Kumar, How are you?"

# for i in a:
#     print(i)

'''Break --- uhi he loop ko exit kra deta hai'''
# for i in range(1,21):
#     if i == 15:
#         break
#     print(i)   

'''Continue --- usko chpd ke aage chalta hai'''
# for i in range(1,21):
#     if i == 15:
#         continue
#     print(i)   

