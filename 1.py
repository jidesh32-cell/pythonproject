# 1. Write a Python script using a for loop and the range() function to iterate through the numbers from 1 up to and including 5.
# Inside the loop, check if each number is even or odd, and then print the result in the format: "Number X is [even/odd]."
# Output
# Number 1 is odd.
# Number 2 is even.
# Number 3 is odd.
# Number 4 is even.
# Number 5 is odd.

for num in range(1, 6):
    if num % 2 == 0:
        print(f"Number {num} is even.")
    else:
        print(f"Number {num} is odd.")
        
# 2. Write a Python script that uses a for loop to calculate the sum of all elements in the given list.
# list = [10,20,30,40]
# Your script must:
# Initialize a variable to keep track of the running total.
# Iterate through the data list using a for loop.
# Inside the loop, print the value currently being added and the new running total.
# Finally, print the total sum after the loop finishes.
# Added 10. Running total is 10.
# Added 20. Running total is 30.
# Added 30. Running total is 60.
# Added 40. Running total is 100.
# Total Sum: 100
data = [10, 20, 30, 40]
total_sum = 0
for num in data:
    total_sum += num
    print(f"Added {num}. Running total is {total_sum}.")
print(f"Total Sum: {total_sum}")


# 3. Write a program that uses a for loop to iterate through the list student_names = ["Ram", "Hari", "Sita"] and prints a personalized message for each student in the format 'Hi [Name], your course approval is ready!'. Include the header ' --- Email Greetings Generated ---' before the loop.
student_names = ["Ram", "Hari", "Sita"]
print("--- Email Greetings Generated ---")
for name in student_names:
    print(f"Hi {name}, your course approval is ready!")
    
# #   4. write a program that iterates through the list of chapter page counts [45, 30, 50, 40] and (starting the count at 1) to print a message for each chapter in the format: 'Chapter [Number] has [Pages] pages.'. Include the header '--- Book Chapter Summary ---'."  
chapter_page_counts = [45, 30, 50, 40]
print("--- Book Chapter Summary ---")
for i in range(len(chapter_page_counts)):
    print(f"Chapter {i + 1} has {chapter_page_counts[i]} pages.")
    


#5. Write a Python script to calculate the product (multiplication) of all numeric elements in a given list. given list=[4,5,3,2]
     
numbers = [4, 5, 3, 2]
product = 1
for num in numbers:
    product *= num
print(f"Product of all elements: {product}")    

#6. multiplication table of a given number. number= 11
number = 11
print(f"Multiplication Table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    
#7. reverse a list given list = [3,2,1,4,5]
my_list = [3, 2, 1, 4, 5]
reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])
print(f"Original list: {my_list}")
print(f"Reversed list: {reversed_list}")

#8.  You have two lists of numbers, and you need to find out which numbers appear in both lists. 
#Given two lists of numbers [1,2,3,4,5] and [3,4,5,6,7] write a for  loop to find the common elements.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []
for num in list1:
    if num in list2:
        common_elements.append(num)
print(f"Common elements: {common_elements}")

#9. Given list is lst=[1,2,3,4] but print 1 and 4 only 
lst = [1, 2, 3, 4]
print(f"First element: {lst[0]}")
print(f"Last element: {lst[-1]}")

#10.  Write a that removes all vowels (a, e, i, o, u) from a string.
input_string = "Hello, World!"
vowels = "aeiouAEIOU"
result_string = ""
for char in input_string:
    if char not in vowels:
        result_string += char
print(f"String without vowels: {result_string}")

# 11.  Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters. 
# given input: 
# 'Loops are Fun'
# expected Output:
# vowels: 5
# consonants: 7 
sentence = "Loops are Fun"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Vowel count: {vowel_count}")
print(f"Consonant count: {consonant_count}")

#12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.

lst = [1,2,3,4,5]
odd = []
even = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    
    else:
        odd.append(i)

print(f'odd: {odd}, even: {even}')

#13. Write a program to determine whether a given number is a prime number.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
        
#14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
mixed_list = [1, 2, 3, 4, "a", "b"]
integers = []
strings = []
for element in mixed_list:
    if isinstance(element, int):
        integers.append(element)
    elif isinstance(element, str):
        strings.append(element)
print(f"Integers: {integers}")
print(f"Strings: {strings}")

#15. Python program that accepts a string and calculate the number of digits and letters
input_string = input("Enter a string: ")
digit_count = 0
letter_count = 0
for char in input_string:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1
print(f"Digits: {digit_count}")
print(f"Letters: {letter_count}")

# 16. Python program to check the validity of username and password input by users
username = input("Enter username: ")
password = input("Enter password: ")
if len(username) >= 5 and len(password) >= 8:
    print("Username and password are valid.")
else:
    print("Invalid username or password. Username must be at least 5 characters and password must be at least 8 characters long.")
    
#17. program to print the given number is odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:    print(f"{number} is odd.")

#18. factorial of a given number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}.")

#19. Print multiplication table of  1,2,3,4,5,6,7,8 
for num in range(1, 9):
    print(f"Multiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()
    
#20. Given list is lst=[1,2,3,4] but print 1 and 2 only
lst = [1, 2, 3, 4]
print(f"First element: {lst[0]}")
print(f"Second element: {lst[1]}")
 
 #21. Python program to calculate the sum of all the odd numbers within the given range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
odd_sum = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        odd_sum += num
print(f"Sum of odd numbers: {odd_sum}")

#22. Python program to calculate the sum of all the even numbers within the given range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
even_sum = 0
for num in range(start, end + 1):
    if num % 2 == 0:
        even_sum += num
print(f"Sum of even numbers: {even_sum}")

#23. Python program to count the space of a given string
input_string = input("Enter a string: ")
space_count = 0
for char in input_string:
    if char == " ":
        space_count += 1
print(f"Number of spaces: {space_count}")

#24. given list is [1,2,3,4] but expected output is [1,8,27,64]
numbers = [1, 2, 3, 4]
cubed_numbers = []
for num in numbers:
    cubed_numbers.append(num ** 3)
print(f"Cubed numbers: {cubed_numbers}")

#25. reverse of a string a="programming". 
a = "programming"
reversed_string = ""
for char in a:
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")

#26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)

for num in range(50):
    if num > 7:
        break
    print(num)
    
#27. Write a for loop that iterates through a string and prints every letter.
input_string = "Hello, World!"
for char in input_string:
    print(char)
    
#28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
names = ["ram", "shyam", 1, 2]
for name in names:
    if isinstance(name, str):
        print(f"Hello! {name}")
        
#29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a = ["ram", "shyam", 1, 2]
prefixed_list = []
for item in a:
    prefixed_list.append(f"Dr.{item}")
print(f"Prefixed list: {prefixed_list}")

#30. Write a for loop which appends the square of each number to the new list.
numbers = [1, 2, 3, 4]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print(f"Squared numbers: {squared_numbers}")


#31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers = []
for num in lst1:
    if num > 0:
        positive_numbers.append(num)
print(f"Positive numbers: {positive_numbers}")

#32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
numbers = [0, 1, 2, 3, 4, 5, 6]
for num in numbers:
    if num == 3 or num == 6:
        continue
    print(num)
    
#33. Write a for loop which appends the type of each element in the first list to the second list.
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
types_list = []
for item in lst1:
    types_list.append(type(item))
print(f"Types of elements: {types_list}")

#34. Use else block to display a message “Done” after successful execution of for loop.
for num in range(5):
    print(num)
else:
    print("Done")
    
#35. Write a for loop statement to print the following series: 
#105 98 -------7
for num in range(105, 6, -7):
    print(num)
    
    
#36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
bad_chars = [';', ':', '!', "*"]
input_string = "py;th* o:n ! ;py * t*h:o !n"
cleaned_string = ""
for char in input_string:
    if char not in bad_chars:
        cleaned_string += char
print(f"Cleaned string: {cleaned_string}")
    
#37. Python program to count the number of even and odd numbers from a series of numbers.  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")

#38. Write a for loop to find the sum of all multiples of 3 or 5 below a given number range from 3 to 99.
total_sum = 0
for num in range(3, 100):
    if num % 3 == 0 or num % 5 == 0:
        total_sum += num
print(f"Sum of multiples of 3 or 5: {total_sum}")

#39. Write a for loop to find the sum of even and odd numbers separately in a range from 1 to 100. 

even_sum = 0
odd_sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

#40. Given a list of numbers, use a loop to count how many times a specific number appears. 
#list =[10, 20, 10, 30, 40, 50]
#target = 10
numbers = [10, 20, 10, 30, 40, 50]
target = 10
count = 0
for num in numbers:
    if num == target:
        count += 1
print(f"Number {target} appears {count} times in the list.")