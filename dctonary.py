1. Create a dictionary mapping students names to email addresses.
student_record = {'rajiv': 'rajiv@example.com',
                  'subin': 'subin@example.com'}

name = input("Enter student name: ")

if name in student_record:
    print("Email address:", student_record[name])
else:
    print("Student not found.")


#2. Shopping list and bought items using sets.
shopping_list = {"Milk", "Bread", "Eggs", "Butter"}
bought = {"Bread", "Eggs"}

missing_items = shopping_list - bought

if missing_items:
    print("Missing items:", missing_items)
else:
    print("Shopping complete.")


#3. Add a new student if not already present.
class_list = {"ram", "sita", "laxman"}

new_student = input("Enter the name of the new student: ")

if new_student not in class_list:
    class_list.add(new_student)
    print("Student added successfully.")
else:
    print("Student already present.")

print("Updated class list:", class_list)


#4. Count Blue votes.
votes = ["Blue", "Red", "Blue", "Green", "Blue", "Red"]

blue_count = votes.count("Blue")

if blue_count >= 3:
    print("Blue wins.")
else:
    print("Blue did not win.")


#5. Check student grades from dictionary.
grades = {"ram": 95, "sita": 88}

student_name = input("Enter the student's name: ")

if student_name in grades:
    print(f"{student_name}'s grade: {grades[student_name]}")
else:
    print("Grade not available.")


#6. Applicant qualification check.
applicant = {
    "name": "Priya",
    "skills": ["sql", "Java", "Python"],
    "experience_years": 3
}

required_skills = {"Python", "Java"}

if required_skills.intersection(applicant["skills"]) and applicant["experience_years"] >= 2:
    print("Priya qualifies.")
else:
    print("Priya does not qualify.")


#7. Airline baggage check.
banned_items = {"scissors", "knife", "lighter"}

baggage_weight = float(input("Enter baggage weight in kg: "))
item = input("Enter the name of the item: ").lower()

if baggage_weight <= 7 and item not in banned_items:
    print("Bag allowed.")
else:
    print("Bag not allowed.")


#8. Change Shyam salary to 8500.
sample_dict = {
    'emp1': {'name': 'john', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'shyam', 'salary': 5500}
}

sample_dict['emp3']['salary'] = 8500

print(sample_dict)


#9. Compare Ram and Laxman items.
ram_items = {"apple", "banana", "orange", "mango"}
laxman_items = {"grape", "melon", "orange"}

common_items = ram_items.intersection(laxman_items)

if common_items:
    print("They have some common items:", common_items)
else:
    print("They picked completely different items.")


#10. Access token validation.
my_list = [10, 20, 30, 40]
my_tuple = (10, 20, 30, 50)
my_set = {30, 40}
my_dict = {'a': 10, 'b': 20}

val = 20

if val in my_list and val in my_tuple:

    if 'b' in my_dict and val not in my_set:
        print("Path A")

    else:
        print("Path B")

else:
    print("Path C")


#11. Duplicate dictionary keys.
data = {'a': 10, 'b': 20, 'a': 30}

print(data)

# Output: {'a': 30, 'b': 20}


#12. Invalid dictionary key.
# [1,2,3] cannot be used as a dictionary key because lists are mutable.


#13. Dictionary get() example.
d = {'val': 10}

if d.get('score'):
    print("Found")
else:
    print("Not Found")


#14. Length of set.
items = [10, 10, 20, 30]

print(len(set(items)))

# Output: 3


#15. Add item to set.
my_set = {10, 20, 30}

my_set.add(40)

print(my_set)


#16. Restaurant menu dictionary.
menu = {'Pizza': 18, 'Burger': 12, 'Salad': 9}

order = 'Pizza'

if order in menu:
    print(f"The price of {order} is ${menu[order]}.")
else:
    print("Item not found.")


#17. Student result status.
student_data = {'name': 'sam', 'score': 90}

if student_data['score'] >= 80:
    student_data['status'] = 'Pass'
else:
    student_data['status'] = 'Review'

print(student_data)


#18. Login system.
database = {"admin": "1234", "user1": "abcd"}

input_user = "admin"
input_pass = "1234"

if input_user in database and database[input_user] == input_pass:
    print("Login Successful")
else:
    print("Login Failed")


#19. Email blacklist checker.
emails = ["ram123@test.com", "hari77@test.com", "sita55@test.com"]

blacklisted = {"hari77@test.com"}

current_email = "sita55@test.com"

if current_email in emails and current_email not in blacklisted:
    print("Email Sent")
else:
    print("Blocked")


#20. Inventory check.
inventory = {'A1': 50, 'B2': 5, 'C3': 10}

restricted_zones = {'Z9'}

target = 'B2'

if target in inventory:

    if target not in restricted_zones and inventory[target] > 0:
        print("Dispatch item.")
    else:
        print("Stock error.")

else:
    print("Invalid zone.")


#21. Student enrollment system.
valid_courses = {"python", "robotics", "java"}

hs_grades = [9, 10, 11, 12]

student_records = {}

name = input("Enter student's name: ")
course = input("Enter course: ")
grade = int(input("Enter grade (9-12): "))

student_records[name] = {
    'course': course,
    'grade': grade
}

if course not in valid_courses:
    print(f"{name} selected an invalid course.")

elif grade < 9:
    print("Grade too low.")

elif grade > 12:
    print("Grade too high.")

else:
    if course == "robotics" and grade == 9:
        print(f"{name} is not eligible for {course} grade too low.")
    else:
        print(f"{name} is approved for {course}.")
