#Part א

#T1

# num1 = 25
# num2 = 7

# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1//num2)
# print(num1%num2)
# print(num1**num2)

# #T2
# balance = 1000
# print(f'balance = {balance}')
# balance += 250
# print(f'balance = {balance}')

# balance -= 100
# print(f'balance = {balance}')

# balance *= 2
# print(f'balance = {balance}')

# balance /= 4
# print(f'balance = {balance}')

#T3

# product_price = int(input('Enter the product price: '))
# interest_rate = float(input('Enter the discount percent: '))
# discount_amount = product_price * interest_rate
# net_price = product_price - discount_amount
# print(f'Discount amount: {discount_amount}\n final price: {net_price} ' )

#T4

# principle = int(input('Enter the principle amount: '))
# annual_interest_rate = float(input('Enter the annual_interest_rate: '))
# annual_interest_payment = principle * annual_interest_rate
# nominal_value = principle + annual_interest_payment
# print(f'Annual interest payment: {annual_interest_payment}\n Nominal value: {nominal_value} ' )

#T5

# grade1 = float(input('Enter a grade: '))
# grade2 = float(input('Enter a grade: '))
# grade3 = float(input('Enter a grade: '))
# total = grade1 + grade2 + grade3
# average = total/3
# print(f'The average of the 3 grades is: {average}')

# #Part ב

# #T6

# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"
# f_string_sentence = f'Hello, my name is {first_name} {last_name} and I live in {city}.'
# concatenation_string_sentence = 'Hello, my name is ' + first_name + ' ' + last_name  + ' ' 'and I live in ' + city + '.'
# print(f_string_sentence)
# print(concatenation_string_sentence)

# #T7
# full_name = input('Enter your full name: ')
# print(full_name)
# print(len(full_name))
# print(full_name.upper())
# print(full_name.lower())

#T8
# sentence = input('Enter a sentence: ')
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.title())

#T9
# raw_name = input('Enter your name: ')
# cleaned_name = raw_name.strip()
# raw_name_length = len(raw_name)
# cleaned_name_length = len(cleaned_name)
# print(raw_name,cleaned_name,raw_name_length,cleaned_name_length)

#T10
# sentence = "I love Java programming"
# python_replace = sentence.replace('Java','Python')
# love_count = sentence.count('love')
# starts_with_I = sentence.startswith('I')
# ends_with_programming = sentence.endswith('programming')
# print(python_replace)
# print(f'love count in sentence: {love_count}')
# print(f'Does the sentence start with "I"? {starts_with_I}')
# print(f'Does the sentence end with "programming"? {ends_with_programming}')

#T11
# word = "Programming"
# print(word[0:1])
# print(word[-1:])
# print(word[2:3])
# print(word[:3])
# print(word[-3:])
# print(word[-4:])
# print(word[-1::-1])

#Part ג

#T12
# a = "100"
# b = "25"
# c = 10
# d = 5.5

# a = int(a)
# b = float(b)
# c = str(c)
# d = int(d)
# print(f'a has the value: {a} and the type {type(a)}')
# print(f'b has the value: {b} and the type {type(b)}')
# print(f'c has the value: {c} and the type {type(c)}')
# print(f'd has the value: {d} and the type {type(d)}')

#T13

# age = input("Enter your age: ")
# #original code will not work because age is a string and it can't be added to 10 which is an int:
# #print(age + 10)
# print(int(age)+10)

# #T14
# original_price = float(input('Enter the original price: ' ))
# VAT = 0.18
# total_price = original_price * (1+VAT)
# print(f"{total_price:.2f}" )

#Part ד

#T15
# first_name = input('Enter your first_name: ')
# last_name =  input('Enter your last_name: ')
# age =  int(input('Enter your age: '))
# monthly_salary = int(input('Enter your monthly salary: '))
# years_employed =  int(input('Enter the number of years at the company: '))
# annual_salary = monthly_salary*12
# raised_salary = monthly_salary*0.05
# full_name_character_count = len(first_name.strip()) + len(last_name.strip())

# print(f'''====== Employee Report ======
# Name: {first_name} {last_name}
# Age: {age}
# Monthly Salary: {monthly_salary}
# Years in the Company: {years_employed}
# Annual Salary: {annual_salary}
# Monthly Salary After Raise: {raised_salary}
# Full Name length: {full_name_character_count}
# ==============================
# ''')

#T16
# usd_rate = 3.25
# shekel_sum = float(input('Enter a sum in shekels: '))
# euro_rate = 3.75
# sum_in_dollars = shekel_sum/usd_rate
# sum_in_euros = shekel_sum/euro_rate
# conversion_fee_rate = 0.02
# after_fee_dollars = sum_in_dollars - (sum_in_dollars*conversion_fee_rate) 
# after_fee_euros = sum_in_euros - (sum_in_euros*conversion_fee_rate)
# print(sum_in_euros,sum_in_dollars,after_fee_dollars,after_fee_euros) 

#T17
# first_name = input('Enter your first_name: ').strip().lower()
# last_name =  input('Enter your last_name: ').strip().lower()
# birth_year =  int(input('Enter your birth year: '))
# email = f'{first_name}.{last_name}.{birth_year}@gmail.com'

#T18

sentence = input('Enter a sentence: ')
print(sentence)
print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence[-1::-1])
print(sentence.count('a'))
print(sentence.replace(' ','-'))

#part ה

# פרויקט מסכם

