
## List Assignment


# 1. Write a program that accepts a list from user and print the alternate element of list.

user = input("Enter elements you want to get alternate: ")
alternate = user[::2]
print("Alternate user list is: ['" + alternate + "']")


# 2. Write a program that accepts a list from user.
# Your program should reverse the content of list and display it. Do not use reverse() method.

user_data = input("Enter characters u want to reverse (use space after every content): ")
user_list = user_data.split()
reverse = user_list[::-1]
print(f"Reverse list are:{reverse}")


# 3. Find and display the largest number of a list without using built-in function max().
# Your program should ask the user to input values in list from keyboard.

find = input("Enter digits here: ")
num_list = list(map(int, find.split()))
largest = num_list[0]
# 
for num in num_list[1:]:
    if num > largest:
        largest = num
print(f"Largest number in list is: {largest}")


# 4. Write a program that rotates the element of a list so that the element at the first index
# moves to the second index, the element in the second index moves to the third index, etc.,
# and the element in the last index moves to the first index.

lst = input("Enter elements separated by space: ").split()
rotate = lst[-1:] + lst[:-1]
print(rotate)


# 5. Write a program that input a string and ask user to delete a given word from a string.

string = input("Enter sentence here: ")
delete = input("Enter word u want to delete: ")
new_string = string.replace(delete,"")
print("New String is:",new_string)


# 6. Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.
# It should print the date in the form March 12, 2021.

user_date = input("Enter you date here (mm/dd/yyyy): ")
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
mm, dd, yyyy = user_date.split('/')
months_name = months[int(mm)-1]
print(f"{months_name} {dd}, {yyyy}")


# 7. Write a program with a function that accepts a string from keyboard and create a new
# string after converting character of each word capitalized. For instance, if the sentence
# is "stop and smell the roses." the output should be "Stop And Smell The Roses"

string = input("Enter your sentence here: ")
keyword = string.split()
sentence = ''
for k in keyword:
    sentence += k[0].upper() + k[1:].lower() + ' '
print("Capatlized Sentence:", sentence.strip())


# 8. Find the sum of each row of matrix of size m x n. For example for the following matrix
# output will be like this:
# 2 11 7 12
# 5 2 9 15
# 8 3 10 42
# Sum of row 1 = 32
# Sum of row 2 = 31
# Sum of row 3 = 63

row = [
    [2, 11, 7, 12],
    [5, 2, 9, 15],
    [8, 3, 10, 42],
    [4, 89, 548, 56]
]
for i in range(len(row)):
    row_sum = sum(row[i])
    print(row[0 + i])
    print(f"Sum of row{i + 1} = {row_sum}")

# 9. Write a program to add two matrices of size n x m.

A = [[2,11],[7,12],[5,2]]
B = [[9,15],[8,3],[10,42]]
add = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    add.append(row)
print('Sum of Matrices:')
for row in add:
    print(row)

# 10. Write a program to multiply two matrices

a = [[2,11],[7,12],[5,2]]
b = [[9,15],[8,3],[10,42]]
multiply = []
for i in range(len((a))):
    row = []
    for j in range(len(a[0])):
        row.append(a[i][j] * b[i][j])
    multiply.append(row)
print("Multiple of Matrices: ", multiply)