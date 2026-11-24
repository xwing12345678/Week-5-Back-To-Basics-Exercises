#Part א

#T1
# first_name:str = "Yisrael Meir"
# last_name:str = "Sobel"
# age:int = 30
# city:str = "Karmiel"
# email:str = 'yisraelmeirsobel@gmail.com'
# print(f'''===== User Details =====
# First Name: {first_name}
# Last Name: {last_name}
# Age: {age}
# City: {city}
# Email: {email}
# ========================
# ''')

#T2

# birth_year:int  = 1996
# current_year:int = 2026
# age:int = current_year - birth_year
# print(f'You are approximately {age} years old.')

#T3
# width:int = 4
# height:int = 2
# rectangle_area:int = width * height
# rectangle_perimeter = 2*(width + height)
# print(f'The rectangle area is {width} x {height} = {rectangle_area}')
# print(f'The rectangle perimeter is 2 x ({width}+{height}) = {rectangle_perimeter}')

#T4
# name:str = "David"
# age:int = 25
# height:float = 1.78
# is_student:bool = True
# salary:int = 8500
# print(f'name has the value {name} and the type {type(name)} ')
# print(f'age has the value {age} and the type {type(age)} ')
# print(f'height has the value {height} and the type {type(height)} ')
# print(f'name has the value {is_student} and the type {type(is_student)} ')
# print(f'salary has the value {salary} and the type {type(salary)} ')

#Part2

#T5

# first_name:str = input("Enter your first_name: ")
# last_name:str = input("Enter your last_name: ")
# age:int = int( input("Enter your age: "))
# city:str =  input("Enter your city: ")
# print(f'''Welcome  {first_name} {last_name}!
# You are {age} years old and live in {city}.
# ''')

#T6
# number_1:int = int(input('Enter the first number: '))
# number_2:int = int(input('Enter the second number: '))
# print(f'{number_1} + {number_2} = {number_1+number_2}')
# print(f'{number_1} - {number_2} = {number_1-number_2}')
# print(f'{number_1} x {number_2} = {number_1*number_2}')
# print(f'{number_1} / {number_2} = {number_1/number_2}')

#T7
# product_name = input('Enter the product name: ')
# product_price = int(input('Enter the product price: '))
# quantity = int(input('Enter the quantity of products: '))
# print(f'''====== Purchase Receipt ======
# Product: {product_name}
# Price: {product_price}
# Quantity: {quantity}
# Total: {quantity * product_price}
# ==============================
# ''')

#Part ג

#T8

# employee_name:str = input('Enter employee name: ')
# hours_per_month = int(input('Enter the hours per month: '))
# hourly_rate = int(input('Enter the hourly rate: '))
# print(f'''====== Employee Salary Report ======
# Name: {employee_name}
# Hours per month: {hours_per_month}
# Rate: {hourly_rate}
# Monthly Salary: {hourly_rate*hours_per_month}
# ==============================
# ''')

#T9
# bill = float(input('Enter the bill for your meal: '))
# tip_percent = float(input('Enter the tip percentage you want to tip the servers: '))
# dinners = int(input('Enter the number of diners who will be splitting the bill: '))
# tip_amount = tip_percent*bill
# total = bill + tip_amount
# amount_per_person = total/dinners
# print(f'The tip size is {tip_amount}.')
# print(f'The total to be paid is {total}')
# print(f'Each person must pay {amount_per_person}')

#T10
# a = 10
# b = 20
# c = a
# a = b
# b = c
# print(f'a = {a}')
# print(f'b = {b}')

#Part ד

#תרגיל סיכום 

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))
institution =  input('Enter the institution you are registering to: ')
course = ('Enter the course you are registering to: ')
duration = int(input('Enter the amount of months you will be learning the course: '))
monthly_price = int(input('Enter the amount of tuition you will be paying every month: '))
total_course_price = monthly_price * duration

print(f'''
================================
       STUDENT REGISTRATION
================================

Student: {first_name} {last_name}
Age: {age}
Institution: {institution}
Course: {course}
Duration: {duration}
Monthly Price: {monthly_price}

Total Course Price: {total_course_price}

================================
Registration completed!
================================
''')