import operator
import trig

x = operator.add(12,34)

print(x)

x = operator.subtract(45,23)

print(x)


from operator import add

x = add(45,23)


print(x)

from operator import subtract

x = subtract(89,45)

print(x)


#import operators modules

import operator

import others

#build a better calculator
x = others.cube(9)
x = operator.add(7,8)

#get numbers

if operator== "cube":
    num = eval(input("enter a number:"))
    x = others.cube(num)
    print(x)

elif operator == "sin":
    angle = eval(input("enter angle in degrees:"))
    sin_of_angle = trig.get_sine(angle)
    print(sin_of_angle)

num1 = eval(input("enter a number1;"))
num2 = eval(input("enter a number2;"))
operators = input("enter an operator;")

if operator == "+":
    x = operator.add(num1,num2)
    print(x)

elif operator == "-":
    x = operators.subtract(num1,num2)

elif operator == "x" or "x" or "X":
    x = operator.multiply(num1,num2)
    print(x)



    
