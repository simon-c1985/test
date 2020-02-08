# def product(n, func):
#     result = 1
#     for number in range(1, n):
#         result *= func(number)
#     return result
#
#
# def square(x):
#     return x * x
#
#
# def cube(x):
#     return x * x *x
#
#
# print(product(4, cube))
#
#
#
# def my_function(a, b, func):
#     result = func([a, b])
#     return result
#
#
# print(my_function(7, 3, sum))
# from random import choice
#
#
# def colorize(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#     result = f'{get_color()} {thing}'
#     return result
#
#
# # print(colorize('apple'))
# # print(colorize('paper
#
#
# def make_color():
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#     return get_color
#
#
# first_color = make_color()
#
# print(first_color())
#
# second_color = make_color()
#
# print(second_color())
#
# third_color = make_color()
#
# print(third_color())
#
#
# def colorize(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return color
#     result = f'{get_color()} {thing}'
#     return result
#
#
# def colorize1(thing):
#     def get_color():
#         colors = ('red', 'green', 'yellow')
#         color = choice(colors)
#         return f'{color} {thing}'
#     return get_color
#
#
# # print(colorize1('apple')())
# colorize_dog = colorize1('dog')
# print(colorize_dog())
#
#
# def simple_function():
#     print('Simple function code')
#
#
# simple_function()
#
#
# def decorator_function(origiginal_func):
#     def wrap_function():
#         print('Some code before old code')
#         origiginal_func()
#         print('Some code after old code')
#     return wrap_function
#
#
# # decorated_function = decorator_function(simple_function)
#
# # decorated_function()
#
#
# @decorator_function
# def simple_function():
#     print('Simple function code')
#
#
# simple_function()
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def make_compliment(func):
# # # # # # # # #     def wrapper(*args, **kwargs):
# # # # # # # # #         func(*args, **kwargs)
# # # # # # # # #         if len(args):
# # # # # # # # #             print(f'Nice to meet you! {args[0]}')
# # # # # # # # #             print(f'What you want to eat? {args[0]}')
# # # # # # # # #         elif len(kwargs):
# # # # # # # # #             print(f'Here is your order:  {kwargs["food"]} and drink {kwargs["drink"]}')
# # # # # # # # #         else:
# # # # # # # # #             pass
# # # # # # # # #     return wrapper
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # @make_compliment
# # # # # # # # # def ask_name():
# # # # # # # # #     print('What is your name?')
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # ask_name()
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # @make_compliment
# # # # # # # # # def my_name(name):
# # # # # # # # #     print(f'My name is: {name}')
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # my_name('Mike')
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # @make_compliment
# # # # # # # # # def order(food, drink):
# # # # # # # # #     print(f'Give me {food} and {drink}')
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # order(food="chips", drink='cola')
# # # # # # # # from functools import wraps
# # # # # # # #
# # # # # # # #
# # # # # # # # def print_function_data(function):
# # # # # # # #     """
# # # # # # # #     thus is decorator function
# # # # # # # #     :param function:
# # # # # # # #     :return:
# # # # # # # #     """
# # # # # # # #     @wraps(function)
# # # # # # # #     def wrapper(*args, **kwargs):
# # # # # # # #         print(f'You are using {function.__name__}')
# # # # # # # #         print(f'Function documentation {function.__doc__}')
# # # # # # # #         return function(*args, **kwargs)
# # # # # # # #     return wrapper
# # # # # # # #
# # # # # # # #
# # # # # # # # @print_function_data
# # # # # # # # def squares_sum(a, b):
# # # # # # # #     """
# # # # # # # #     :param a: first number
# # # # # # # #     :param b: second number
# # # # # # # #     :return: sum of sqares first and second numbers (a * a + b * b)
# # # # # # # #     """
# # # # # # # #     return a ** 2 + b ** 2
# # # # # # # #
# # # # # # # #
# # # # # # # # # print(squares_sum(2, 3))
# # # # # # # # print(squares_sum.__doc__)
# # # # # # # # print(squares_sum.__name__)
# # # # # # # # help(squares_sum)
# # # # # # #
# # # # # # # from time import time
# # # # # # # from functools import wraps
# # # # # # #
# # # # # # #
# # # # # # # def speed_test(function):
# # # # # # #     @wraps(function)
# # # # # # #     def wrapper(*args, **kwargs):
# # # # # # #         start_time = time()
# # # # # # #         result = function(*args, **kwargs)
# # # # # # #         end_time = time()
# # # # # # #         print(f'Time of code execution {end_time - start_time}')
# # # # # # #         return result
# # # # # # #     return wrapper
# # # # # # #
# # # # # # #
# # # # # # # @speed_test
# # # # # # # def sum_with_list():
# # # # # # #     return sum([number for number in range(10000000)])
# # # # # # #
# # # # # # #
# # # # # # # # print(sum_with_list())
# # # # # # #
# # # # # # #
# # # # # # # @speed_test
# # # # # # # def sum_with_gen():
# # # # # # #     return sum(number for number in range(10000000))
# # # # # # #
# # # # # # #
# # # # # # # # print(sum_with_gen())
# # # # # # #
# # # # # # #
# # # # # # # @speed_test
# # # # # # # def product(range_value):
# # # # # # #     result = 1
# # # # # # #     for number in range(1, range_value):
# # # # # # #         result *= number
# # # # # # #     return result
# # # # # # #
# # # # # # #
# # # # # # # print(sum_with_list())
# # # # # # # print(sum_with_gen())
# # # # # # # print(product(100000))
# # # # # #
# # # # # # from functools import wraps
# # # # # #
# # # # # #
# # # # # # def prohibit_kwargs(func):
# # # # # #     @wraps(func)
# # # # # #     def wrapper(*arga, **kwargs):
# # # # # #         if kwargs:
# # # # # #             raise ValueError('Keyword arguments are prohibited')
# # # # # #         return func(*arga, **kwargs)
# # # # # #     return wrapper
# # # # # #
# # # # # #
# # # # # # def prohibit_arguments(func):
# # # # # #     @wraps(func)
# # # # # #     def wrapper(*args, **kwargs):
# # # # # #         for val in args:
# # # # # #             if type(val) == int:
# # # # # #                 raise ValueError('Integer arguments are prohibited')
# # # # # #         for key, val in kwargs.items():
# # # # # #             if type(val) == int:
# # # # # #                 raise ValueError('Integer arguments are prohibited')
# # # # # #         return func(*args, **kwargs)
# # # # # #     return wrapper
# # # # # #
# # # # # #
# # # # # # @prohibit_arguments
# # # # # # def print_hello(name):
# # # # # #     print(f'Hello {name}!')
# # # # # #
# # # # # #
# # # # # # print_hello('Jack')
# # # # # # print_hello(3)
# # # # # #
# # # # #
# # # # #
# # # # # from functools import wraps
# # # # #
# # # # #
# # # # # def check_if_first_arg_is(value):
# # # # #     def inner_dec(func):
# # # # #         @wraps(func)
# # # # #         def wrapper(*args, **kwargs):
# # # # #             if args and args[0] != value:
# # # # #                 print(f'First argument has to be {value}')
# # # # #             return func(*args, **kwargs)
# # # # #         return wrapper
# # # # #     return inner_dec
# # # # #
# # # # #
# # # # # @check_if_first_arg_is('red')
# # # # # def print_rainbow_colors(*colors):
# # # # #     print(colors)
# # # # #
# # # # #
# # # # # @check_if_first_arg_is(7)
# # # # # def multi_seven(a, b):
# # # # #     return a * b
# # # # #
# # # # #
# # # # # print(multi_seven(8, 3))
# # # # #
# # # #
# # # # from functools import wraps
# # # #
# # # #
# # # # def enforce(*types):
# # # #     def inner_dec(func):
# # # #         @wraps(func)
# # # #         def wrapper(*args, **kwargs):
# # # #             new_args =[]
# # # #             for a, t in zip(args, types):
# # # #                 new_args.append(t(a))
# # # #             return func(*new_args, **kwargs)
# # # #         return wrapper
# # # #     return inner_dec
# # # #
# # # #
# # # # @enforce(str, int)
# # # # def print_text_n_times(text, n):
# # # #     for number in range(n):
# # # #         print(text)
# # # #
# # # #
# # # # print_text_n_times(5555, '5')
# # #
# # # #
# # # # from functools import wraps
# # # #
# # # #
# # # # def print_args(func):
# # # #     @wraps(func)
# # # #     def wrapper(*args, **kwargs):
# # # #         print(f'args: {args}')
# # # #         print(f'kwargs: {kwargs}')
# # # #         return func(*args, **kwargs)
# # # #     return wrapper
# # # #
# # # #
# # # # @print_args
# # # # def some_func():
# # # #     print('Some code')
# # # #
# # # #
# # # # some_func()
# # #
# # #
# # # from functools import wraps
# # #
# # #
# # # def hello_from_decorator(func):
# # #     @wraps(func)
# # #     def wrapper(*args, **kwargs):
# # #         return f'hello_from_decorator {func(*args, **kwargs)}'
# # #     return wrapper
# # #
# # #
# # # @hello_from_decorator
# # # def some_func():
# # #     return 3
# # #
# # #
# # # print(some_func())
# # #
# # #
# #
# # from functools import wraps
# #
# #
# # def prohibit_more_then_two_args(func):
# #     @wraps(func)
# #     def wrapper(*args):
# #         if len(args) < 3:
# #             return func(*args)
# #         else:
# #             raise ValueError('Function must have less than 3 arguments!')
# #     return wrapper
# #
# #
# # @prohibit_more_then_two_args
# # def some_func(a, b):
# #     return a + b
# #
# #
# # print(some_func(2, 22))
#
#
# # # # def enforce(*types):
# # # #     def inner_dec(func):
# # # #         @wraps(func)
# # # #         def wrapper(*args, **kwargs):
# # # #             new_args =[]
# # # #             for a, t in zip(args, types):
# # # #                 new_args.append(t(a))
# # # #             return func(*new_args, **kwargs)
# # # #         return wrapper
# # # #     return inner_dec
# # # #
# # # #
# # # # @enforce(str, int)
# # # # def print_text_n_times(text, n):
# # # #     for number in range(n):
# # # #         print(text)
# # # #
# # # #
# # # # print_text_n_times(5555, '5')
#
# from functools import wraps
# from time import sleep
# from time import time
#
#
# def wait(n):
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args):
#             start_time = time()
#             sleep(n)
#             print(f'Function wait {time() - start_time} seconds')
#             return func(*args)
#         return wrapper
#     return inner_dec
#
#
# @wait(5)
# def sum_a_b(a, b):
#     return a + b
#
#
# print(sum_a_b(1, 3))


# from time import sleep
# from time import time
# from functools import wraps
#
#
# def wait(n):
#     def init_func(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start_time = time()
#             sleep(n)
#             func(*args, *kwargs)
#             print(f'There was a pause {n} seconds before execution {func.__name__}')
#             print(start_time - time())
#         return wrapper
#     return init_func
#
#
# def func_plus():
#     x = int(input("Enter X:  "))
#     y = int(input ('Enter Y:  '))
#     return x + y
#
#
# @wait(func_plus())
# def func_a_plus_b(a, b):
#     print(a + b)
#     return a + b
#
#
# func_a_plus_b(2, 3)
