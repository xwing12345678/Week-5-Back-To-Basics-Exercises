# Part א
#T1
i = 1
while not i > 10:
    print (i)
    i+=1

#T2
i = 10
while not i < 1:
    print (i)
    i-=1
print("START!")

#T3
i = 1
while not i > 50:
    if i % 2 == 0:
        print (i)
    i+=1

#T4
# user_input = input("Enter a whole positive number: ")
# user_number = int(user_input)
# Accumulator = user_number
# while Accumulator <= user_number *5:
#     print(Accumulator)
#     Accumulator += user_number

#T5
number = 1
Accumulator = 0
while Accumulator <= 100:
    Accumulator += number
print (Accumulator)

#part ב

# #T6
# password = "Python123"
# user_try = ""
# while user_try != password:
#     user_try = input("Enter in your password: ")
# print("Welcome!")

#T7
# secret_number = 27
# user_number = 0
# while user_number != secret_number:
#     user_try = input("Guess the number: ")
#     if not user_try.isdigit():
#         continue
#     user_number = int(user_try)
    
# print("Congradulations you guessed correctly!")

#T8
# exit_number:int = 0 
# number_list:list[int] = []
# user_number = 10
# loop_exit = False

# while loop_exit == False:
#     user_try = input("Enter a Grade: ")
#     if not user_try.isdigit():
#         continue
#     user_number = int(user_try)
#     if user_number == exit_number:
#         loop_exit = True
#     else:
#         number_list.append(user_number)
# print(sum(number_list))

#T9
# loop_exit = False
# exit_number:int = 999
# grade_list:list[int] = []
# while loop_exit == False:
#     user_try = input("Enter a Grade: ")
#     if not user_try.isdigit():
#         continue
#     user_number = int(user_try)
#     if user_number == exit_number:
#         loop_exit = True
#     else:
#         grade_list.append(user_number)
# grade_sum = sum(grade_list)
# grade_count = grade_list.__len__()
# print(grade_count)
# print(grade_sum)
# if grade_sum > 0:
#     print (grade_sum//grade_count)
# else:
#     print(0)

#T10
# loop_exit = False
# exit_number:int = 0
# number_list:list[int] = []
# while loop_exit == False:
#     user_try = input("Enter a number: ")
#     user_number = int(user_try)
#     if user_number < exit_number:
#         loop_exit = True
#     else:
#         number_list.append(user_number)
# number_sum = sum(number_list)
# number_count = number_list.__len__()
# print(f'You entered {number_count} numbers')
# print(f'For a total of:{number_sum}')
         
# part ג

#T11
# user_number = int(input("Enter a number: "))
# i = 1
# while i >=10:
#      print(f'{user_number} x {i} = {user_number*i} ')

#T12
# user_input = input("Enter a whole number: ")
# user_number = int(user_input)
# digit_count = 0
# while user_number > 0:
#     user_number //= 10
#     digit_count+=1
# print(f'{digit_count} digits')

#t13
# user_input = input("Enter a whole number: ")
# user_number = int(user_input)
# fliped = 0
# while user_number > 0:
#     fliped = (fliped* 10 + user_number % 10)
#     user_number //= 10
# print(fliped)

#t14
# user_input = input("Enter a whole number: ")
# user_number = int(user_input)
# i = 2
# proven_non_prime = False
# while i < user_number:
#     if user_number % i == 0:
#         print(f'{user_number} is not a prime number, {user_number} can be divided by {i}!')
#         proven_non_prime = True
#     i += 1
# if proven_non_prime == False:
#     print(f"{user_number} is a prime!")

#T15
# balance = 5000
# running:bool = True
# while running == True:
#     choice = input(f'''Welcome to the banking system! \n
#  Please chose one of the following options:
#  1. Check ballance \n
#  2. Deposit money \n
#  3. Withdraw money \n
#  4. Exit 
# ''')
#     if choice == '1':
#         print(f'Your remaining ballance is: {balance}.')
#     elif choice == '2':
#         raw_withdrawal = input(f'Enter the amount of money you wish to deposit. \n You may not enter a negative number! \n Amount: ')
#         Withdrawal = float(raw_withdrawal)
#         if not Withdrawal >= 0:
#             print("You can only deposit a positive amount!")
#         balance += Withdrawal
#         print(f'Thank you for your deposit! Your ballance is now {balance}')
#     elif choice == '3':
#         raw_withdrawal = input(f'Enter the amount of money you wish to withdraw. \n You may not enter a negative number! \n Amount: ')
#         Withdrawal = float(raw_withdrawal)
#         if not Withdrawal >= 0:
#             print("You can only withdraw a positive amount!")
#         balance -= Withdrawal
#         print(f'Withdrawal confirmed! Your ballance is now {balance}')
#     else:
#         print("Thank you for using the banking system!\n We hope to see you again soon!")
#         running = False
#         break

#Part ד
#T16

# i = 1
# while True:
#     print (i)
#     i+=1
#     if i == 15:
#         break

# #T17
# i = 0
# while True:
#     i+=1
#     if i % 3 == 0:
#         continue
#     print (i)
#     if i == 31:
#         break

# #T18
# # end_number = 100
# # while True:
# #     user_input = input("Guess the number: ")
# #     user_number = int(user_input)
# #     if user_number == end_number:
# #         print('Congradulations you entered the correct number!')
# #         break

# #Part ה

# #T19
# for i in range(1,20):
#     print(i)

# #T20
# for i in range(0,101,5):
#     print(i)

# #T21
# Accumulator = 0
# for i in range(1,100):
#     Accumulator += i
# print(Accumulator)

# #T22
# user_input = input("Guess the number: ")
# user_number = int(user_input)
# for i in range(1,11): 
#     print(f'{user_number} x {i} = {user_number*i} ')

# #T23
# start_range = int(input("Enter the start number: "))
# end_range = int(input("Enter the end number: "))
# accumulator = 0
# for i in range(start_range,end_range+1):
#     accumulator += i
# print(f'Result: {accumulator}')

# #T24

# for i in range (1,100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

#Part ו

#T25
# row_count = int(input("Enter the number of rows: "))
# colunm_count = int(input("Enter the number of colunms: "))
# for row in range(1,row_count+1):
#     row_string = ""
#     for colunm in range(1,colunm_count+1):
#         row_string += '*'
#     print(row_string)

#T26
# row_count = 6
# colunm_count = 1
# row_string = ""
# for row in range(1,row_count+1):
#     for colunm in range(1,colunm_count+1):
#         row_string += '*'
#     print(row_string)

#T27
for multiple_a in range(1,11):
    for multiple_b in range(1,11):
        print(f'{multiple_a} x {multiple_b} = {multiple_a*multiple_b}')

#T28
for root_number in range(1,6):
    for iteration in range(1,6):
        print(f'{root_number}, {iteration}')


# Part ז





