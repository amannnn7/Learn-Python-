#print("hello world")
#print("My name is aman.","my age is 23.")
#print(25)
#print(25+25)

# VARIABLE IN PYTHON

#name = "Aman" #string : string is a value where we write any words in sindle coart or double coats 
#age = 23
#price = 34.99

#print("name")  # here the name variable will not get printed the word name will be printed as it is written in double quotes so to print name value which is stored in variable we need to write name without inverted coats.

#print(name)

#print("me is :", name)
#print("my age is :", age)

#print(type(name))
#print(type(age)) #these types are called data types

#you can present the string in single, double or triple cort

"""name1 = "sk"
name2 = 'sk'
name3 = '''sk'''

print(name1)
print(name2)
print(name3)"""

"""age = 23
old = False
a = None
print(type(old))
print(type(a))"""

# python is case sensitive means a has another value and A has another value
# print sum

"""a = 2
b = 3
sum = a + b
print(sum)"""

#change for differnece , multiplication , etc.

# for commenting the code use ctrl +/ for commenting multiple line at a single time
# arithmetic operator
# a = 2
# b = 3
# print(a+b) #addition
# print(a-b) #subtraction
# print(a*b) #multiplication
# print(a/b) #division
# print(a%b) #modulus
# print(a**b) #exponentiation (means a to the power b)

# relational/ comparison operator these are use to compare two value 
#(==, !=, >, <, >=, <=)
# a = 2 
# b = 3
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

#assignment operator (means assigning the value)
#(=, +=, -=, *=, /=, %=,**=)

# a = 2 (means we are assigning value 2 to a)
# num = 10
# ##num = num + 10 #10+10=20
# # we can write num = num + 10 value as num += 10 in python 
# #num += 10 #20
# #num -= 10 #0
# num *= 10 #100
# print("num :", num)

#LOGICAL OPERATOR (NOT, AND , OR)
# IT WORK ON BOOLEAN LIKE TRUE AD FALSE

# print(not False)
# print(not True)

# we can use by putiing value
# a = 20
# b = 30

# print(not False)
# print(not (a > b)) # here bpth condition are true now we are changing the value and again we will check

# a = 50
# b = 30

# print(not False)
# print(not (a > b))

# val1 = True
# val2 = True
# print("and operator:", val1 and val2) # here bothr thr value should be true the only it return true if any one value is false it will return false.

# val1 = True
# val2 = False
# print("or operator:", val1 or val2) # anyone can be true then it will return true value

#NOW WE ARE CHECKING CONDITION BY GIVING THE VALUE
# a = 50
# b = 30

# val1 = True
# val2 = False
# print("or operator:", (a == b) or (a > b))

#TYPE CONVERSION 
# int to float
# float to int
# int to str
#CONVERTING ONE TYPE INTO ANOTHER TYPE

# a = 50
# b = 30.8

# sum = a + b #20+30.8=50.8
# print("sum:", sum)

# a = "50"
# b = 30.8

# sum = a + b #50+30.8=80.8
# print("sum:", sum) # here it will give error because we are trying to add string and float value

# a = int("50")
# b = 30.8

# sum = a + b #50+30.8=80.8
# print("sum:", sum) #here 50 is considered as int value that use it get added, so this process is under type casting where we change one type into its suitable type 

# a = 3.14
# a = str(a)
# print(type(a))

# INPUT IN PYTHON 
#input() statement is used to accept vales using keyboard from user

#input() # result for input()  is always a str
# int (input()) #int
# float (input()) #float

#input("your name is: ")
# print("your name is: ", input()) # here we are printing the input value in string 

# name = input("your name is: ")
# print("your name is: ", name) # here we are storing the input value in variable nam

# val = input("enter some value: ")
# print(type(val), val)

# val = input("Enter a num: ")
# print(val) # here you enter anyvalue 22, 99.9 it will always return str valu

# val = int(input("enter some value: ")) #here we define int value show it will return int if we define float then it will return float
# print(type(val), val)

# name = input("enter your name: ")
# age = int(input("enter your age: "))
# marks = input("enter your marks: ")

# print ("name is :", name)
# print ("age:", age)
# print ("my marks :", marks)

#write a program to input two number and print their sum
# 4

#WAP TO INPUT SIDE OF A SQUARE AND PRINT ITS AREA

# side = int(input("enter the number :"))
# # area = side * side
# # print("area of square: ", area)
# # we can also do like this 
# print("area= ", side * side)

#WAP TO INPUT 2 FLOATING POINT NUMBER AND PRINT THEIR AVERAGE 

# a = 1.4
# b = 2.5
# or
# a = float(input("enter a number:"))
# b = float(input("enter a number:"))
# print("avg:", (a + b)/2)

# WAP TO INPUT 2 INT NUMBER A and B. PRINT TRUE IF A IS GREATER THAN EQUAL TO B IF NOT PRINT FALSE

# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# print(a >= b)
# #or
# if a >= b:
#     print(True)
# else:
#     print(False)

# String and conditional statement
# str1 = "aman"
# str2 = 'aman'
# str3 = '''aman'''

# str4 = "this is a string.\nwe are creating it in python" #\n is use to take the things into next line.
# print(str4) #we can also use r to make it raw string

#basic operation 
# concatenation(adding two string)
# str1 = "am"
# str2 = "an"
# sum = str1 + str2
# print(sum) #output: aman

#length of string
# str1 = "aman"
# #print(len(str1))
# #or
# len2 = len(str1)
# print(len2) #output: 4

# IN COUNTING STRING VALUE THEY ALSO COUNT THE STRING
# str1 = "aman"
# str2 = "kumar"
# finalstr = str1 + " " + str2
# print(len(finalstr))# outpot = 10

#INDEXING 
# str = "aman kumar"
# ch = str[1]
# print(ch) #output: m
#or
# str = "aman kumar"
# print(str[1]) #output: m

# WE CANNOT ASSIGN ANY CHARACTER IN PYTHON LIKE WE WANT TO ADD @ IN THR STR AMAN KUMAR SO IT IS NOT ALLOWED

#SLICING
# str[starting index: ending index](but last index is not included)
# str = "aman kumar"
# # print(str[1:4])
# #output: man
# print(str[3:len(str)])
# #output : m kumar
#or
# print(str[3:]) #output: m kumar
# print(str[:3]) #output: aman
# print(str[1:5]) #output: man

#SLICING (NEGATIVE INDEX(BACKWARD COUNTING))

# str ="aman"
# print(str[-3:-1]) #output:ma
# print(str[-4:]) #output:man
# print(str[:-2]) #output:ama
# print(str[-1:]) #output:a

#STRING FUNCTION 

# str = "i am aman"
# #print(str.endswith("an")) #output:true
# print(str.capitalize()) #I am aman , this is not modifying the original string it create new string is we want to create or print our 
# # string again then it will again print the same see as example below
# print(str)
#  # so to modify the original string we need to store this in a str value as shown below
# str = str.capitalize()
# print(str) #I am aman

# replace function is use to replace the old function to new function 
# str = "i am aman"
# print(str.replace("a","o"))
# print(str.replace("aman","monu")) #i am monu

# find function is use to such the word in that string( jaha pe 1st string 1st time dikhega uska starting string return karega)

# str = "i am aman"
# print(str.find("aman")) #output: 5
# print(str.find("l")) #output: -1
# print(str.find("aman", 5)) #output: 5

# count function is used to find the occurance (kitni baar wo string exist karta hai wo return karke dega)
# str = "aman kumar aman"
# print(str.count("aman")) #output: 2
# print(str.count("kumar")) #output: 1
# print(str.count("man"))#output: 2
# print(str.count("ramS")) #output: not produce

#PRACTISE QUESTION
#Q: WAP TO INPUT USER FIRST NAME AND PRINT ITS LENGTH
# a = input("enter your first name:")
# print(len(a)) #output: length of the string

# Q: WAP TO FIND OCCURANCE OF $ IN A STRING
# a = input("enter your string:")
# print(a.count("s")) #output: count of s in the string

# Q: WAP TO FIND OCCURANCE OF $ IN A STRING FROM 5TH INDEX
# a = input("enter your string:")
# print(a.count("s", 5)) #output: count of s in the string from

#CONDITIONAL STATEMENT
#if-elif-else(SYNTAX)
# if (condition):
#     #code to be executed if condition is true
# elif (condition):
#     #code to be executed if condition is true
# else:
#     #code to be executed if all conditions are false

# age = 21
# if (age >= 18):
#     print("you are adult")
# else:
#     print("you are minor") #this will not print because of indentation error
#or
# a =input("enter your age:")
# age = int(a)
# if (age >= 18):
#     print("you are adult")
# else:
#     print("you are minor")

# light = "green"
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("ready to go")
# elif(light =="green"):
#     print("go") #this will not print because of indentation error

# light = "pink"
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("ready to go")
# elif(light == "green"):
#     print("go") 
# else:
#     print("invalid color")

# a = ("enter the color of light")
# light = input(a)
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("ready to go")
# elif(light == "green"):
#     print("go") 
# else:
#     print("invalid color") 

#indentation = means giving proper space like we 4 space after if or else
#indentation is must in python

#WAP TO GIVE THE GRADE TO STUDENT ON THEIR MARKS
# marks = int(input("enter the marks:"))
# if marks >= 90:
#     print("grade A")
# elif 90 > marks >= 80:
#     print("grade B")
# elif 80 > marks >= 70:
#     print("grade C")
# elif 70 > marks >= 60:
#     print("grade D")

# NESTING ( IF KE ANDER EK AUR IF LIKHNA )
# age = 34
# if age >= 18:
#     if age >= 65:
#         print("you are senior citizen and cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

#Wap to check if a number entered by the user is odd or even
# num = int(input("enter the number:"))
# if num % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

#WAP  TO FIND THE GREATEST OF 3 NUMBER ENTERED BY THE USER
# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# num3 = int(input("enter the third number:"))
# if num1 > num2 and num1 > num3:
#     print("number 1 is greatest")
# elif num2 > num1 and num2 > num3:
#     print("number 2 is greatest")
# elif num3 > num1 and num3 > num2:
#     print("number 3 is greatest")
# else:
#     print("all numbers are equal")

#OR

# a = int(input("enter the first number:"))
# b = int(input("enter the second number:"))
# c = int(input("enter the third number:"))
# if(a >= b and a >= c):
#     print("number 1 is greatest", a)
# elif(b >= c):
#     print("number 2 is greatest", b)
# else:
#     print("number 3 is greatest", c)

#WAP TO CHECK IF A NUMBER IS A MILTIPLE OF 7 OR NOT
# num = int(input("enter the number:"))
# if num % 7 == 0:
#     print("number is multiple of 7")
# else:
#     print("number is not multiple of 7")




# if condition
#     # code to be executed if condition is true
