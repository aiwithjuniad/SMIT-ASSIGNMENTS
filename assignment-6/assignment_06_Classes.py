
## CLASSES

# 1- Write a Python program to create a class representing a Circle. Include methods to
# calculate its area and perimeter.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
cir = Circle(int(input("Enter circle radius here: ")))
print(f"Your radius is {cir.radius}")
print(f"Circle area is {round(cir.area(),2)}")
print(f"Circle perimeter is {round(cir.perimeter(),2)}")


# 2- Write a Python program to create a person class. Include attributes like name, country
# and date of birth. Implement a method to determine the person's age.

from datetime import date

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    def age(self, current_date):
        dob_day, dob_month, dob_year = map(int, self.date_of_birth.split("-"))
        cur_day, cur_month, cur_year = map(int, current_date.split("-"))

        age = cur_year - dob_year
        if(cur_month, cur_day) < (dob_month, dob_day):
            age -= 1
        return age
today = date.today()
current_date = today.strftime("%d-%m-%Y")

person_data = Person(name = input("Enter your name here: "),
                     country = input("Enter your country name here: "),
                     date_of_birth = input("Enter your date of birth here (dd-mm-yyyy): "))
print(f"Name: {person_data.name}")
print(f"Country: {person_data.country}")
print(f"DOB: {person_data.date_of_birth}")
print(f"Age: {person_data.age(current_date)}")


# 3- Write a Python program to create a calculator class.Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

a = int(input("Enter your a value here: "))
operator = input("Enter operator here ('+', '-', '*', '/'): ")
b = int(input("Enter your b value here: "))

calculate = Calculator()
if operator == '+':
    print(f"The addition of {a} {operator} {b} =", calculate.add(a, b))
elif operator == '-':
    print(f"The subtraction of {a} {operator} {b} =", calculate.sub(a, b))
elif operator == '*':
    print(f"The multiplication of {a} {operator} {b} =", calculate.mul(a, b))
elif operator == '/':
    print(f"The division of {a} {operator} {b} =", calculate.div(a, b))
else:
    print("Invalid operator")