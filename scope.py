# # pi = 'outer pi variable'
# #
# # def print_pi():
# #     pi = 'inner pi variable'
# #     print(pi)
# #
# # print_pi()
# # print(pi)
#
# # Local Scope
#
# pi = 'global pi variable'
# def inner():
#     pi = 'inner pi variable'
#     print(pi)
#
# inner()
# Built-in Scope
# from math import pi
#
# # pi = 'global pi variable'
#
# def outer():
#     pi = 'outer pi variable'
#     def inner():
#         # pi = 'inner pi variable'
#         print(pi)
#     inner()
#
# outer()


# Enclosed Scope
pi = 'global pi variable'
def outer():
    pi = 'outer pi variable'
    def inner():
        #pi = 'inner pi variable'
        nonlocal pi
        #pi = 'inner pi variable'
        print(pi)
    inner()
    print(pi)

outer()
#print(pi)
