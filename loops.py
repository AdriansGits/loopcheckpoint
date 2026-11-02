# Name:Adrian
# Period:PM

# ============================================================
# Python Skills Check — LISTS & LOOPS
# CHALLENGE VERSION — 40 TASKS
# ============================================================
# DIRECTIONS:
# - Create a repository, clone it, and add this file.
# - Complete each task UNDER its directions.
# - Do not delete the directions.
# - Use ONLY concepts learned in class, except for 'in' and 'not in'.
#   You must research these two new operators independently in Section 5.
# - Use the EXACT variable and function names provided.
# - The entire file must run without errors.
# - Do not hard-code results Python should calculate.
# - Unless a task says otherwise, do NOT use sum(), min(), max(),
#   sorted(), sort(), list comprehensions, sets, or dictionaries.
# - For functions, RETURN values when instructed; do not just print.
# - Test edge cases and change the starting values to check your logic.
# - Tasks that ask for input() may be tested individually.

# ============================================================
# SECTION 1 — LIST FUNDAMENTALS (TASKS 1–6)
# ============================================================

# TASK 1:
# Create a list named scores containing 85, 92, 78, 96, 88.
# Print the entire list and its length using len().
scores = [85, 92, 78, 96, 88]
print(scores)
print(len(scores))
# TASK 2:
# Using scores from Task 1, print the FIRST, THIRD, and LAST
# elements on separate lines. Use indexes, not hard-coded values.
print(scores[0])
print(scores[2])
print(scores[4])
# TASK 3:
# Change the third element of scores to 100.
# Print the updated list. Do not create a replacement list.
scores[2] = 100
print(scores)
# TASK 4:
# Create games = ["Minecraft", "Roblox", "Fortnite"].
# Append "Valorant" and insert "Rocket League" at index 1.
# Print games. Check the order carefully.
create_games = ["Minecraft", "Roblox", "Fortnite"]
create_games.append("valorant")
create_games.insert(1, "Rocket League")
# TASK 5:
# Using games from Task 4, remove "Roblox" with remove().
# Then pop the FIRST item into a variable named removed_game.
# Print removed_game and the remaining games list.
create_games.remove("Roblox")
removed_game = create_games.pop(0)
print(removed_game)
print(create_games)
# TASK 6:
# Create colors = ["red", "blue", "green", "yellow", "purple"].
# Store the index of "green" in green_index using index().
# Print green_index. Then replace "yellow" with "orange".
# Print the new list.
create_colors = ["red", "blue", "green", "yellow", "purple"]
green_index = create_colors.index("green")
print(green_index)
create_colors[3] = "orange"
# ============================================================
# SECTION 2 — FOR LOOPS & RANGE (TASKS 7–12)
# ============================================================

# TASK 7:
# Use a for loop with range() to print numbers 1 through 20,
# INCLUDING 20. Do not manually print the numbers.

for i in range(1, 21):
    print(i)
# TASK 8:
# Use a for loop with range() to print 30, 27, 24, ... 0.
# IMPORTANT: The zero must be included.
for i in range(30, -1, -3):
    print(i)
# TASK 9:
# Use a for loop to print all EVEN numbers from 1 to 50.
# You MUST use an if statement and the % operator inside the loop.
for i in range(1,51):
    if i % 2 == 0:
        print(i)
# TASK 10:
# Create number = 7.
# Print its multiplication table from 1 through 12 using a for loop.
# Example line: 7 x 3 = 21
# Your code must also work if number changes.
number = 7
for i in range(1,13):
    print(number * int(i))
# TASK 11:
# Create students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"].
# Use a for loop to print "Student: " followed by each name.
# Do NOT write five separate print statements.
students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
for student in students:
    print("Students:" + student)
# TASK 12:
# Using students, print a NUMBERED roster:
# 1. Alex
# 2. Jordan
# ...
# 5. Casey
# Use range(len(students)) OR enumerate().
for i in range(len(students)):
    print(i + 1,  students[i])
# ============================================================
# SECTION 3 — WHILE LOOPS & VALIDATION (TASKS 13–18)
# ============================================================

# TASK 13:
# Create countdown = 10.
# Use a while loop to print from countdown down to 0.
# Then print "Blast off!". Avoid an infinite loop.
countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("Take Off")
# TASK 14:
# Create password = "Python123".
# Keep asking the user for a password until it matches.
# Print "Access granted" exactly once after a correct entry.
password = "Python123"
guess = ""
while guess != password:
    guess = input("Enter Password: ")
print("Access Greanted!")
# TASK 15:
# Ask the user for an integer between 1 and 10 INCLUSIVE.
# Keep asking while the value is invalid.
# After a valid entry, print "Valid number".
# Test 0, 1, 10, and 11.
user_input = 0
while user_input < 1 or user_input > 10:
    user_input = int(input("Enter an integer between 1 and 10 inclusive: "))
print("Valid number")
# TASK 16:
# Create total = 0.
# Repeatedly ask for an integer. Add each nonzero entry to total.
# Stop when the user enters 0, then print total.
# Example inputs: 5, 8, -2, 0 -> Total: 11.
total = 0
user_input = int(input("Enter an integer (0 to stop): "))
while user_input != 0:
    total += user_input
    user_input = int(input("Enter an integer (0 to stop): "))
print("Total: ", total)
# TASK 17:
# Create secret = "robot" and attempts = 3.
# Ask the user to guess secret, allowing AT MOST 3 guesses.
# Print "Correct" if guessed in time; otherwise "Out of attempts".
# Make sure a correct guess does NOT print both messages.
secret = "robot"
attempts = 3
guess = 0
while attempts > 0 and guess != secret:
    guess = input("Guess the secret word: ")
    attempts -= 1
if guess == secret:
    print("Correct")
else:
    print("Out of attempts")
# TASK 18:
# Make a while-loop menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit
# Repeat until the user enters 3. Handle invalid choices.
# Print "Goodbye" only when option 2 is selected.
choice = 0
while choice != "3":
    print("--- Menu ---")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
# ============================================================
# SECTION 4 — PROCESSING LISTS WITH LOOPS (TASKS 19–24)
# ============================================================
# TASK 19:
# Create numbers = [4, 8, 15, 16, 23, 42].
# Use a for loop to calculate and print their total.
# Do NOT use sum().
numbers = [4, 8, 15, 16, 23, 42]
total = 0
for num in numbers:
    total += num
print("The total is:", total)
# TASK 20:
# Create grades = [90, 85, 78, 92, 88].
# Use a loop and len() to calculate the average.
# Print the average. Do NOT use sum().
grades = [90, 85, 78, 92, 88]
total = 0
for grade in grades:
    total += grade
average = total / len(grades)
print("The average grade is:", average)
# TASK 21:
# Create numbers = [3, 8, 12, 7, 15, 20, 24, 9].
# Use ONE loop to count even and odd values separately.
# Print "Even: [count]" and "Odd: [count]".
numbers = [3, 8, 12, 7, 15, 20, 24, 9]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(str("Even:") + even_count)
print(str("Odd:") + odd_count)
# TASK 22:
# Create numbers = [-14, -67, -23, -89, -45].
# Use a loop to find and print the HIGHEST number.
# Do NOT use max() or sorting.
# IMPORTANT: Starting your answer at 0 gives a wrong result.
numbers = [-14, -67, -23, -89, -45]
max_num = numbers[0]
for i in numbers:
    if i > max_num:
        max_num = i
print(max_num)
# TASK 23:
# Create numbers = [14, 67, 23, 89, 45, 12].
# Use a loop to find and print the LOWEST number.
# Do NOT use min() or sorting.
# Your logic must also work with all-negative numbers.
numbers = [14, 67, 23, 89, 45, 12]
min_num = numbers[0]
for i in numbers:
    if i < min_num:
        min_num = i
print(min_num)
# TASK 24:
# Create numbers = [5, 2, 5, 8, 5, 3, 2, 5].
# Create target = 5.
# Use a loop to count how often target appears; print the count.
# Do NOT use count(). It must work if target changes.
numbers = [5, 2, 5, 8, 5, 3, 2, 5]
target = 5
count = 0
for i in numbers:
    if i == target:
        count += 1
print(count)
# ============================================================
# SECTION 5 — IN / NOT IN (TASKS 25–30)
# ============================================================
# INDEPENDENT RESEARCH REQUIRED:
# We have NOT covered 'in' and 'not in' in class. Before starting
# Tasks 25–30, research both operators on your own using reliable
# Python learning resources or the official Python documentation.
# Learn what each operator does, how it works with lists, and how
# to use it inside if statements and while loops.
# Write a short comment in your code explaining the difference
# between 'in' and 'not in' in your own words.
# The examples below are starting hints, NOT a substitute for research.
#
# NEW CONCEPT:
# 'in' checks whether a value is in a list.
# Example: "apple" in ["apple", "banana"] evaluates to True.
# 'not in' checks whether a value is missing.
# Example: "grape" not in ["apple", "banana"] evaluates to True.
# These expressions are useful in if statements and while loops.

# TASK 25:
# Create foods = ["pizza", "burger", "tacos", "sushi", "pasta"].
# Ask the user to enter a food.
# Use 'in' to print "Available" or "Not available".
# Do NOT use index() to search.
foods = ["pizza", "burger", "tacos", "sushi", "pasta"]
food = input("Enter a food: ")
if food in foods:
    print("Available")
else:
    print("Not available")
# TASK 26:
# Create supplies = ["pencil", "notebook", "eraser", "backpack"].
# Ask the user for an item.
# Use 'not in' to print "Need to buy" if it is missing,
# otherwise print "Already have it".
supplies = ["pencil", "notebook", "eraser", "backpack"]
item = input("Enter a stationary item: ")
if item in supplies:
    print("Already have it")
else:
    print("Need to buy")
# TASK 27:
# Create usernames = ["alex123", "gamer99", "pythonpro"].
# Ask the user to enter a new username.
# If it is already in the list, print "Username taken".
# Otherwise append it and print the updated list.
# Do not allow duplicates.
usernames = ["alex123", "gamer99", "pythonpro"]
username = input("Enter a username: ")
if username in usernames:
    print("Username taken")
else:
    usernames.append(username)
    print(usernames)
# TASK 28:
# Modify the idea from Task 27 using a NEW list named accounts.
# Start with accounts = ["admin", "guest"].
# Use a while loop to keep asking until the entered name
# is NOT in accounts. Append the accepted name and print accounts.
# REQUIREMENT: Use 'not in' in your solution.
accounts = ["admin", "guest"]
account_name = input("Enter an account name: ")
while account_name in accounts:
    print("Name taken")
    account_name = input("Enter a different account name: ")
accounts.append(account_name)
print(accounts)
# TASK 29:
# Create secret_words = ["dragon", "robot", "python", "galaxy"].
# Keep asking the user for a word UNTIL it is in secret_words.
# Count and print the number of guesses made.
# A correct first guess should count as 1.
secret_words = ["dragon", "robot", "python", "galaxy"]
guess = input("Enter your guess for the secret word: ")
count = 1
while guess not in secret_words:
    print("Incorrect guess")
    count += 1
    guess = input("Try again: ")
print("You guessed a secret word!")
print("Number of tries:", count)
# TASK 30:
# Create guests = [].
# Ask the user to enter EXACTLY FIVE UNIQUE guest names.
# If a name is already in guests, reject it and ask again.
# Use a while loop, 'in' or 'not in', and append().
# Print the finished list and its length.
print("Input five guests")
guests = []
length = len(guests)
name = ""
while len(guests) < 5:
    name = input("Enter a name: ")
    while name in guests:
        print("That name is already in the guest list")
        name = input("Enter a name: ")
    guests.append(name)
print(guests)
print("Number of guests:", len(guests))
# ============================================================
# SECTION 6 — LISTS + FUNCTIONS (TASKS 31–35)
# ============================================================

# TASK 31:
# Create a function named count_positive(numbers).
# RETURN how many elements are greater than 0.
# Do NOT use count().
# Test: count_positive([-2, 0, 4, 9, -1]) -> 2
def count_positive(numbers):
    count = 0
    for i in numbers:
        if i > 0:
            count += 1
    print(count)
count_positive([-2, 0, 4, 9, -1])
# TASK 32:
# Create a function named find_item(items, target).
# RETURN the index of the FIRST matching item, or -1 if missing.
# Do NOT use index().
# Test: find_item(["cat", "dog", "cat"], "cat") -> 0
# Test: find_item(["cat", "dog"], "fish") -> -1
def find_item(items, target):
    if target in items:
        return items.index(target)
    else:
        return -1
print(find_item(["cat", "dog", "cat"], "cat"))
print(find_item(["cat", "dog"], "fish"))
# TASK 33:
# Create a function named unique_items(items).
# RETURN a NEW list without duplicate values, preserving first
# appearance order. REQUIREMENT: Use 'not in'.
# Test: unique_items([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
def unique_items(items):
    unique_items = []
    for i in items:
        if i not in unique_items:
            unique_items.append(i)
    print(unique_items)
unique_items([1, 2, 2, 3, 1, 4])
# TASK 34:
# Create a function named common_items(list1, list2).
# RETURN a NEW list of values found in BOTH lists.
# Include each matching value only once, in list1's order.
# REQUIREMENT: Use both 'in' and 'not in'.
# Test: common_items([1, 2, 3, 3], [3, 4, 1]) -> [1, 3]
def common_items(list1, list2):
    combined_list = []
    for i in list1:
        if i in list2:
            if i not in combined_list:
                combined_list.append(i)
    print(combined_list)
common_items([1, 2, 3, 3], [3, 4, 1])
# TASK 35:
# Create a function named reverse_list(items).
# RETURN a NEW list in reverse order, without changing items.
# Do NOT use reverse(), reversed(), or [::-1].
# Test: reverse_list([10, 20, 30]) -> [30, 20, 10]
def reverse_list(items):
    reversed = []
    for i in items:
        reversed.insert(0, i)
    print(reversed)
reverse_list([10, 20, 30])
# ============================================================
# SECTION 7 — DEBUGGING (TASKS 36–37)
# ============================================================

# TASK 36:
# Fix this code so it prints 1, 2, 3, 4, 5 exactly once each.
# Explain in a comment what was wrong.
#
# number = 1
# while number <= 5:
#     print(number)
#
# Do NOT replace the while loop with a for loop.
number = 1
while number <= 5:
    print(number)
    number += 1
# TASK 37:
# Fix this code so it removes ALL 4s without skipping any.
# Explain in a comment why the original approach can fail.
#
# values = [4, 4, 7, 4, 9]
# for value in values:
#     if value == 4:
#         values.remove(value)
# print(values)
#
# Expected: [7, 9]
# HINT: A while loop and 'in' can help.
values = [4, 4, 7, 4, 9]
for value in values:
    while 4 in values:
        values.remove(value)
print(values)
# ============================================================
# FINAL BOSS CHALLENGES (TASKS 38–40)
# ============================================================

# TASK 38 — SHOPPING LIST MANAGER:
# Build a menu-driven program with:
# 1. Add item
# 2. Remove item
# 3. View numbered items
# 4. Search for item
# 5. Exit
# Start with shopping_list = [].
# REQUIREMENTS:
# - Use a while loop for the menu and a for loop to display items.
# - Use 'in' to prevent duplicates and 'not in' to reject missing items.
# - Handle an empty list and invalid menu selections.
# - Keep running until the user chooses Exit.
products = ["chips", "soda", "candy", "cookies", "water", "sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]
shopping_cart = []
selection = 0
def display_items():
   print("=====Avalible Products=====")
   for i in range(len(products)):
      print(str(i + 1) + "." + str(products[i]) + " -- $" + format(prices[i]))
print()
def add_item():
    display_items()
    try:
        item_num = int(input("Enter the product number to add: "))
        if 1 <= item_num <= len(products):
            chosen_product = products[item_num - 1]
            chosen_price = prices[item_num - 1]
            shopping_cart.append(chosen_product)
            print("Added " + str(chosen_product) + " to your cart!")
        else:
            print("Invalid product number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_item():
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
        return

    print("========== YOUR SHOPPING CART ==========")
    for i in range(len(shopping_cart)):
        print(str(i + 1) + ". " + str(shopping_cart[i]))
    print()
    
    
    while True:
        try:
            item_num = int(input("Which item would you like to remove?\nEnter item number: "))
            if 1 <= item_num <= len(shopping_cart):
                removed = shopping_cart.pop(item_num - 1)
                print( str(removed) + " was removed from your cart!")
                break
            else:
                print("Invalid item number! Please choose a number between 1 and " + str(len(shopping_cart)) + ".")
        except ValueError:
            print("Invalid input! Please enter a number.")
    

def view_cart():
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
        return

    print("========= YOUR SHOPPING CART ==========")
    for i in range(len(shopping_cart)):
        item_name = shopping_cart[i]
        print(item_name)
        prod_index = products.index(item_name)
        item_price = prices[prod_index]
        print(str(i + 1) + ". " + str(item_name) + "$" + format(item_price))
    
    print("Total Items: " + str(len(shopping_cart)))
    
def view_total():
    if len(shopping_cart) == 0:
        print("========== CURRENT TOTAL ==========")
        print("Subtotal:$0.00")
        return

    print("========== CURRENT TOTAL ==========")
    subtotal = 0.0
    for i in range(len(shopping_cart)):
        item_name = shopping_cart[i]
        prod_index = products.index(item_name)
        item_price = prices[prod_index]
        print(str(item_name) + "$" + format(item_price))
        subtotal += item_price 
        
    print("Subtotal:" + "$" + format(subtotal) + "")

def checkout():
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty! You cannot checkout.")
        return False 
    subtotal = 0.0
    for i in range(len(shopping_cart)):
        item_name = shopping_cart[i]
        prod_index = products.index(item_name)
        subtotal += prices[prod_index]

    
    if subtotal < 10.0:
        discount_percent = 0
        discount_text = "No discount"
    elif subtotal < 20.0:
        discount_percent = 5
        discount_text = "5%"
    elif subtotal < 40.0:
        discount_percent = 10
        discount_text = "10%"
    else:
        discount_percent = 15
        discount_text = "15%"

    amount_saved = subtotal * (discount_percent / 100.0)
    final_total = subtotal - amount_saved

    print("========== CHECKOUT ==========")
    print("Subtotal:" + format(subtotal))
    print("Discount:" + discount_text)
    print("Amount Saved:" + format(amount_saved))
    print("Final Total:" + format(final_total))
    print("Thank you for shopping!")
    return True
    

print("========== SMART SHOPPING CART ==========")
print("")
print("1. View Available Products")
print("2. Add Product to Cart")
print("3. Remove Product from Cart")
print("4. View Shopping Cart")
print("5. View Current Total")
print("6. Checkout")
ready_to_shop = input("Ready to shop? (yes/no)")
def they_are_ready(theanswer):
    while theanswer != "yes":
        theanswer = input("How about now?")

    return theanswer
ready_to_shop = they_are_ready(ready_to_shop)

while ready_to_shop == "yes" and selection != 6:
    print("========== SMART SHOPPING CART ==========")
    print("")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    selection = int(input("Enter your choice (1-6): "))
    if selection == 1:
        display_items()
    elif selection == 2:
        add_item()
    elif selection == 3:
        remove_item()
    elif selection == 4:
        view_cart()
    elif selection == 5:
        view_total()
    elif selection == 6:
        checkout_successful = checkout()
        if not checkout_successful:
            selection = 0 
    else:
        print("Invalid selection. Please choose a number from 1 to 6.")
# TASK 39 — GRADE ANALYZER:
# Create a function named analyze_grades(grades).
# RETURN a list containing, IN THIS ORDER:
# [highest_grade, lowest_grade, average_grade, passing_count, failing_count]
# Passing means 70 or higher.
# Do NOT use sum(), min(), max(), or sorting.
# For an empty list, RETURN [].
# Test: analyze_grades([95, 82, 67, 74, 58])
# Expected: [95, 58, 75.2, 3, 2]
# Test with a single grade and all-negative values too.
def analyze_grades(grades):
    new_grades = []
    highest_grade = 0
    lowest_grade = 0
    avg_grade = 0
    passing_count = 0
    failing_count = 0

    if len(grades) == 0:
        return new_grades
    for i in grades:
        if i > highest_grade:
            highest_grade = i
        if i < lowest_grade and i >= 0:
            lowest_grade = i
        avg_grade += i
        if i >= 70:
            passing_count += 1
        else:
            failing_count += 1

    if avg_grade >= 0:    
        avg_grade = avg_grade / len(grades)
    else:
        avg_grade = 0

    new_grades.append(highest_grade)
    new_grades.append(lowest_grade)
    new_grades.append(avg_grade)
    new_grades.append(passing_count)
    new_grades.append(failing_count)

    return new_grades
print(analyze_grades([95, 82, 67, 74, 58]))
print(analyze_grades([]))
print(analyze_grades([67]))
print(analyze_grades([-95, -82, -67, -74, -58]))
# TASK 40 — STUDENT ATTENDANCE SYSTEM:
# Start with:
# students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# present = []
# absent = []
# For EACH student, ask whether they are Present (P) or Absent (A).
# REQUIREMENTS:
# - Use a for loop to process the student list.
# - Use a while loop to reject anything other than P or A.
# - Prevent duplicate attendance records using 'in' / 'not in'.
# - Print numbered present and absent lists.
# - Print the number present, number absent, and attendance percentage.
# - Print "Perfect Attendance!" if everyone is present.
# - Create attendance_percentage(present, students) that RETURNS
#   the percentage; if students is empty, RETURN 0.
# - Test with all present, all absent, and a mixture.
students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
present = []
absent = []
for i in students:
    print()
    print(i)
    if i not in absent and i not in present:
        attendance = input("Is this student absent or present (P/A): ")

        while attendance != "P" and attendance != "A":
            print()
            print("Invalid option!")
            attendance = input("Is this student absent or present: ")

        if attendance == "P":
            present.append(i)
        else:
            absent.append(i)
print()
print("PRESENT:")
for i in range(len(present)):
    print(str(i + 1) + ".", present[i])
print("Number present:", len(present))
print()
print("ABSENT:")
for i in range(len(absent)):
    print(str(i + 1) + ".", absent[i])
print("Number absent:", len(absent))
print()
def attendance_percentage(present, students):
    if len(students) > 0:
        return (len(present) / len(students)) * 100
    else:
        return 0
percentage = attendance_percentage(present, students)
print("Attendance percentage: " + str(round(percentage)) + "%")
if percentage == 100:
    print("Perfect Attendance!")
print()
# ============================================================
# END OF CHECKPOINT — REVIEW YOUR WORK BEFORE PUSHING
# ============================================================
