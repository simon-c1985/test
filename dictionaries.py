from pip._vendor.distlib.compat import raw_input

person = {
    'first name': 'Jack',
    'last name': 'Black',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daugter': 'Pamela'}
}
print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])
print(person['hobbies'][2])
print(person.keys())

# Exercise

print('///////////////////Exercise///////////////////')

dic = {
    'person': 'human',
    'sex': 'man',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daugter': 'Pamela'}
}
print(dic['person'])
# res = input('Input Start time: ["2019-01-01"]' or "2019-01-01")
#
# print(res)

res = input('Folder [default] : ' or 'default') or 'def'
# res = res or 'default'
print(res)