# 1 Create a Python program that prompts the user to enter their age. If the age is less
# than 18, print you are a minor. If the age is between 18 and 60, print you are an
# adult. For ages over 60, print you are a senior citizen. The program should continue
# until the user inputs stop.

while True:
    age = input("Enter your age: ")

    if int(age) < 18:
        print("You are a minor.")
    
    elif int(age) < 60:
        print("You are an adult.")

    elif int(age) > 60:
        print("You are a senior citizen.")
    
    elif age.lower() == 'stop':
        break

# 2 Write a Python program that simulates waiting for a specific vehicle, such as a bus.
# The program should repeatedly prompt the user to input the name of a vehicle. If the
# input is not bus, the program should print waiting and continue. Once the user inputs
# bus, the program should print finally the wait is over and terminate the loop.

while True:
    vehicle = input("Enter the name of the vehicle: ")

    if vehicle.lower() == 'bus':
        print("Finally, the wait is over!")
        break

    else:
        print("Waiting...")

# 3 Generate a frequency table for the ratings list which is initialized below. Ratings =
# ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']

ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']

content_ratings = {}
i = 0


while i < len(ratings):
    if ratings[i] in content_ratings:
        content_ratings[ratings[i]] += 1
        i += 1
    
    else:
        content_ratings[ratings[i]] = 1
        i += 1


print(content_ratings)

#4. Write a Python program that generates a random number between 1 and 10 and
#prompts the user to guess the number. The program should provide hints such as
#guess higher or guess lower based on the user's input. Once the user guesses the
#correct number, the program should display the number of attempts it took to guess
#the correct number

secret_number = random.randint(1, 10)

attempts = 0

print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Guess higher!")
    elif guess > secret_number:
        print("Guess lower!")
    else:
        print("Congratulations! You guessed the correct number.")
        print("Number of attempts:", attempts)
        break

# 5. Write a Python program that simulates a login system. The program should prompt
# the user to enter a username and password. If both are correct for example username
# is admin and password is 1234, print Login successful and exit. If either is incorrect,
# print Invalid credentials, try again. Allow the user up to 3 attempts before locking
# them out with the message too many failed attempts.

username = 'admin'
password = '1234'
attempts = 3

while attempts > 0:
    u_user = input("Enter your username: ")
    u_pass = input("Enter your password: ")

    if u_user == username and u_pass == password:
        print("Login Successful!")
        break

    else:
        attempts -= 1
        print(f"Invalid Credentials! You have {attempts} remaining.")

else:
    print("Too many failed attempts!")

# 6. Write a Python program that simulates a basic arithmetic quiz. Generate two random
# numbers between 1 and 30 and ask the user to provide the result of their
# multiplication. If the answer is correct, print correct and generate a new question. If
# the answer is wrong, print Incorrect, try again. Allow the user to stop the quiz when
# the user enters exit.

import random
marks = 0

print("Welcome to the Quiz, you can stop anytime if you enter 'exit'")

while True:
    num1 = random.randrange(1, 30)
    num2 = random.randrange(1, 30)
    guess = input(f"Enter the product of {num1} and {num2}: ")

    if guess.lower() == 'exit':
        print(f"You got {marks} marks!")
        break

    elif int(guess) != (num1 * num2):
        print("Incorrect Guess!")
    
    elif int(guess) == (num1 * num2):
        print("Correct Guess!")
        marks += 1


# 7.  Write a Python program that prompts the user to repeatedly enter a name. If the user
# enters the phrase good luck, the program keeps track of how many times the phrase
# has been entered. When the phrase has been entered three times, the program should
# display a message stating you typed good luck three times. For each entry of good
# luck before the third occurrence, display the message you typed the same word
# [count] times. Continue this process until the phrase has been entered three times

lst = []
count = 0

while count < 3:
    u_input = input("Enter a name: ")

    if u_input in lst:
        lst.append(u_input)
        count = lst.count(u_input)
        print(f"You typed the same word {count} times.")

    elif u_input not in lst:
        lst.append(u_input)
    

# 8. Generate a random number (1–50). Give the user up to 7 attempts to guess it using a
# while loop. Track remaining attempts and stop early if they guess correctly or run out
# of tries

import random

num = random.randrange(1, 50)
attempts = 0

while attempts < 7:
   guess =  int(input("Guess the number between 1-50: "))

   if guess != num:
     print("Try again")
     attempts += 1

   elif guess == num:
      print("Correct Guess")

else:
   print("You ran out of attempts!")



# Write a Python program that simulates a basic elevator system. The program should
# keep track of the elevator's current position and allow a user to travel to different
# floors until they choose to exit.


current_floor = 1

while True:
    target_floor = input("Enter the floor number: ")

    if target_floor == '0':
        print("Goodbye!")
        break

    elif not target_floor.isnumeric():
        print("Invalid Floor Number!")

    elif int(target_floor) > current_floor:
        print("Going up")
        current_floor = int(target_floor)

    elif int(target_floor) < current_floor:
        print("Going down")
        current_floor = int(target_floor)
   

    else:
        print("You are already on the floor")

# 10. Develop a two-player Rock, Paper, Scissors game. The program should automate the
# scoring logic and continue the match until one player reaches a specific score.

player1_score = 0
player2_score = 0

while True:
    player1_choice = input("Player 1, enter your choice, Rock, paper or scissors: ").lower()
    player2_choice = input("Player 2, enter your choice, Rock, paper or scissors: ").lower()

    if player1_choice == player2_choice:
        print("It's a tie!")

    elif player1_choice == 'rock':
        if player2_choice == 'paper':
            player1_score += 1
        else:
            player2_score += 1

    elif player1_choice == 'paper':
        if player2_choice == 'scissors':
            player1_score += 1
        else:
            player2_score += 1

    elif player1_choice == 'scissors':
        if player2_choice == 'rock':
            player1_score += 1
        else:
            player2_score += 1

    print(f"Player 1's score: {player1_score}")
    print(f"Player 2's score: {player2_score}")

    if player1_score == 5:
        print("Player 1 won the game!")
        break

    elif player2_score == 5:
        print("Player 2 won the game!")
        break
    

# 11. Write a python program to get the following output using while loop.
# 1 – 49
# 2 – 48
# 3 – 47
# 4 – 46
# .
# .
# .
# 48 – 2
# 49 –1

i = 1
while i <= 49:
    print(f"{i} - {50 - i}")
    i += 1

# 12. Write a program that accepts a number from the user and calculates the sum of all
# numbers from 1 up to that number.

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    sum += i
print(f"The sum of all numbers from 1 to {num} is {sum}")

# 13.  Print alphabet series A to Z.
# Output: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

i = 65
while i <= 90:
    print(chr(i), end=" ")
    i += 1

# 14. Write a program to find the numbers which are below 20 in a list using while loop.
# number = [2, 40, 21, 31, 10, 7, 5]

number = [2, 40, 21, 31, 10, 7, 5]
i = 0

while i < len(number):
    if number[i] < 20:
        print(number[i], end = " ")
    i += 1