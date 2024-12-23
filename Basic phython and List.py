#1.print "Hello Python"

print("Hello Phython")

#2. arithmetic operations

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b

print("Addition: ",addition)
print("Subtraction:",subtraction)
print("Multiplication:",multiplication)
print("Division:",division)
print("Floor Division:",floor_division)
print("Modulus:",modulus)
print("Exponentiation: ",exponentiation)

#3.area of a triangle

b = float(input("Enter base : "))
h= float(input("Enter height : "))

area = 0.5 * b * h

print("area of triangle :", area)

#4.quadratic equation

import cmath  # Importing the cmath module to handle complex square roots

# Input coefficients a, b, and c
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Find two solutions (handling complex roots with cmath)
x = (-b - cmath.sqrt(d)) / (2*a)
y = (-b + cmath.sqrt(d)) / (2*a)


print('The solutions are {0} and {1}'.format(x, y))

#5.swap two variables

M = input("Enter  value  M: ")
S = input("Enter  value  S: ")

M, S = S, M

print("After swapping:")
print("M =", M)
print("S =", S)

#6.Generate a Random Number

import random

random_number = random.randint(1, 100)

print("Random number:", random_number)

#7.convert kilometers to miles

km = float(input("Enter the distance in km: "))

# Conversion factor
CF = 0.621371

m = km * CF

print(f"{km} kilometers is equal to {m} miles")

#8.convert Celsius to Fahrenheit

c = float(input("Enter temperature in Celsius: "))

f = ( 9/5 * c ) + 32

print(f"{c}°C is equal to {f}°F")

#9.display calendar

import calendar

yy = int(input("Enter year: ")) #yy = 2000
mm = int(input("Enter month: ")) #mm = 10

print(calendar.month(yy, mm))

#10.check if a Number is Positive, Negative or Zero

def check_number(num):
    if num > 0:
        print("is a Positive number",num)
    elif num < 0:
        print("is a Negative number",num)
    else:
        print("The number is Zero.")

number = float(input("Enter  number: "))

# Call the function
check_number(number)

#11.check if a Number is Odd or Even

num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even",{num} )
else:
    print("Odd",num)

#12.check Leap Year

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("is a Leap Year.",year)
else:
    print("is not a Leap Year.",year)

#13.check Prime Number

num = int(input("Enter number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("is not a Prime number.",num)
            break
    else:
        print("is a Prime number.",num)
else:
    print("is not a Prime number.",num)

#14.print all Prime Numbers in an Interval

start = int(input("Enter start of interval: "))
end = int(input("Enter end of interval: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

#15.Find the Factorial of a Number

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

num = int(input("Enter number: "))
print(f"Factorial of {num} is {factorial(num)}.")

#16.display the Multiplication Table

num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#17.print the Fibonacci Sequence

n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

#18.Check Armstrong Number

num = int(input("Enter a number: "))
order = len(str(num))
sum_of_digits = sum(int(digit) ** order for digit in str(num))

if num == sum_of_digits:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#19.find Armstrong Numbers in an Interval

start = int(input("Enter start of interval: "))
end = int(input("Enter end of interval: "))

for num in range(start, end + 1):
    order = len(str(num))
    if num == sum(int(digit) ** order for digit in str(num)):
        print(num)

#20.Find the Sum of Natural Numbers

n = int(input("Enter a number: "))
sum_n = n * (n + 1) // 2
print(f"Sum of first {n} natural numbers is {sum_n}.")

#21.Print Reverse of a String

string = input("Enter a string: ")
print(f"Reversed string is: {string[::-1]}")

#22.Print Sum of First Ten Natural Numbers

print(f"Sum of first 10 natural numbers is {sum(range(1, 11))}.")

#23.7Find LCM

import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"LCM of {x} and {y} is {lcm(x, y)}.")

#24.Find HCF

import math  # Import the math module
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"HCF of {x} and {y} is {math.gcd(x, y)}.")

#25.Convert Decimal to Binary, Octal, and Hexadecimal

num = int(input("Enter a decimal number: "))
print(f"Binary: {bin(num)[2:]}")
print(f"Octal: {oct(num)[2:]}")
print(f"Hexadecimal: {hex(num)[2:]}")

#26.Find ASCII value of a Character

char = input("Enter a character: ")
print(f"ASCII value of '{char}' is {ord(char)}.")

#27.Make a Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else 'Undefined (cannot divide by zero)'

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    print(f"Result: {add(a, b)}")
elif operation == '-':
    print(f"Result: {subtract(a, b)}")
elif operation == '*':
    print(f"Result: {multiply(a, b)}")
elif operation == '/':
    print(f"Result: {divide(a, b)}")
else:
    print("Invalid operation!")

#28.Display Fibonacci Sequence Using Recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = int(input("Enter number of terms: "))
for i in range(n_terms):
    print(fibonacci(i), end=' ')

#29.Find Factorial of a Number Using Recursion

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}.")

#30.Calculate the Power of a Number

def power(base, exp):
    return base ** exp

base = float(input("Enter base: "))
exp = int(input("Enter exponent: "))
print(f"{base} to the power of {exp} is {power(base, exp)}.")

#31.Add Two Matrices

matrix1 = [[9, 7], [1, 3]]
matrix2 = [[5, 1], [7, 9]]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

for row in result:
    print(row)

#32.Multiply Two Matrices

matrix1 = [[3, 2], [3, 4]]
matrix2 = [[5, 7], [7, 8]]

result = [[0, 0], [0, 0]]


for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result:
    print(row)

#33.Transpose a Matrix

matrix = [[1, 5, 3], [4, 5, 3], [7, 8, 9]]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for row in transpose:
    print(row)

#34.Sort Words in Alphabetic Order

sentence = input("Enter a sentence: ")
words = sentence.split()
words.sort()
print("Sorted words:", " ".join(words))

#35.Remove Punctuation From a String

import string

text = input("Enter a string: ")
cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
print("String without punctuation:", cleaned_text)

#36.Convert List to String

lst = ['My', 'Name', 'is Shakib']
result = " ".join(lst)
print(result)

#37.Convert Int to String

num = 739
print("String representation of number:", num)

#38.Concatenate Two Strings

str1 = "Musfiqur"
str2 = "Shakib"
result = str1 + str2
print(result)

#39.Generate a Random String

import random
import string


length = int(input("Enter the length of the random string: "))
result = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
print(f"Random string: {result}")

#40.Check Whether a Given String is a Palindrome or Not

a = input("Enter string: ")

# Normalize the string: convert to lowercase and remove spaces
b = a.replace(" ", "").lower()

# Check if the normalized string is a palindrome
if b == b[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#41Convert the String into Lowercase to Uppercase and Vice Versa

string = input("Enter a string: ")
swapped = string.swapcase()
print(f"Swapped case: {swapped}")

#42.Find the Occurrence of a Substring Within a String

string = input("Enter the main string: ")
substring = input("Enter the substring to find: ")
count = string.count(substring)
print(f"'{substring}' occurs {count} times in the string.")

#43.Append Element in the List

lst = [1, 2, 3, 4, 5, 6, 7,8,9,11,13]
a = int(input("Enter element to append: "))
lst.append(a)
print("Updated list:", lst)

#44.Compare Two Lists

list1 = [1, 5, 3]
list2 = [1, 5, 3]

if list1 == list2:
    print("Both lists are equal.")
else:
    print("Lists are not equal.")

#45.Convert List to Dictionary

keys = ['Name', 'Age', 'City']
values = ['Musfiqur Shakib', 23, 'Uttara ,Dhaka']

dictionary = dict(zip(keys, values))#mapping the keys and values in the dictionary
print("Converted dictionary:", dictionary)

#46.Remove an Element from a List

lst = [1, 3, 5,7 ,9]
a = int(input("Enter element to remove: "))
lst.remove(a)
print("Updated list:", lst)

#47.Add Two Lists

list1 = [1,3,5,7,9 ]
list2 = [11,13,15,17,19]

result = list1 + list2#join or adding to list into new one
print("Combined list:", result)

#48.Convert List to Set

list = [1, 3,   5, 7,9]
set_result = set(list)
print("Converted set:", set_result)

#49.Convert List to String

list = ['My', 'name', 'is' , 'Shakib']
result = " ".join(list)
print("Converted string:", result)
