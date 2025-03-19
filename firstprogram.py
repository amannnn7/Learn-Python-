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

# """name1 = "sk"
# name2 = 'sk'
# name3 = '''sk'''

# print(name1)
# print(name2)
# print(name3)"""

# """age = 23
# old = False
# a = None
# print(type(old))
# print(type(a))"""

# python is case sensitive means a has another value and A has another value
# print sum

# """a = 2
# b = 3
# sum = a + b
# print(sum)"""

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

# LIST IN PYTHON
# IT CAN STORE ELEMENTS OF DIFFERENT TYPES (INTEGER, FLOAT, STRING, ETC.)
# marks = [67,45, 98, 34]  for example 

# marks = 95.4
# marks = 87.5
# marks = 98.6
# marks = 67.8
# marks = 45.6
# ab koi new student aayega to phir se game new marks ka varible banana hoga
# so built data function come where we can store multiple value

# marks = [98.5, 67.9, 65.7, 98.6] # this built in function is called list
# print(marks)
# print(type(marks))
# print(marks[0]) # same we do in string
# print(marks[4]) # index out of range error

#LIST ARE MUTABLE IN PYTHON WHERE STRING ARE IMMUTABLE(WHICH NOT CHANGES) 
# str - "hello"
# print(str[0])
# str[0] = "y" # this is not allowed in python as string are immutable so we can't change the value
# so this will give the error
# but this is possible in python as change is possible for example
# student = ["karan", 95.4, 17, "delhi"]
# print(student[0])
# student[0] = "karan kumar"
# print(student)
# so this will not give the error 

#LIST SLICING  (similar to string slicing)

# marks = [87, 68, 89, 88, 94]
# print(marks[1:4])
# print(marks[1:4:2]) # this will print every 2nd element
# #  here also there in negative index concept
# print(marks[-1]) # this will print last element
# print(marks[-2]) # this will print second last element

# LIST METHODS
# marks = [87, 68, 89, 88, 94]
# marks.append(45)  #add the append element at the last
# print(marks)
# marks.sort() #sorted in ascending order
# print(marks)
# # but it we tries to print marks.sort then it will print none as it change the value by going inside the marks list
# # so it will return none
# marks.reverse() # reverse the list
# print(marks)
# marks.insert(1, 78) # insert the element at index  like list.insert(index, element)
# print(marks)
# marks.pop(2) # remove the element 2nd from the list
# print(marks)

#TUPLES IN PYTHON 
# tuples are immutable in python
# tup = (87, 68, 89, 88, 94)
# #tup[0] = 43 # not allowed 
# print(type(tup))
# print(tup[0])

# #slicing concept is same in tuples as was in list
# print(tup[1:4])
#TUPLE METHOD
# tup = (87, 68, 89, 88, 94)
# #tup.append(45) # not allowed as tuples are immutable
# print(tup)
# print(tup.count(89)) # count the element in tuple
# print(tup.index(89)) # index of the element in tuple of first occurance

#WAP TO ASK THE USER TO ENTER NAME OF THEIR 3 FAVORITE MOVIE AND STORE THEN IN LIST
# name = input("enter your name:")
# movies = []
# for i in range(3):
#     movie = input("enter your favorite movie:")
#     movies.append(movie)
# print("your favorite movies are: ", movies)
# # here we can also use list comprehension to store the movies in list
  # OR

# movie = []
# mov1 = input("enter first movie name")
# mov2 = input("enter second movie name")
# mov3 = input("enter third movie name")
# # here we can also use list comprehension to store the movies in list
# movie.append(mov1)
# movie.append(mov2)
# movie.append(mov3)
# print(movie)/

 # OR

# movie = []
# mov = input("enter first movie name")
# movie.append(mov)
# mov = input("enter second movie name")
# movie.append(mov)
# mov = input("enter third movie name")
# movie.append(mov)

# print(movie)

#OR
# movie = []
# movies.append(input("enter first movie name"))
# movies.append(input("enter second movie name"))
# movies.append(input("enter third movie name"))
# print(movies)

# WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.
# list1 = [1, 2, 1]
# list2 = [1, 2, 3]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("list contains palindrome elements")
# else:
#      print("list does not contain palindrome elements")

# list = int(input("enter a number: "))
# if str(list) == str(list)[::-1]:
#     print("number is palindrome")
# else:
#    print("number is not palindrome")

#OR
# a = int(input("enter a number: "))
# sum = 0 #we have to initialize the sum before declaring it otherwise it will take a garbadge value
# b = a
# while a > 0:
#    rem = a % 10  # for example it take 141 so after performing modulo it will give 1 as remainder
#    sum = sum*10 + rem # here we declare the sum / initiality sum is zero so sum = 0*10 + 1 = 1
#    a = a // 10
# if b == sum:
#     print("number is palindrome")
# else:
#    print("number is not palindrome")

# WAP TO COUNT THE NUMBER OF STUDENT WITH THE "A" GRADE IN THE FOLLOWING TUPLE
# ["C", "D", "A", "A", "B", "B", "A"]

# grade = ("C", "D", "A", "A", "B", "B", "A")
# print(grade.count("A"))

# STORE THE ABOVE VALUE IN A LIST AND SORT THEM FROM "A" TO "D"
# grade = ["C", "D", "A", "A", "B", "B", "A"]
# grade.sort()
# print(grade)

# DICTIONARY IN PYTHON
# DICTIONARY IS A COLLECTION OF KEY VALUE PAIR
# DICTIONARY IS MUTABLE
# Dictionaries are used to store data value in key value pairs.
# they are unordered, mutable (changeable) and don't allow duplicate keys.

# info = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Mumbai",
# }

# print(info)

# we can store list and tuple in dictonaries
# info = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Mumbai",
#     "hobbies": ["cricket", "football", "reading"], #list
#     "address": ("Mumbai", "Maharashtra", "India"), #tuple
# }
# print(info)

# info = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Mumbai",
#     "hobbies": ["cricket", "football", "reading"], #list
#     "address": ("Mumbai", "Maharashtra", "India"), #tuple
# }
# print(info["name"])
# print(info["city"])
# print(info["address"])

#assigning value 

# info = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Mumbai",
#     "hobbies": ["cricket", "football", "reading"], #list
#     "address": ("Mumbai", "Maharashtra", "India"), #tuple
# }

# info["name"] = "aman"
# print(info["name"]) #output: aman 
# #OR
# print(info)# here all value will be printed after the updation
# print(info["age"] + 10) #output: 30 

#NESTED DICTIONARY 

# student = {
#     "name" : "aman",
#     "score": {
#         "math" : 90,
#         "science" : 80,
#         "english" : 70
#      }
# }
# print(student)
# print(student["score"]["math"]) #output: 90

#DICTIONARY METHODS

# myDict.keys() #return all keys
# myDict.values() #reyurn all values
# myDict.items() #return all key value pairs as tuples (key, val)
# myDict.get(key) #return value for key if key exists, otherwise return None
# myDict.setdefault(key, default) #return value for key if key exists, otherwise return default
# myDict.pop(key) #remove key and return value
# myDict.popitem() #remove and return last key-value pair
# myDict.update(newDict) #update myDict with key-value pairs from other

# student = {
#     "name" : "aman",
#     "score": {
#         "math" : 90,
#         "science" : 80,
#         "english" : 70
#      }
# }
# print(student.keys())
# print(len(student.keys())) # return length of the key not nested key only outer layer key.
# print(student.values())

# # hum dictionary ki list ke andar ya list ko dictionary ke andar store kara sakte hai 
# print(list(student.items()))
# # agar hame sirf ek ki pair ko print karwana hai to 
# pairs = list(student.items())
# print(pairs[0]) #output: ('name', 'aman')

# hum key likh ke uska value pata kar lete hai lekin yaha ek aur method aaya 
# d.get("key") = value 
#why we need this as we are getting the value by two methods lets understand by code

# student = {
#     "name" : "aman",
#     "score": {
#         "math" : 90,
#         "science" : 80,
#         "english" : 70
#      }
# }
# print(student["name"])
# print(student.get("name"))
# # here both the print will return the name
# # but if we try to access the key which is not present in the dictionary then it will throw
# # an error but get method will return None
# print(student["name2"]) #output: NameError
# print(student.get("name2")) #output: None

# student = {
#     "name" : "aman",
#     "score": {
#         "math" : 90,
#         "science" : 80,
#         "english" : 70
#      }
# }

# student.update({"city" : "mumbai"})
# print(student) 

#SETS IN PYTHON
#set is the collection of the unordered items.
#each element in the set must be unique and immutable
#but set is mutable
# nums = {1, 2, 3, 4}
#set2 = {1, 2, 2, 2} repeated elemens stored only once, so it resolved to {1, 2}

#null_sets = set() empty set syntax

# collection = {1, 2, 3, 4}
# print(collection) #output: {1, 2, 3, 4}
# print(type(collection))
# print(collection[0]) #output: IndexError: set indices must be integers or strings
# print(collection[0:2]) #output: TypeError: set indices must be integers or strings

# collection = set()
# print(collection) #output: set()

# SET METHODS
# add() - adds an element to the set
# discard() - removes an element from the set if it is a member
# remove() - removes an element from the set if it is a member
# pop() - removes an arbitrary element from the set
# clear() - removes all elements from the set

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# print(collection) 

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.remove(2)
# print(collection)

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("aman")
# collection.add("city")
# # we can use tuple but not list to time ke saath change ho sakti hai new element add and remove ho sakte.
# collection.add([1, 2, 3]) # this will give no error
# collection.add((1, 2, 3)) # this will give the error(unhashable type) unhasable ka matlab jinki valu baad me jaake change ho jaaye means immutable

# print(collection)

# collection = {"hello", "world", " aman", " monu"}
# print(collection.pop()) # it will pop the element in random order.
# print(collection.pop())
# print(collection) # it will print the set after popping the element.  #output: {'aman', 'monu'}

# there are  more methods
# set.union() combines both set values and return new
# set.intersection() returns a new set with elements common to the set and others
# set.difference() returns a new set with elements in the set but not in others

#  PRACTICE QUESTION
# 1. Write a Python program to create a set of numbers from 1 to 10
# STORE FOLLOWING WORD MEANING IN A PTHON DICTIONARY
# table : "a piece of furniture". "list of facts and figures"
# cat: "a small animals"

# dictionary = {
#     "cat" : "a small animals",
#     "table" : ["a piece of furniture", "list of facts and figures"]
    
# }

# print(dictionary)

# You are given a list of subjects for students. Assume one classroom is required for 1
#  subject. How many classrooms are needed by all students.
#  ”python”, “java”, “C++”, “python”, “javascript”,
#  “java”, “python”, “java”, “C++”, “C”

# to yaha pe hm agar ek set bana le aur uska length nikal le to kaam ho jaayega

# subject = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "C"}
# print(len(subject)) # it will print the number of unique subject

#  WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#  an empty dictionary & add one by one. Use subject name as key & marks as value

# marks = {}
# subject = input("Enter subject name: ")
# marks[subject] = int(input("Enter marks: "))
# subject = input("Enter subject name: ")
# marks[subject] = int(input("Enter marks: "))
# subject = input("Enter subject name: ")
# marks[subject] = int(input("Enter marks: "))
# print(marks) # it will print the dictionary with subject name as key and marks as value.

#or

# marks = {}
# x = int(input("enter phy: "))
# marks['phy'] = x
# x = int(input("enter chem: "))
# marks['chem'] = x
# x = int(input("enter math: "))
# marks['math'] = x
# print(marks) # it will print the dictionary with subject name as key and marks as value.

# Figure out a way to store 9 & 9.0 as separate values in the set. 
# (You can take help of built-in data types) 

# values = {9, 9.0}
# print(values) # it will print {9.0, 9} because in set duplicate values

#so we have to think differently

# values = {9, 9.0, 8.23}
# print(values)

# values = {9, "9.0"}
# print(values) # here its done.

#LOOPS IN PYTHON
#loops are used to repeat instructions..


#WHILE LOOP
#  while condition:
#        instruction

# while True :
#     print("Hello, World!") #it will print infinite time as true to true hi rahega

# so we need to define a value till which the while loop will work

# count = 1
# while count <=5 :
#   print("hello")
#   count = count + 1

# print(count) # this will print the count value which is 6
# count variable ko iteration bolte hai 
# loop ke andar run krne ko iteration bolte hai 

# i = 1
# while i <=5:
#    print("hello")
#    i += 1

# print number 1 to 5
# i = 1
# while i <=5:
#     print(i)
#     i += 1

# PRACTICE QUESTION 
# PRINT NUMBER FROM 1 TO 100

# i = 1
# while i<=100:
#     print(i)
#     i += 1

# PRINT NUMBER FROM 100 TO 1

# i = 100
# while i>=1:
#     print(i)
#     i -= 1

#Print the multiplication table of a number n.

# i = 1
# while i<=10:
#     print(3*i)
#     i += 1


# By taking input from the user
# table = int(input("enter your number:"))
# i = 1
# while i<=10:
#     print(table*i)
#     i += 1
    
# Print the elements of the following list using a loop: 
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# idx = 0
# while idx < len(num):
#     print(idx)
#     idx +=1 # if we write this code the output will be 0 to 9
  

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# idx = 0
# while idx < len(num):
#     print(num[idx]) #num[0] #num[1]......
#     idx +=1
# this process is called traverse as we are going to each and every element


#  Search for a number x in this tuple using loop:
#  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) 
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) 

# i = 0
# while i < len(num):
#     print(num[1])
#     i += 1
# this will print the element of num
# now the code for the actual question 

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) 

# x = 36 # hame x= 36 ke liye search krna hai jo list me present bhi hai 

# i = 0 #initialization
# while i < len(num):
#     if(num[i] == x):
#         print("number found") 
#     i += 1


# now how loop works like we have more occurance of the element
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36) 

# x = 36 # hame x= 36 ke liye search krna hai jo list me present bhi hai 

# i = 0 #initialization
# while i < len(num):
#     if(num[i] == x):
#         print("number found at idx", i) 

#     else:
#         print("finding...")
#         i += 1


# BREAK AND CONTINUE
# BREAK IS USED TO TERMINATE THE LOOP WHEN ENCOUNTERED
# CONTINUE IS USED TO SKIP THE CURRENT ITERATION AND MOVE TO THE NEXT ONE

# i = 1
# while i<=100:
#     print(i)
#     if (i == 20):
#         break
#     i += 1


# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36) 

# x = 36 # hame x= 36 ke liye search krna hai jo list me present bhi hai 

# i = 0 #initialization
# while i < len(num):
#     if(num[i] == x):
#         print("number found at idx", i) 
#         break
#     else:
#         print("finding...")
#         i += 1


# i = 1
# while i<=100:
#   if (i == 20):
#     i += 1
#     continue #skip that number
#   print(i)
#   i += 1
  #this will print the whole number except 20

# we want to print all the even number from 1 to 100
# i = 1
# while i<=100:
#   if (i%2 == 0):
#     i += 1
#     continue 
#   print(i)
#   i += 1

#LOOPS IN PyTHON
# Loops are used for sequential for transversing list, tupe, string, etc.
#syntax
# for Loops
#  for el in list: 
    #some work

#for loop with else
# for el in list: 
#    #some work
# else: 
#    #work when loop ends

# nums = [1, 2, 3, 4, 5]
# for val in nums: # pehle hamari value 1 hogi phir 2 and so on
#     print(val) # ye print kr dega 1,2,3,4,5

# nums = [1, 2, 3, 4, 5]
# for val in nums: 
#     print(val)
# else:
#     print("End") 
# now understand why we are using else  
# this can be used where we use break
#if we want to search the element in a string

# str = ("amankumar")
# for char in str:
#     if char == "a":
#        print(" o found")
#        break
# else:
#     print("End")

#   #this will print "o found" because "a" is present in the string
# and print the character of the string
# str = ("kumar")
# for char in str:
#     if char == "a":
#        print("o found")
#        break
#     print(char)
# else:
#     print("End")

#  Print the elements of the following list using a loop: 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# number = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for num in number:
#     print(num)  # Output: 1, 4, 9, 16,

# Search for a number x in this tuple using loop:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 


# number = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 25
# for num in number:
#     if num == x:
#         print("Number found")
#         break
#     else:
#         print("Number not found") 
         # Output: Number found

# another method to found the number with index

# number = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] # this process of searching is called linera search
# x = 25
# idx = 0
# for num in number:
#     if (num == x):
#         print("Number found at idx", idx)
#     idx += 1

# RANGE IN PYTHON
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by
#  1 (by default), and stops before a specified number.
# range( start?, stop, step)
# start: The starting number of the sequence. Default is 0.
# stop: The end value of the sequence. This is exclusive, meaning that the generated numbers never
#  reach this value.
# step: The difference between each number in the sequence. Default is 1.
# step and start are optional 
# seq = range(5)
# print(list(seq))  # Output: [0, 1, 2, 3, 4]

#Or

# seq = range(5)
# for i in seq:
#     print(i)


# for i in range(10): #range(stop)
#     print(i)  # Output: 0, 1, 2, 3, 4

# for i in range(2, 10): #range(start, stop)
#     print(i) 

# for i in range(2, 10, 2): #range(start, stop, step)
#     print(i) 

# we want to print the even number from 1 to 100
# for i in range(2, 101, 2): #range(start, stop, step)
#     print(i)

# Print numbers from 1 to 100. 
# for i in range(1, 100):
#     print(i)  # Output: 1, 2, 3, 4,

# Print numbers from 100 to 1. 

# for i in range(100, 0, -1):
#     print(i)


# Print the multiplication table of a number n. 
# n = int(input("Enter a number:"))
# for i in range(1, 11):
#     print(n * i)
   
# Print the first n natural numbers.
# n = int(input("Enter a number:"))
# for i in range(n):
#     print(i)


#PASS STATEMENT
# pass is a null statement that does nothing. It is used as a placeholder for future code.
# SYNTAX
#  for el in range(10): 
#      pass

# for i in range(5):
#     pass
# print("hi")
    
# Let‘s Practice
# WAP to find the sum of first n natural numbers. (using while)
# n = int(input("Enter a number:"))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i

# print("total sum", sum)

# now using while loop
# n = int(input("Enter a number:"))
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i + 1
# print("total sum", sum)



# WAP to find the factorial of first n numbers. (using for)
# n = int(input("Enter a number:"))

# fact = 1 # we cannot initialize fact by 0 otherwise it will multiply by 0 
# i = 1
# while i <= n:
#     fact = fact * i
#     i = i + 1
# print("total fact", fact)

# using for
# n = int(input("Enter a number:"))
# fact = 0
# for i in range(1, n+1):
#     fact = fact * i

# print("factorial=", fact)


# Functions in Python
# Block of statements that perform a specific task.
# def func_name( param1, param2..) : 
#     #some work
#     return val 
# func_name( arg1, arg2 ..) #function call  # args wo value hao jo parameter k2e andar jaake store ho jaayega
# if we need to write a block of code 2 or 3 times in our code then we have to convert that into a function

# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum
# calc_sum(10, 20) #function call, the value 10 and 20 are arguments

# calculate the avg of 3 number
# def cal_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg
# cal_avg(10, 20, 30) #function call, the value 10, 20, 30

#TYPES IN PYTHON
# 1. BUILT IN function  [ print(), len(), type(), range()]
# 2. USER DEFINED function

# Default Parameters
# Assigning a default value to parameter, which is used when no argument is passed

# def calc_sum(a = 1, b = 1):
#     sum = a + b
#     print(sum)
#     return sum
# calc_sum()   #here we didn't pass any value so it will take default value which we had passed during defining a function
# we always give default value from last first we give it to b then a

# Let‘s Practice
#  WAF to print the length of a list. ( list is the parameter)
# list = [1, 2, 3, 4, 5]
# def print_len(list):
#     print(len(list))
# print_len(list)

#  WAF to print the elements of a list in a single line. ( list is the parameter)
# list = [1, 2, 3, 4, 5]
# def print_elements(list):
#     print(*list)
# print_elements(list)

#OR
# list = [1, 2, 3, 4, 5]
# def print_elements(list):
#     for element in list:
#         print(element, end = ' ')
# print_elements(list)
    


#  WAF to find the factorial of n. (n is the parameter)
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     print(fact)
# cal_fact(int(input("enter a number:")))



#  WAF to find the sum of n natural numbers. (n is the parameter)
# def cal_sum(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum = sum + i
#     print(sum)
# cal_sum(int(input("enter a number:")))


#  WAF to convert USD to INR.

# def converter(usd_val):
#     inr_val = usd_val * 80
#     print(usd_val,"USD=", inr_val, "INR")
# converter(100)  # here we are passing 100 as an argument to the function converter()

# Recursion
#  When a function calls itself repeatedly. 
#prints n to 1 backwards

# def show(n):
#     print(n)
# show(5) # this will print 5
# but we want to print 5,4,3,2,1 in only one function call
# means we call show 1 time and it will print all the number
# so here we also run a loop but we have do it by recursion

# def show(n):
#     if (n == 0): # jab wo number 0 ho jaaye to hum return kar jaaye
#         return
#     print(n)
#     show(n-1)
# show(5)
# this function is called recursive function

# recursion through factorial 
# like returns n!
# def fact(n):
#     if (n == 0 or n == 1): # jab wo number 0 ho jaaye to hum
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))
# n! = (n-1)! * n menas 5 factorial is 4 factorial * 5

# Let‘s Practice
# Write a recursive function to calculate the sum of first n natural numbers. 
# def sum_natural(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_natural(n-1)  # ye bol rha ki pehle sum of 4 cal krlo phir 5 ko add krdo , sum (3) cal krlo phir 4 ko add krdo like
# print(sum_natural(5))

#OR

# def calc_sum(n):
#     if (n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(5)
# print(sum) #output: 15


# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

# def print_list(list, idx):
#     if (idx == len(list)):  # yaha check kiya 0 length ke barara hai nhi hai to print karwa diya 
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["mango", "apple", "banana", "pineapple"]
# print_list(fruits, 0) #output: mango, apple, banana, pineapple

#FILE INPUT / OUTPUT 

#  Python can be used to perform operations on a file. (read & write data)
#  Types of all files
#  1.Text Files : .txt, .docx, .log etc.
#  2. Binary Files : .mp4, .mov, .png, .jpeg etc.

# Open, read & close File
#  We have to open a file before reading or writing.
#  f = open( “file_name”, “mode”)
# file name are simple txt or demo.docx and mode is read or write mode
#  r : read mode
#  w : write mode
#  open method help to return our file


# f = open("demo.txt", "r")
# data = f.read()  #read the file
# print(data)
# f.close()

# we can pass parameter that if we want to read the particular line  
# f = open("demo.txt", "r")
# data = f.read(5)  #read the file
# print(data)
# f.close()

#  we can read a single line 
# f = open("demo.txt", "r")
# line1 = f.readline()  #read the file
# print(line1)
# f.close()


# Writing to a file
#  f = open( “demo.txt”, “w”)
#  f.write( “this is a new line“ ) #overwrites the entire file
#  f = open( “demo.txt”, “a”)
#  f.write( “this is a new line“ ) #adds to the file

# f = open("demo.txt", "w")
# f.write("this is a new line")
# f.close()

# this will automaticlly create a new file
# f = open("sample.txt", "w")
# f.close()/

# if we want to read and write at the same time
# f = open("demo.txt", "r+")
# f.write("this is a new line")
# f.close()

# r+ is used for read+ overwrite and pointer start me hota hai and no truncate
# w+ is used for read+ overwrite and pointer start and end me hota agar delete hota hai and truncate
# a+ is used for read+ append and pointer end me hota hai and no truncate

# with Syntax
#  with open( “demo.txt”, “a”) as f: #now this will act as f
#          data = f.read( ) 

# Deleting a File
#  using the os module
#  Module (like a code library) is a file written by another programmer that generally has
#  a functions we can use.
#  import os #it is pre installed in python like if we run this then no error will come 
#   os.remove( filename ) 

# Let‘s Practice
#  Create a new file “practice.txt” using python. Add the following data in it: 
#  Hi everyone
#  we are learning File I/O using Java. 
#  I like programming in Java

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O using Java.\nI like programming in Java")

# WAF that replace all occurrences of “Java” with “python” in above file   
#  so here we first read the data then overwrite it.

# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

# Search if the word “learning” exists in the file or not. 
# with open("practice.txt","r") as f:
#      data = f.read()
#      if "learning" in data:
#           print("Yes, the word exists in the file")
#      else:
#          print("No, the word does not exist in the file")

# we can also write this as a function then we can call it
# def check_for_word():
#      word = "learning"
#      with open("practice.txt","r") as f:
#          data = f.read()
#          if "learning" in data:
#              print("Yes, the word exists in the file")
#          else:
#              print("No, the word does not exist in the file")

# check_for_word()

# WAF to find in which line of the file does the word “learning”occur first. 
# Print -1 if word not found. 

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O using Java.\nI like programming in Java")


# def check_for_word():
#      word = "learning"
#      with open("practice.txt","r") as f:
#          data = f.read()
#          if "learning" in data:
#              print("Yes, the word exists in the file")
#          else:
#              print("No, the word does not exist in the file")

# check_for_word()

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         for line in f:
#             while data:
#                 data = f.readline()
#                 if(word in data):
#                     print(line_no)
#                     return
#                 line_no += 1
#     return -1
# print(check_for_line())
#OOPs IN PYTHON

#  To map with real world scenarios, we started using objects in code.
#  This is called object oriented programming. 

# function ki wajah se redundancy decrease ho jaati hai reusability increase ho jaati hai 
#koi chiz repeat ho rhi hai to usko combine krke ek function bana do to uski redundancy decrease ho jaati hai

# Class & Object in Python
#  Class is a blueprint for creating objects.(it tells object ke andar kya kya feature honge.)
#  #creating class
#  class Student:   
# name = “karan kumar”
#  #creating object (instance)
#  s1 =  Student( )
#  print( s1.name ) 

# class Student:
#     name = ("Aman") # here we define the object so every time when we call the name for any student it will print Aman
  
# s1 = Student() #this is an object
# print(s1.name)

# s2 = Student()
# print(s2.name)

# _ _init_ _ Function
 
#  Constructor
#  All classes have a function called __init__(), which is always executed when the object is being
#  initiated.

#  #creating class
#  class Student: 
# def __init__( self, fullname ):
#  self.name =  fullname

#  #creating object
#  s1 =  Student( “karan” )
#  print( s1.name ) 

# *The self parameter is a reference to the current
#  instance of the class, and is used to access variables
#  that belongs to the class.

# class car:
#     color = "black"
#     model = "maruti"

# car1 = car()
# print(car1.color)
# print(car1.model) # output: black, maruti

# class Student:
#     name = "Aman"
#     def __init__(self):
#         print("adding new student in the database")
# s1 = Student() # this () paranthesis is use to call the function def__init__


# class Student:
#     name = "Aman"
#     def __init__(self, fullname): #pehle hmne object banaya phir constructor banaya
#         self.name = fullname # we use this because we don't want to give same name to every student
# #so jo bhi value hm student me pass karenge wo full name me aa jaayegi and self ke andar wo value assign ho jaayegi
      
#         print("adding new student in the database")
# s1 = Student("Aman")
# print(s1.name) # output: Aman

# s2 = Student("Monu")
# print(s2.name) #output: Monu

# ye jitne bhi data hmne store kiya usko attribute kehte hai

# class Student:
#     name = "Aman"
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks
#         print("adding new student in the database")
# s1 = Student("Aman", 95)
# print(s1.name, s1.marks)

# s2 = Student("Monu", 91)
# print(s2.name, s2.marks)

# Class & Instance Attributes
#  Class.attr
#  obj.attr

# class Student:
#     college_name = "ABC" # Clg name to sare student ke liye same hi rahega to ek hi baar usko memory me define kiye hai 
 
    
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks
#         print("adding new student in the database")
# s1 = Student("Aman", 95)
# print(s1.name, s1.marks)

# s2 = Student("Monu", 91)
# print(s2.name, s2.marks)
# print(s2.college_name) # output: ABC
# #or
# print(Student.college_name) # output: ABC

# Methods
#  Methods are functions that belong to objects.
#  #creating class
#  class Student: 
# def __init__( self, fullname ):
#  self.name =  fullname
#  def hello( self ):
#  print( “hello”, self.name)

#  #creating object
#  s1 =  Student( “karan” )
#  s1.hello()


# class Student:
#     college_name = "ABC" 
    
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks

#     def welcome(self):
#         print("Welcome student", self.name)

#     def get_marks(self):
#         return self.marks
      
# s1 = Student("Aman", 95)
# s1.welcome() # output: Welcome student
# print(s1.get_marks())

# Let‘s Practice
#  Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is:", sum/3)
     
        
# s1 = Student("Aman", [99, 98, 97])
# s1.get_avg()


# Static Methods
#  Methods that don’t use the self parameter (work at class level)
 
#  class Student: 
#      @staticmethod    #decorator
#      def college( ):
#          print( “ABC College” )
 
#  *Decorators allow us to wrap another function in order to
#  extend the behaviour of the wrapped function, without
#  permanently modifying it


# Important
#  Abstraction
#  Hiding the implementation details of a class and only showing the essential features to the user.
#  Encapsulation
#  Wrapping data and functions into a single unit (object).
#  Inheritance
#  Creating a new class from an existing class.
#  Polymorphism
#  Ability of an object to take on multiple forms.


  










