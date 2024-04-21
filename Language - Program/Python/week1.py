# Basic Syntax
# Will print the same line
# eg
# greet = ("Hello World")
# print(greet, end="!")

# Not on the same lines due to line break
# !\n do linebreak
# eg
# Function hello()
# def hello():
#     print("Hello")
#     print("!\n")
#     print("end")
# print("sample")
# hello()

# when python see the input(), you are required
# to input something in the commandline.
# It will read line by line
# eg
# print("Hello there, what is your name?")
# name=input()
# print("hello, " + name)

# naming variable need to be in snake case, denote the word with "_", cannot start a vairbale with a number
# Dynamically typed Variables (same as javascript): Can change variable or data types such as string or boolean (will print both 1 and false below)
# Stronly typed varable (opposite from JS): can not automatically convert data, have to be concise!
# eg (Dynamically)
# data=1
# print(data)
# data="false"
# print(data)
# Stronly
# print("this will give error!" + data)
# print("this will not give error!" + str(data))

# **Data Types
# _String
# String can be "" or '' 
# String can be multilines withouth br
# _String Interpolation using f and {}
# name="Kim"
# print(f"hello, {name}")

# Format to three decimal places, f = format
# num = 100.525145234623
# print(f"{num:.3f}")

# slice string [i:n]
# negative means counting from the end
# .strip() - use to remove all the white spaces
# .split("where to split or seperator") use to split the strings
# .replace("Old","New") use to replace strings
# name = "Kim Seng Thai"
# print(name[0:5])

# Numbers (int and float)
# Result will always give a float value after calculation (decimal)
# To give a whole number you can use double sign (// or ++)

# Booleans (bool() - to test, falsey and trucey similar to how in JS)

# Data Types
# List - [] (order is important, unmuted - can make any changes, similar to arrays, print( variable[n]))
# Tuple - () (order is important, muted - can not make any changes, print( variable[n]), eg coordinate, color - RBG)
# Set - {} (order is not important, similar to object in JS, no repeated items, access via looping)
# Set - eg
# months = {"Jan", "Feb", "Mar"}
# for month in months:
#     print(month)
# (len(varoiable)) means to ask for the number of index
# Dictionary - {} (order is important with newer version, similar to object in JS, no duplicate)
# person = {"name":"Kim", "age": 26}
# print(person["name"])
# If you dont want to wrap the key in string use dict.
# another_person = dict(name = "John", age = 20)

# Operators
# Arithmetic:   +, -, *, /, %, **, //
# Assignment:   =, +=, -=, *=, /=, %=, etc.
# Comparison:   ==, !=, >, <, >=, <=
# Logical:      and, or, not (similar to || and && in JS)
# Identity:     is, is not (check for if something is not or is)
# Membership:   in, not in (if something is in a variable or not, return boolean)
# eg: word = "hello everyne and the rest of the world"
# print("hello" in word)

# Conditional
# If statement
# Indentation is very important
# x = 10
# if x >= 10:
#     print("OK")
# elif x < 0:
#      print("Negative")    
# else:
#     print("NO OK") 

# Conditional Expressed
# name="Hello"
# print('Hello') if name == "Kim" else print("Bye")
# # This will print Hello

# Pass Statement
# invoke a pass keyword if you want to leave a conditional statement blank
# eg
# else:
    # pass

# Switch Statement
# match...case
# eg
# x = 1
# match(x):
    # case 1: do something
    # case 2: do something


