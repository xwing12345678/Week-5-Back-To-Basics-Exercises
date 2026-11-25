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
