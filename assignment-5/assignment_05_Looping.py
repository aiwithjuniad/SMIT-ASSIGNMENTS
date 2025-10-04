
## LOOPING STRUCTURE

# 1. Write a Python program to print the numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)


# 2. Write a Python program to print the numbers from 20 to 1 using a while loop.

for i in range(20, 0, -1):
    print(i)


# 3. Write a program to print even numbers from 1 to 10.

for even in range(1, 11):
    if even % 2 == 0:
        print(even)


# 4. Write a program that prompts the user to enter a number n and prints all the numbers from 1 to n.

n = int(input("Enter number u want to print: "))
for i in range(1, n + 1):
    print(i)


# 5. Write a program that prompts the user to enter a number n, and then prints
# all the odd numbers between 1 and n.

n = int(input("Enter number u want to print: "))
for odd in range(1, n + 1):
    if odd % 2 != 0:
        print(odd)


# 6. Write a program that prints 'Happy Birthday!' five times on screen.

for greet in range(5):
    print("Happy Birthday")


# 7. Write a program that takes a number n as input from the user and generates the first
# n terms of the series formed by squaring the natural numbers.
# Sample output
# Enter a number: 6
# The first 6 terms of the series are:
# 1 4 9 16 25 36

n = int(input("Enter number you want to square: "))
print(f"The First {n} terms of the series are: ")
for num in range(1, n + 1):
    print(num ** 2)


# 8. Write a program that prompts the user to input a number and prints its multiplication table.

table = int(input("Enter your number u want table: "))
print(f"The table of {table} are: ")
for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")


# 9. Write a Python program to print the first 8 terms of an arithmetic progression starting
# with 3 and having a common difference of 4.
# The program should output the following sequence:
# 3 7 11 15 19 23 27 31

for i in range(8):
    print(3 + i * 4)

# 10. Write a Python program to print the first 6 terms of a geometric sequence starting with 2
# and having a common ratio of 3. The program should output the following sequence:
# 2 6 18 54 162 486

for i in range(6):
    print(2 * 3 ** i)


# 11. Write a program that asks the user for a positive integer value. The program should calculate the sum
# of all the integers from 1 up to the number entered. For example, if the user enters 20,the loop will find
# the sum of 1, 2, 3, 4, ... 20.

add = int(input("Enter number u want to sum: "))
if add > 0:
    total = 0
    for i in range(1, add + 1):
        total += i
    print(f"The Sum of 1 to {add} is: {total}")
else:
    print("Enter positive integer")


# 12. write a program that takes a positive integer N as input and calculates the sum of the reciprocals
# of all numbers from 1 up to N. The program should display the final sum.

rec = int(input("Enter positive integer here: "))
if rec > 0:
    sum = 0.0
    for total in range(1, rec + 1):
        sum += 1 / total
    print(round(sum,2))
else:
    ("Enter positive integer")