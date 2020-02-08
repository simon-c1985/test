# x = 0
# while x < 10:
#     print("less 10")
#     x += 1
# else:
#     x -= 1
#     print(f'{x} not more 10')
#
# for y in range(10):
#     print(y)
# else:
#     print(f'x = {y}')

# my_list = [1, 2, 3, 4, 5]
# for item in my_list:
#     if item == 3:
#         break
#     print(item)
# #    print('in for')
#
# # print('out for')
# from random import randint
# list = {}
# x = 0
# while x != 7:
#     x = randint(1, 10)
#     list[x] = x
# else:
#     print(list)
#     # print(set(list))

# my_string = 'dgdwerwgw wesd'
# for index, item in enumerate(my_string):
#     print(f'item in index {index} is {item}')
# print('a' in 'Jack')
# string = 'sfgsfag'
# print(string.index('f', 2))
# dict = {5: 'a', 2: 'b', 3: 'c'}
# list = (2, 4, 5, 6, 1)
# print(min(dict))
# greeting = 'hello'
# letter_list = [num for num in greeting]
# print(letter_list)
# number_list = [(int(num) - 3) + 2 ** 2
#                for num in '1234567890'
#                if int(num) % 2 != 0]
# print(number_list)
# number_list_2 = [6, 43, -2, 11, -55, -12, 3, 345]
# new_list = ['+' if number > 0 else '-' for number in number_list_2]
#
# number_string = '1234567890'
# new_list_2 = [int(number) if int(number) % 2 != 0
#               else 'none'
#               for number in number_string]
# print(new_list)
# print(new_list_2)

# number_dict = {'first': 1, 'second': 2, 'third': 3}
# new_dict = {key: value ** 3 for key, value in number_dict.items()}
# print(new_dict)
#
# number_list = [6, 43, -2, 11, -55, -12, 3, 345]
# number_dict = {number: number ** 2 for number in number_list}
# print(number_dict)
#
# number_list = [6, 43, -2, 0, 11, -55, -12, 3, 345]
# number_dict = {number: 'positive' if number > 0
#                else 'negative' if number == 0
#                else 'zero'
#                for number in number_list}
# print(number_dict)
#
# number_dict = {number: 'positive' if number > 0
#                else 'negative' if number < 0
#                else 'zero'
#                for number in number_list}
# print(number_dict)
# number_string = '1234567890'
# new_list_2 = [int(number) if int(number) % 2 != 0
#               else 'odd' if (int(number) % 2 == 0) & (int(number) > 0)
#               else 'zerro'
#               for number in number_string]
# print(new_list)
# print(new_list_2)

# number_list = [6, 43, -2, 11, -55, -12, 3, 345]
# number_dict = {number ** 2 for number in number_list}
# print(number_dict)
#
# # number_list = [6, 43, -2, 11, -55, -12, 3, 345]
# number_dict = {number ** 2 for number in range(3, 11)}
# print(number_dict)
#
# smile = '\U0001f600'
# for x in range(10):
#     count = 0
#     list = ''
#     while x >= count:
#         list += smile
#         count += 1
#     print(list)


# smile = '\U0001f600'
# for x in range(11):
#     count = 0
#     list = ''
#     for _ in range(x):
#         list += smile
#     print(list)

# for number in range(1, 11):
#     print('\U0001f600' * number)
#
# count = 1
# while count < 11:
#     print('\U0001f600' * count)
#     count += 1

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13]]
# print(nested_list)
# # print(len(nested_list))
# # print(nested_list[3][2])
# for num_list in nested_list:
#     print(num_list)
#     for val in num_list:
#         print(val)
# [[print(number) for number in inner_list] for inner_list in nested_list]

# greetings = ['hello', 'hi', 'hey', 'hola']
# # new_greetings = []
# new_greetings = [word[1] for word in greetings]
# print(new_greetings)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
new_digits_list = []
for num in digits:
    if num % 2 != 0:
        new_digits_list.append(num)
print(new_digits_list)

new_digits_list_2 = [num for num in digits
                     if num % 2 != 0]
print(new_digits_list_2)
