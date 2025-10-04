## Part -1 Python Basics (Variables)


# 1- Print Your Name with your Father name and Date of birth using suitable escape sequence charactor?

print("My Name:\t'Junaid Ahmed'\nFather Name:\t'Ishtiaq Ahmed'\nDOB:\t\t'07-06-2002'")

# 2- Write your small bio using variables and print it using print function?

name = "Junaid Ahmed"
father_name = "Ishtiaq Ahmed"
date_of_birth = "07-06-2025"

print(f"My Name is:\t\t{name}\nMy Father Name is:\t{father_name}\nMy Date of Birth is:\t{date_of_birth}")

# 3- Write a program in which use all the operators we can use in Python?

# AIRTHMETIC OPERATORS
# + addition
# - subtraction
# * multiplication
# / division
# % modulus
# // floor operator
# ** exponentional(power) operator

print(2 + 3)
print(45 - 42)
print(3 * 3)
print(4 / 2)
print(int(4 / 2))
print(4 // 2)
print(11 % 3)
print(2**3)

# Assignment Operators (ADVANCED)
# += plus is equals too
# -= minus is equals too
# /= divide is equals too
# *= multiply is equals too
# //= floor is equals too
# %= module is equals too

num1 = 20
num2 = 10
num1 += num2
print(f"plus equals too: {num1}")
num1 -= num2
print(f"minus equals too: {num2}")
num1 *= num2
print(f"multiply equals too: {num1}")
num1 /= num2
print(f"divide equals too: {num1}")
num1 //= num2
print(f"floor equals too: {num1}")
num1 %= num2
print(f"module equals too: {num1}")

# Comparison Operators (Always Output True Or False)
# == is equals too
# != is not equals too
# > greater than
# < less than
# >= greater than is equals too
# <= less than equals too

print(10 == 10)
print(10 != 5)
print(25 > 5)
print(25 < 5)
print(25 >= 25)
print(25 <= 5)

## Logical Operators
# and (When both condition is true)
# or (atleast one condition is true)
# not (reverse of true or false)

a = 10
b = 25
print(a == b and a != b)
print(a == b or b == a)
x = True
print(not x)

# 4- Completes the following steps of small task:
# - Mention Marks of English, Islamiat and Maths out of 100 in 3 different variables
# - Mention Variable of Total Marks and assign 300 to it
# - Calculate Percentage

English = 80
Islamiat = 90
Maths = 100
obtain_marks = English + Islamiat + Maths
total_marks = 300
print(obtain_marks / total_marks * 100)