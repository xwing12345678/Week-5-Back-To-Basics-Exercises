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
# user_input = input("Enter a whole poitive number: ")
# user_number = int(user_input)
# Accumulator = user_number
# for number in range (1,6):
#     print(Accumulator)
#     Accumulator += user_number

#T5
Accumulator = 0
for number in range (1,101):
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
# for i in range(1,11):
#     print(f'{user_number} x {i} = {user_number*i} ')

#T12
# user_input = input("Enter a whole number: ")
# user_number = int(user_input)
# digit_count = 0
# while user_number > 0:
#     user_number //= 10
#     digit_count+=1
# print(f'{digit_count} digits')

#t13
user_input = input("Enter a whole number: ")
user_number = int(user_input)
fliped = 0
while user_number > 0:
    fliped = (fliped* 10 + user_number % 10)
    user_number //= 10
print(fliped)

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






