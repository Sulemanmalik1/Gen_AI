# 01 - display the result to output
# print("hello world")
# print(34)
# print(True)
# print(type("hello world 56"))

# 02 - legal name of variables

# name = "Khurram"
# firstName = "ali" # camel case;
# FirstName = "aslam" # pascal case;
# first_name = "ali" # snake case;
# name1st = "alia" # number case; case sensitive;


# 03 - type of variables;

# print(type(23))
# print(type(True))
# print(type("34"))

# 04 data types in python

# a = "string"
# b = True
# c = 34
# d = 34.5
# e = 1j
# f = ["aslam","amna","mehmona"] 
# g = ("hello","world","!")
# h = {"name":"umar","age":23}
# i = b"hello world"
# j = {"hi","many","fight"}

# 05 math operation

# a = 4
# b = 2
# sum =  a + b 
# print(sum , type(sum))
# print(a ** b)

# 06 input type 

# a = input("Enter you name : ")
# print(a,type(a))

# 07 if conditions 

# num = 101
# if (num >= 45 and num <= 50 ) :
#     print("you are passed")
# elif (num >= 90 and num > 101) :
#     print("you are passed Grad A")
# else :
#     print("you are not passsed")

# num = 20
# num2 = 60
# if num == 20:

#     if num2 == 40:
#         print("you got both right")
#     elif num2 == 60:
#         print("hurrey you got it")
#     else :
#         print("you have wrong")
# else:
#    print( "you got both wrong")

# marks = 90
# if marks > 80:
#     print("passed")
# elif marks > 85:
#     print("passed Grade a")

# 08 typ casting

# num = "45"
# num = int(num)
# print(type(num))

# num2 = 45
# num2 = str(num2)
# print(type(num2))

# num3 = "43.0"
# num3 = float(num3)
# print(type(num3))

# val = input("Enter your age in number : ")
# val1 = int(val)
# print(type(val1) , type(val))


# 01 Assignment solution

# edu = int(input("Enter you education : "))
# age = int(input("Enter you age : "))
# height = float(input("Enter you height : "))

# if( edu >= 12 and (age <= 32 and age >= 18)):
#     print("Passed")
# elif( (age <= 32 and age >= 18) and height >= 5.6 ) :
#     print("Passed")
# elif(  height >= 5.6 and edu >= 12 ) :
#     print("Passed")
# else:
#     print("Failed")

# 09  multiline string

# b = """hello world how are
#  you;"""
# print(b)

# c = """hello world"""
# print(type(c), len(c))

# 10 concatenation 

# a = "hello"
# b = "World"
# print(a + " " + b)

# a = 42
# b = 43
# c = "hello world!"
# print( str(a) + b + " " + c)


# 11  format in string and integers / float
# marks = 45
# total = " your total marks is 100 and you got {}"
# obt = total.format(marks)
# print(obt)

# age = 24
# total = 100
# obt = 90
# res = " your age is {0} and your total marks {2} and obtain marks {1}"
# tot = res.format(age,obt,total)
# print(tot)


# 12 string slicing

# a = "hello world!"
# print(a[-3:-1])
# print(a[0:])
# print(a[:5])

# 13  split in string

# a = "hello AI class"
# b = a.split(" ")
# print(a, b)

# 14  uppar case lower case in string

# st = "Hello World!"
# up = st.upper()
# lo = st.lower()
# print(up, lo) 
# print( st.upper(), st.lower())
# st = "hello world"
# print(st.capitalize(),st.title())

# a = "hello"
# b = "world"
# print( a.capitalize() + " " + b.capitalize())

# 02 assignment solution 

# a = "jaranwala faisalabad lahore"
# print( a[0:1].upper() + a[1:9] , a[10:11].upper() + a[11:20] , a[21:22].upper() + a[22:]   )


# 15 replace methods 
# a = "hello"
# b = a.replace("h","H")
# print(b)

# 03 assignment home 

# st = "Jaranwala Faisalabad Lahore Karachi Multan" # don't use the slice method and replace first letters in small;


# 15 lists  

 # ls = list(("Lahore","Faisalabad","Jaranwala")) # constructor method

# ls= []
# ls = [ "Lahore","Faisalabad","Jaranwala"]
# print(type(ls), ls)
# print(type(ls), ls)

# ls = ["Lahore","Faisalabad","Jaranwala"]

# print(ls[2:])

# ls[1] = "Multan"
# ls[0:1] = [ "Karachi"]
# ls[2:] = ["Multan"]
# ls[1:2] = ["Peshawar"]
# ls[0:] = ["Lahore","Faislabad","Jaranwala","Peshawar"]
# print(ls)

# ls = ["Lahore","Faisalabad","Jaranwala"]
# ls.append("Peshawar")
# ls.insert(2,"Peshawar")
# ls.pop(0)
# ls.remove("Faisalabad")
# del ls

# ls.clear()
# print(ls)

# 16 for loops 

# ls = ["apple","banana","mango", "orange"]

# print(ls)
# for item in ls:
#     print(item)

# Assignments class 19/ 03/ 2025:______________________

# ls = ["lahore","faisalabad","jaranwala"]
# lp=[]
# for x in ls:
#     p = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper()
#     lp.append(p)
#     print(p)
# print(lp)

# ls = [ "lahore","Faisalabad","jaranwala"]
# lp = []
# for x in ls:
#     lp.insert(0,x)
# print(lp23423423g)

# While Loop
# i=0
# while i<=20:
#     print(i)
#     i=i+2

#For loop
# i=[0,2,4,6,8,20,12,14,16,18,20]
# for items in i:
#     print (items)

#List Comprehension

# ls=["Karachi","Islamabad","Jarawanla","kivi"]
# ls2=[]
# for x in ls:
#     if "a" in x:
#         ls2.append(x)
# print(ls2)        

# ls=["Karachi","Islamabad","Jarawanla","kivi"]
# ls2=[x for x in ls if "i" in x] # first x before for command is representing the expression and the x after for is representing items in list.

# print(ls2)

# ls=["Karachi","Islamabad","Jarawanla","kivi"]
# ls2=[x for x in ls if x !="Karachi"]
# print(ls2)

# ls=["Karachi","Islamabad","Jarawanla","kivi"]
# ls2=[x[0].upper()+x[1:] for x in ls]
# print(ls2)

# ls=["Karachi","Islamabad","Jarawanla","kivi"]
# ls2=[x.capitalize() for x in ls]
# print(ls2)

# ls=["Karachi","Islamabad","Jarawanla","kivi"]
# ls2=[x[0].upper()+x[1:-1].lower()+ x[-1:].upper() for x in ls]
# print(ls2)

# ls=["Karachi","Islamabad","Jarawanla","kivi"]
# ls2=[x for x in ls if "F" in x]
# print(ls2)


# While Loop
# i=0
# while i<=20:
#     print("2 *", i , "=", 2*i)
#     i=i+1

#For Loop
# for items in range(1,11):
#     print("2 *", items, "=", 2*items)


# fact=5
# i=1
# while i<5:
#     fact=fact*i
#     i=i+1
# print(fact)    


a = input("Enter 1st value (comma-separated):").split(',')
b = input("Enter 2nd value (comma-separated):").split(',')
print(a+b)

#Therefore, even though you are providing string input, the .split(',') method transforms that string
#into a list of strings, which is then concatenated with another list of strings.

print("git statushello")

 