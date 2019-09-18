# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:22:19 2019

@author: hp
"""

message = "Cool!"
print(message)
print("Cool!")

string_test = 'I told my friend, "Python is a good language!"'
print(string_test)

string_test = "I told my friend, 'Python is a good language!'"
print(string_test)
print(string_test.title())
print(string_test.upper())
print(string_test.lower())

first_name = "XIAO"
last_name = "LIU"
full_name = first_name + " " + last_name

print(full_name)

birthday = str(11.04)

full = first_name + " " + last_name + ": " + birthday
print(full)

# test for Python 3
digital_test = 3 / 2
print(str(digital_test))

# import this

# name = input('Input name: ')
# age = input('Input age: ')
# print('His name is {} and his age is {}'.format(name, age))

pi = 3.1415926
print('The pi\'s short format is {:.2f}'.format(pi))

a = 3
b = 5
print(b // a)
print(not 1)

num = int(input('Please input an integer: '))
if 10 < num and num < 20:
    print('20>num > 10')
elif num == 10:
    print('num = 10')
else:
    pass
    # print('num < 10')

print('It is {}'.format(num))

class_mate = ['Tom', 'Peter', 'Jason']

for name in class_mate:
    print(name)

# range() includes head and ignore tail, make sure i+1
for i in range(1, 10):
    print(i)

a = 0
while a < 10:
    a = a + 1  # put the regular thing at first
    if a == 5:
        continue
    print(a)

# little test from shiyanlou
# my method
for i in range(0, 18):
    i = i + 1
    if i % 7 != 0:
        if i < 10:
            if str(i)[0] != '7':
                print(i)
        elif 10 <= i < 99:
            if str(i)[0] != '7' and str(i)[1] != '7':
                print(i)

# offical answer
i = 0
while i < 29:
    i = i + 1
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        continue
    print(i)
