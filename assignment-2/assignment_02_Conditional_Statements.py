
## Part -2 Conditional Statements


# 1- A company decided to give bonus of 5% to employee if his/her year of service is more than
# 5 years.Ask user for their salary and year of service and print the net bonus amount.

service = int(input("How many years of service in our company: "))
if service > 5:
    salary = int(input("Enter your salary here: "))
    bonus = salary * 5 / 100
    print(bonus)
else:
    print("Sorry.. you are not eligible for bonus")


# 2- Write a program to check whether a person is eligible for voting or not (accept age from user)
# if age is greater than 17 eligible otherwise not eligible

user_age = int(input("Enter your age here: "))
if user_age > 17:
    print("You are eligible for voting")
else:
    print("Sorry you are not eligible for voting")


# 3- Write a program to check whether a number entered by user is even or odd.

check = int(input("Enter your number here: "))
if check % 2 == 0:
    print("It's Even...")
else:
    print("It's Odd...")


# 4- Write a program to check whether a number is divisible by 7 or not. Show Answer

num = int(input("Enter you want to check: "))
if num % 7 == 0:
    print("Your number is divisible by 7")
else:
    print("Your number is not divisible by 7")


# 5- Write a program to display "Hello" if a number entered by user is a multiple of five,
# otherwise print "Bye".

divisible = int(input("Enter your number here: "))
if divisible % 5 == 0:
    print("Hello...")
else:
    print("Bye....")

# 6- Write a program to calculate the electricity bill (accept number of unit from user)
# according to the following criteria:
# Unit Price upto 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per
# unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if
# input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than
# total bill amount is Rs.750

user_unit = int(input("Enter your monthly units here: "))
bill = float(0)
if user_unit >= 0 and user_unit <= 100:
    print(f"Total bill amount is Rs: 0")
elif user_unit > 100 and user_unit <= 200:
    print(f"Total bill amount is Rs: {user_unit * 5}")
elif user_unit > 200:
    print(f"Total bill amount is Rs: {user_unit * 10}")
else:
    print("Invalid Amount")

# 7- Write a program to display the last digit of a number.

digit = int(input("Enter your digit here: "))
last_digit = digit % 10
print(f"Your digit is: {digit}\n Their last digit is: {last_digit}")

# 8- Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

length = int(input("Enter length here: "))
breadth = int(input("Enter breadth here: "))
if length == breadth:
    print("It's Square...")
else:
    print("It's Rectangle...")

# 9- Take two int values from user and print greatest among them.

val_1 = int(input("Enter first value here: "))
val_2 = int(input("Enter second value here: "))
if val_1 > val_2:
    print(f"The max value is first value: {val_1}")
elif val_2 > val_1:
    print(f"The max value is second value: {val_2}")
else:
    print(f"Both value are same")

# 10- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("Enter your purchase quantity here: "))
cost = 100
total_cost = quantity * cost
if total_cost > 1000:
    discount = total_cost * 10 / 100
    discounted_cost = total_cost - discount
    print(f"Congrats you are offering discount\nYour cost is: {discounted_cost}")
else:
    print(f"Sorry you are not offering discount\nYour cost is: {total_cost}")

# 11- A school has following rules for grading system:

# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

student_marks = int(input("Enter your marks here: "))
if student_marks < 25 and student_marks <=0:
    print("You are 'Fail'")
elif student_marks > 25 and student_marks <= 45:
    print("Your Grade is 'E'")
elif student_marks >= 45 and student_marks < 50:
    print("Your Grade is 'D'")
elif student_marks >= 50 and student_marks < 60:
    print("Your Grade is 'C'")
elif student_marks >= 60 and student_marks < 80:
    print("Your Grade is 'B'")
elif student_marks >= 80:
    print("Your Grade is 'A'")
else:
    print("Invalid Marks")

# 12- A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user:

# Number of classes held
# Number of classes attended.
# And print percentage of class attended
# Is student is allowed to sit in exam or not.

class_held = int(input("Enter classes total held: "))
class_attend = int(input("Enter classes total attend: "))
percentage_class = class_attend / class_held * 100
print(f"Your Percentage of class is: {percentage_class}")
if percentage_class >= 75:
    print("Welcome you are allow to sit in exam")
else:
    print("Sorry you are not allow to sit in exam")

# 13- Take input of age of 3 people by user and determine oldest and youngest among them.

age_1 = int(input("Enter age here: "))
age_2 = int(input("Enter age here: "))
age_3 = int(input("Enter age here: "))

oldest = max(age_1, age_2, age_3)
youngest = min(age_1, age_2, age_3)
print("Oldest Age is: ",oldest)
print("Youngest Age is: ",youngest)

# 14- Modify the above question to allow student to sit if he/she has medical cause. Ask user
# if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

class_held = int(input("Enter classes total held: "))
class_attend = int(input("Enter classes total attend: "))
percentage_class = class_attend / class_held * 100
medical_cause = input("Enter your medical cause? (Y/N): ").strip().upper()
if percentage_class >= 75 and medical_cause == 'Y':
    print("Welcome you are sit in exam...")
elif percentage_class < 75 and medical_cause == 'N':
    print("Sorry you are not sit in exam....")
else:
    print("Invalid Input")

# 15- Write a program to check if a year is leap year or not. If a year is divisible by 4 then
# it is leap year but if the year is century year like 2000, 1900, 2100 then it must be
# divisible by 400.

year = int(input("Enter year here: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It's Leap Year...")
else:
    print("No It's Not a Leap Year...")

# 16- Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using
# following rules print their place of service.

# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere.
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".

marital_status = input("Enter your marital status here (Y/N): ").strip().upper()
gender = input("Enter your gender here (M/F): ").strip().upper()

if gender == "F":
    print("Work only in urban areas...")
elif gender == "M":
    age = int(input("Enter your age here: "))
    if age >= 20 and age <= 40:
        print("Work anywhere u want...")
    elif age > 40 and age <= 60:
        print("Work only in urban areas...")
    else:
        print("Invalid age")
else:
    print("Invalid Gender....")