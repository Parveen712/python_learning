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



