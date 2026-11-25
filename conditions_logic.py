#Part א

#T1
# age = int(input('Enter an age: '))
# if age >= 18:
#     print('Adult')
# else:
#     print('Minor')

# #T2
# number = int(input('Enter a number: '))

# if number > 0:
#     print('Positive')
# elif number < 0:
#     print('Negative')
# else:
#     print('Zero ')

# #T3
# number = int(input('Enter a number: '))

# if number % 2 == 0:
#     print('Even ')
# else:
#     print('Odd')

# #T4
# number1 = int(input('Enter the first number: '))
# number2 = int(input('Enter the second number: '))

# if number1 == number2:
#     print('The numbers are equal.')
# elif number1 > number2:
#     print(number1)
# else:
#     print(number2)

# #T5
# password = "Python123"
# user_input = input('Enter the password: ')
# if user_input == password:
#     print('Access Granted')
# else:
#     print('Access Denied')

# #Part ב

# #T6
# number = int(input('Enter a number: '))

# if 1 <= number <=10:
#     print('Between 1 and 10.')
# elif  11 <= number <=50:
#     print('Between 11 and 50.')
# elif  51 <= number <=100:
#     print('Between 51 and 100.')
# else:
#     print('Number is out of the range of 1-100')

# #T7
# number = int(input('Enter a number: '))

# if 0 <= number <=59:
#     print('Failed')
# elif  60 <= number <=69:
#     print('Passed')
# elif  70 <= number <=79:
#     print('Good')
# elif  80 <= number <=89:
#     print('Very Good')
# elif  90 <= number <=100:
#     print('Excellent.')
# else:
#     print('Invalid')

# #T8
# correct_username = "admin"
# correct_password = "123456"
# entered_username = input('Enter your username: ')
# if entered_username != correct_username:
#     print('Unknown User')
# else:
#     entered_password = input('Enter your password: ')
#     if not correct_password== entered_password:
#         print('Wrong Password')
#     else:
#         print('Login Successful')

# #T9
# senior_discount_percent = 0.2
# youth_discount_percent = 0.1
# age = int(input('Enter your age: '))
# product_price = float(input('Enter the product price: '))
# if age > 60:
#     total_price = product_price - (product_price*senior_discount_percent)
# elif age <18:
#     total_price = product_price - (product_price*youth_discount_percent)
# else:
#     total_price = product_price
# print(f'{total_price}')

# #T10
# number = int(input('Enter a whole number: '))
# multiple_of_3:bool = number % 3 == 0 
# multiple_of_5:bool = number % 5 == 0 
# if multiple_of_3 and multiple_of_5:
#     print(f'{number} is a multiple of 3 and 5.')
# elif multiple_of_3:
#     print(f'{number} is a multiple of 3.')
# elif multiple_of_5:
#     print(f'{number} is a multiple of 5.')
# else:
#     print(f'{number} is NOT a multiple of either 3 or 5.')

#Part ג

#T11
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('Allowed')
# else:
#     accompanied_input = input('Enter True if he is accompanied else enter something else: ')
#     if accompanied_input == 'True':
#         accompanied:bool = True
#     else:
#         accompanied:bool = False
#     if not (age >= 16 and accompanied == True):
#         print('Not allowed in!')
#     else:
#         print('Allowed')

# #T12
# average = float(input('Enter your average: '))
# if average > 90:
#     print('You qualify for a scholarship!')
# else:
#     monthly_income = float(input('Enter your monthly income in shekels: '))
#     if monthly_income < 5000:
#         low_income:bool = True
#     else:
#         low_income = False
#     if not (low_income and average>85):
#         print('Not qualified for a scholarship!')
#     else:
#         print('You qualify for a scholarship!') 

#T13

# correct_username = "admin"
# correct_password = "123456"
# user_active = False
# entered_username = input('Enter your username: ')
# if entered_username != correct_username:
#     print('Unknown User, access denied!')
# else:
#     entered_password = input('Enter your password: ')
#     user_active_input = input('If your acount is active enter True, else enter anything else: ')
#     if user_active_input == 'True':
#         user_active = True
#     if not (correct_password== entered_password and user_active):
#         print('Access denied!')
#     else:
#         print('Access granted!')

#T14a
# number = int(input('Enter a number: '))
# valid_number = False
# # if number >= 20 and number <=80 :
# #     valid_number = True
# if not (number > 20 and number <=80):
#     valid_number = False
# else:
#     valid_number = True
# if valid_number:
#     print('Number in range')
# else:
#     print('Number out of range')

#Part ד

#T15
# balance = 5000
# withdrawal_amount = int(input(f'You  have {balance} amount of money in your acount.\nEnter the amount of money you want to withdraw: '))
# if not withdrawal_amount > 0 :
#     print('Error, you cannot withdraw a negative amount!') 
# else:
#     if not withdrawal_amount <= balance:
#         print('Error, you cannot withdraw more then you have in your acount!')
#     else:
#         print('Withdrawal approved!')
#         balance -= withdrawal_amount
#         print(f'Your remaining ballance is {balance}')

#T16
# membership_discount_percent = 0.1
# age = int(input('Enter your age: '))
# is_member = False
# membership_input = input('Enter True if you are a member, otherwise enter anything else: ')
# if membership_input == 'True':
#     is_member = True
# if age > 18:
#     ticket_price = 50 
# elif age <12:
#     ticket_price = 25 
# else:
#     ticket_price = 35 

# if not is_member:
#     total_price = ticket_price
# else:
#     total_price = ticket_price -(ticket_price*membership_discount_percent)
# print(f'{total_price}')

#T17
# age = int(input('Enter your age: '))
# if not age >= 21:
#     print('Ineligible for a loan, you are too young!')
# else:
#     monthly_salary = int(input('Enter your monthly salary: '))
#     if not monthly_salary >= 7000:
#         print('Ineligible for a loan, you are too poor!')
#     else:
#         work_seniority = float(input('Enter the number of years at your job: '))
#         if not work_seniority >= 1:
#             print('Ineligible for a loan, you job hop to much!')
#         else:
#             print('Your loan is approved!')

#T18

# hours = float(input('Enter the number of hours parked: '))
# vehicle_type = input ('Enter in the type of vehicle: ') 
# less_one_hour_discount_percent = 0.1
# five_hour_discount_percent = 0.15

# if vehicle_type == 'motorcycle':
#     price_per_hour = 10
# elif vehicle_type == 'car' :
#     price_per_hour = 20
# else:
#     price_per_hour = 35

# if not (hours<1 or hours>5):
#     total_price = price_per_hour*hours
# elif hours>5:
#     total_price = (price_per_hour*hours) -((price_per_hour*hours)*five_hour_discount_percent)
# else:
#     total_price = (price_per_hour*hours) -((price_per_hour*hours)*less_one_hour_discount_percent)
# print(f'{total_price}')

#Part ה

#T19
# number1 = int(input('Enter the first number: '))
# number2 = int(input('Enter the second number: '))
# operation_type = input('Enter one of the following operations to do between the 2 numbers:\n+ - * or /: ')
# if operation_type == '/':
#     if not number2 != 0:
#         print('You cannot divide by zero!')
#     else:
#         print(number1/number2)
# elif operation_type == '*':
#     print(number1/number2)
# elif operation_type == '+':
#     print(number1+number2)
# elif operation_type == '-':
#     print(number1-number2)
# else:
#     print('Error, you did not select a valid operation!')

#T20
# year = int(input('Enter the year you want to check: '))
# divisible_by_100 = year % 100 ==0
# divisible_by_4 = year % 4 ==0
# divisible_by_400 = year % 400 ==0
# if divisible_by_400:
#     leap_year_str = 'is'
# elif divisible_by_4 and not divisible_by_100:
#     leap_year_str = 'is'
# else:
#     leap_year_str = 'is not'
# print(f'{year} {leap_year_str} a leap year.')

#T21
# hours_worked = int(input('Enter the number of hours worked: '))
# base_hourly_pay = 50
# overtime_threshold = 182
# extreme_overtime_threshold = 2
# overtime = hours_worked > overtime_threshold
# overtime_bonus_less_2_hours = 1.25
# overtime_bonus_more_then_2_hours = 1.5
# if not overtime:
#     total_pay = hours_worked*base_hourly_pay
# else:
#     base_pay = base_hourly_pay*overtime_threshold
#     overtime_hours = hours_worked -overtime_threshold
#     if overtime_hours <= extreme_overtime_threshold:
#         overtime_pay = overtime_hours*base_hourly_pay*overtime_bonus_less_2_hours
#         total_pay = overtime_pay + base_pay
#     else:
#         early_overtime_pay = extreme_overtime_threshold*base_hourly_pay*overtime_bonus_less_2_hours
#         extreme_overtime_hours = overtime_hours - extreme_overtime_threshold
#         extreme_overtime_pay = extreme_overtime_hours*base_hourly_pay*overtime_bonus_more_then_2_hours
#         total_pay = base_pay+early_overtime_pay+extreme_overtime_pay
# print(total_pay)


#Part ו

#Refund System mini project
# member_return_threshold = 30
# regular_return_threshold = 14

# opened_input = input('Has the product been opened? Enter False if it is still closed and anything else if it was opened: ')
# if not opened_input == 'False':
#     print('Sorry, you cannot get a refund on opened products, have a nice day!')

# else:
#     has_receipt_input = input('Do you have a receipt? Enter True if you do and anything else if it not: ')
#     if not has_receipt_input == 'True':
#         print('Sorry, you cannot get a refund without a receipt, have a nice day!')
#     else:
#         purchase_amount = float(input('Enter the amount you purchased the product for: '))
#         if not purchase_amount > 0:
#             print('We can only refund a positive amount!')
#         else:
#             days_since_purchase = int(input('Enter how many days have passed since your purchase: '))
#             member_return_threshold = 30
#             regular_return_threshold = 14
#             if not days_since_purchase <= member_return_threshold:
#                 print('Sorry, too many days have passed since you bought our product.')
            
#             elif not (days_since_purchase < regular_return_threshold):
#                 membership_input = input('Are you part of our membership program? Enter True if you are and anything else if not: ')
#                 if not membership_input == 'True':
#                     print('Sorry, too many days have passed since you bought our product.')
#             else:
#                 customer_age = int(input('Enter the customers age: '))
#                 print(f'You are entitled to a refund of {purchase_amount}!\nYou are {customer_age} years old.')


           



    

        




    
