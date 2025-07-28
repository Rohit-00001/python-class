# Exception handling: Errors in python can be of two types:- SyntaxError and  Exceptions

# Errors   are the problems in a program  due to which the program will not run or execute properly.
# wheras  the exceptions are raised due to the abnormal flow of the program.
# Name errors
# var = 10
# print(hello)
# print"hello


# a= 10
# b= "g"

# try:
#     print("execution started")
#     print(a/b)
#     print("inside try block")
  
    

# except ZeroDivisionError :
    
#     print("Error: Division by zero is not allowed.")
#     print("inside except block")
  
# except TypeError:
#     print("Error: Unsupported operation between different types.")
#     print("inside except block")
  

# finally:
#     print("execution completed")




# Modules: these are the collection of predefined functions and variables which can be imported in the program to use them.

# Math module : extensive functions for mathematical operations

# math.dist() Returns the Euclidean distance between two points
# math.cos () Returns the cosine of a number
# math.ceil() Rounds a number up to the nearest integer
# math.pi Returns PI (3.1415...)
# math.e Returns Euler's number (2.7182...)
# math.tan() Returns the tangent of a number
# math.sqrt() Returns the square root of a number
# math.sin() Returns the sine of a number
# math.radians() Converts a degree value into radiansiterable
# math.prod() Returns the product of all the elements in an
# math.pow)) Returns the value of x to the power of nearest integer

# import math
# print(math.ceil(4.55556666))
# print(math.sqrt(169))
# print(math.sin(90))



# Random methods :- builtin methods that is use to generate random data in python

# randint() Returns a random number between the given range
#  randrange() Returns a random number between the given range
# random()  returns a random number between 0-1


# import random 

# print(random.())


# Calendar: builtin function which gives access to calendar
# import calendar

# print(calendar.calendar(1000))
# print(calendar.month(2025,7))


# PIL - python Image Library

from PIL import Image
# import matplotlib.pylot as py

img = Image.open("C:\Users\DIBYARUPA\Pictures\igris-solo-leveling-uhdpaper.com-4K-7.1071.jpg")

print(img)
print(img.format)