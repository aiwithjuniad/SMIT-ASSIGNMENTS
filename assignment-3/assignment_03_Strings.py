
### Strings Assignments

# 1. Write a program that accepts a string from user. Your program should count and display number of
# vowels in that string.

string = input("Enter your words here: ")
vowels = 'aeiouAEIOU'
count = sum(map(string.count, vowels))

if count > 0:    
    print("Number of vowels: ", count)
else:
    print("no vowels")

string = input("Enter your word here: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)


# 2. Write a program that reads a string from keyboard and display:
# The number of uppercase letters in the string
# The number of lowercase letters in the string
# The number of digits in the string
# The number of whitespace characters in the string

keyboard = input("Enter you want to check: ")
uppercase = sum(map(str.isupper, keyboard))
lowercase = sum(map(str.islower, keyboard))
digits = sum(map(str.isdigit, keyboard))
whitespace = sum(map(str.isspace, keyboard))
print(f"Uppercase Letters in this word is: {uppercase}")
print(f"Lowercase Letters in this word is: {lowercase}")
print(f"Digits in this word is: {digits}")
print(f"Whitespace in this word is: {whitespace}")


# 3. Write a Python program that accepts a string from user. Your program should create and display a new
# string where the first and last characters have been exchanged.
# For example if the user enters the string 'HELLO' then new string would be 'OELLH'

string = input("Enter string u want to change: ")
exchange = string[-1] + string[1:-1] + string[0]
print('Exchanged String:', exchange)

# 4. Write a Python program that accepts a string from user. Your program should create a new
# string in reverse of first string and display it.
# For example if the user enters the string 'EXAM' then new string would be 'MAXE'

reverse = input("Enter string u want to reverse: ")
new_string = string[::-1]
print("Reversed String:", new_string)

# 5. Write a Python program that accepts a string from user. Your program should create a new
# string by shifting one position to left.
# For example if the user enters the string 'examination 2021' then new string would be 'xamination 2021e'

str = input("Enter word you want to shift: ")
shift = str[1:] + str[0]
print(shift)

# 6. Write a program that asks the user to input his name and print its initials. Assuming that the user
# always types first name, middle name and last name and does not include any unnecessary spaces.
# For example, if the user enters Ajay Kumar Garg the program should display A. K. G.
# Note: Don't use split() method

name = input("Enter your full name here (Without unnecessary spaces): ")
initial_1 = name[0]
first_space = name.find(" ")
initial_2 = name[first_space + 1]
second_space = name.find(' ', first_space + 1)
initial_3 = name[second_space + 1]
print(initial_1 + '. ' + initial_2 + '. ' + initial_3)


# 7. A palindrome is a string that reads the same backward as forward. For example, the words dad, madam
# and radar are all palindromes. Write a programs that determines whether the string is a palindrome.
# Note: do not use reverse() method

string = input("Enter word u want to check palindrome: ")
cleaned = ""
reverse = ""

for i in string:
    if i.isalpha():
        ch = i.lower()
        cleaned += ch
        reverse = ch + reverse
if cleaned == reverse:
    print("It's palindrome")
else:
    print("It's not a palindrome")


# 8. Write a program that display following output:
# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT

word = input("Enter words you want to shift: ")
print(word)
for i in range(len(word)):
    word = word[1:] + word[0]
    print(word)


# 9. Write a program in python that accepts a string to setup a passwords.
# Your entered password must meet the following requirements:
# The password must be at least eight characters long.
# It must contain at least one uppercase letter.
# It must contain at least one lowercase letter.
# It must contain at least one numeric digit.
# Your program should should perform this validation.

password = input("Enter you password here(must uppercase, lowercase, digits, 8 character): ")
length = len(password) >= 8
uppercase = any(map(str.isupper, password))
lowercase = any(map(str.islower, password))
digits = any(map(str.isdigit, password))
if length and uppercase and lowercase and digits:
    print(password)
else:
    print("Make stronger password.....")