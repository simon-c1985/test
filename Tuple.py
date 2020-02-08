tuple_1 = (1, 2, 3,)
tuple_2 = ('one', 'hello')
tuple_3 = (3, 2.3, 'three')

print(tuple_1)
print(tuple_2)
print(tuple_3)
print(type(tuple_1))
print(tuple_1[1])
new_tuple = (tuple_1[0], 3, tuple_2[0])
print(new_tuple)

person_tuple = ('John', 'Smith', 1986)
first_name, last_name, year_of_birth = person_tuple

print(first_name, last_name, year_of_birth)

t1 = (1, 2, 5, 1, 7, 9)

print(t1.count(3))

print(t1.index(1, 1, 4))
print(t1)
# Exercise

print('///////////////////Exercise///////////////////')

computer = ('notebook', 'MacBook Pro', '2.6 GHz Intel Core i5',
            '8 GB 1600 MHz DDR3')
type, model, processor, memory = computer
print(type, model, processor, memory)
