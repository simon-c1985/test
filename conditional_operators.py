# x = 3
# if x > 3:
#     print('x > 3')
# elif x < 3:
#     print('x < 3')
# else:
#     print('x == 3')

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in number_list:
#     if number % 2 == 0:
#         print(f'{str(number)}  "Четное"')
#     elif number % 3 == 0:
#         print(f'{str(number)} "На три делится""')
#     else:
#         print(f'{str(number)} "Остальные числа"')

# greeting = 'Hello Python'
# x = 0
# y = 0
# for letter in greeting:
#     x += 1
#     if letter != 'o':
#         y += 1
#         print(letter)
# print(x, y)

# x = 0
# tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# for item in tuple_list:
#     print(item)
# for tupe in tuple_list:
#     for letter_1 in tupe:
#         print(f'tupe: {tupe} first symbol: {letter_1} and second symbol:') # {letter_2}')

# dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# for item in dictionary:
#     print(f'item in dictionary: {item}')
# for item in dictionary.items():
#     print(f'item in dictionary.items(): {item}')
# for item in dictionary.keys():
#     print(f'item in dictionary.keys(): {item}')
# for item in dictionary.values():
#     print(f'item in dictionary.values(): {item}')
# for key, value in dictionary.items():
#     print(f'key in dictionary: {key} key in dictionary: {value}')
# for number in range(10, 31):
#     if number % 2 == 0:
#         print(number)
# z = input('Enter number of repeat\n')
# for _ in range(int(z)):
#     print('Hello')

number = input('Enter any number\n\n\n\t')
if int(number) == 7:
    print('7 is a lucky number!')
else:
    print('Not now!')

integer_number = int(input('Enter integer number:\n\n\n\t'))
if integer_number % 2 == 0:
    print('This number is even')
elif integer_number % 2 != 0:
    print('The number is odd')
else:
    print('None')
