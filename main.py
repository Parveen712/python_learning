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

'''Continue --- usko chod ke aage chalta hai'''
# for i in range(1,21):
#     if i == 15:
#         continue
#     print(i)   

'''Directory jane ke liye'''
# print(dir(str))

'''While loop'''

# a=1
# while a<=20:
#     print(a)
#     a+=1

'''Functions'''

# def hello():     #declare function
#     print("HEllo PArveen kumar ")

# hello()         #calling the function

# #functions with parameter and arguments
# def hello (name):      #name is a parameter
#     print(f"Heelo {name}")

# hello("Parveen")       #PArveen is an argument

'''Types of arguments'''

#positional argument

# def add(a,b):
#     return a+b

# print(add(12,33))     # 12 is assign to a and 33 is assign to b 

#default argument

# def greet(name="Devil"):
#     print(f"Hello {name}")

# greet()    # use default name is devil
# greet("Bob")   #use bob

#keyword argument

# def greet(name,age):
#     print(f"I am {name} and my age is {age}")

# greet(name="Parveen", age="22")    

# #simple palindrome 
# def palindrome(str):
#     rev=""
#     for i in range(len(str)-1,-1,-1):
#         rev=rev+str[i]

#     if rev==str:
#         print(f"{str} is palindrome")
#     else:
#         print(f"{str} is  not a palindrome")    

# palindrome("NAMAN")

'''Lists'''
# a = [12,13,14,15,16,34.5]


# #1st way using index

# for i in range(len(a)):
#     print(a[i])

# #2nd way directly on values

# for i in a:
#     print(i)

# print(dir(list))       #all methods of lists is shown
# help(list)                #all methods initialize and given merthod and help is shown

#some methods of list

# num=[5,2,9,1,5,6]   #initialize list

# num.append(10)      #add 10 in end
# print(num)
# num.insert(1,3)       #inssert 3 at index 2
# print(num)
# num.extend([20,25,43])   #extend the list 
# print(num)
# num.remove(5)          #remove the first occurence of 5
# print(num)
# popped_item=num.pop(3)   #remove and store  the element at index 3
# print(popped_item)
# index=num.index(6)       #find the index at 6
# print(index)
# count_5=num.count(5)      #count the occurence of 5
# print(count_5)
# num.sort()                #sort the list
# print(num)
# num.reverse()             #reverse the whole list
# print(num)
# new_number=num.copy()      #copy of the list
# print(new_number)
# num.clear()                 #remove all element of the list
# print(num)


'''Tuple'''

# a = (1,2,3,4,5,5,5.5,print(),"hello")
# a[0]=12   #error occure

# index=a.index(5)
# print(index)

# count = a.count(5)

# print(count)

# a,b,c,d=(1,2,3,4)
# print(a)
# print(b)
# print(c)
# print(d)


# a = (1)

# print(type(a))     <int>

# a = (1,)

# print(type(a))    <tuple>

'''Sets'''     #its depend on hash value

# set={}     #<dict>
# print(type(set))

# set={1,2,3,4,2,5,6}    #doesnt occur duplicate value
# set[0]=3          #doesnt change error show
# print(set)

# a=hash("hello")
# print(a)
# a=hash((1,23,4))
# print(a)  
   
#for i in range (len(a))   #doesnt occur it give us error because it is unorderd

# a = {1,8,9,"hello",2,3,4,5} 
# for i in a:           
#     print(i)

#methods for set

# a={8,1,2,3,4}
# a.add(5)         #add element
# print(a)
# a.remove(4)        #remove element
# print(a)
# a.discard(3)          #same as remove
# print(a)
# a.pop()               #delete by hash value
# print(a)
# a.clear()                #clear all element
# print(a)

# a={1,2,3,4,5}
# b={4,5,6,7,8}

# print(a|b)      #union
# print(a&b)       #intersection
# print(b-a)       #difference
# print(b^a)       #symmetric difference

'''Dictionary'''

# d = {10:100,20:200,30:300,40:400}


# d[50] = 500 # creating
# d[10] = 100 #updating
# del d[30] # deleting 

# print(d)

# d = {10:100,20:200,30:300,40:400}
# d.clear()
# print(d)

#transveral

# d = {10:100,20:200,30:300,40:400}

# for i in d:
#     print(i)    #print key

# for i in d:
#     print(d[i])        #print value

# for i in d.values():      #for value
#     print(i)       


# d = {10:100,20:200,30:300,40:400}

# d2=d.copy()   #shallow copy of d

# d2[0]=100    

# print(d2)       #doesnt effect on d


# d = {10:100,20:200,30:300,40:400}
# print(d.items())



'''Exception handling'''

# a = int(input("tell your number :- "))

# try:
#     print(10/a)

# except Exception as err:
#     print(f"sorry there is an err as {err}")

# else:
#     print("good there is no exception")

# finally:
#     print("i will run no matter what")


# print("ok i have done the division")




# age = int(input("tell your age :- "))

# try:

#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")

# except Exception as err:
#     print(f"an error occured as {err}")


# print("the club will start soon")


'''File handling'''

# p=open('main.py')            #given the pathh of file
# print(p.read())

# p=open("super.text",'w')     #w for write

# p.write("Hello I am parveen kumar and i write a code inside the file")

# p.close()      #must be close 

# p=open("super.text",'a')     #a for append

# p.write("Hello I am parveen kumar and i write a code inside the file")

# p.close()      #must be close 

# file=open("super.text",'r')
# print(file.read())          #read entire file
# print(file.readline())       #read one line
# print(file.readlines())      #read all lines in a list

# file.close()

#no need to close file.....
# with open("super.text","r") as f:
#     content=f.read()
#     print(content)


