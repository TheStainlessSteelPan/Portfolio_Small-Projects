# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:17:46 2026
"""
# PYTHON Crash Course Notes
# STRINGS

print('Pythonn\nJava\nSQL\nC\nReact')
print('\tPrinting multi-line strings')

# Stripping whitespaces on strings using Rstrip and Lstrip and strip method
message = " Hello there, stranger! "
print(message.rstrip())
print(message.lstrip())
print(message.strip())

# Removing prefixes or suffixes?
student_ID = "ID.2025STEM1124.B24"
cleaned_ID = student_ID.removeprefix('ID.')
print(cleaned_ID)

suffix_ID = student_ID.removesuffix('.B24')
print(suffix_ID)

# NUMBERS (INTEGERS & FLOATS)
# Arithmetic
print(2 + 2)
print(2 - 1)
print(2 * 3)
# When dividing two integers, the result is always a float
print(10 / 2)

# Order of operations
print(1320/(2*3))

# Floats, a number with decimal point
num1 = 12.3324
print(num1)
print(type(num1))

# To easily read large digits of numbers, use underscore
large_num = 12_000_000_0000
print(large_num)

# Multiple variable assignments to one digit
x, y, z = 0, 0 ,0
print(x)
print(y)
print(z)

# import this
# Zen of Python


# Constants - variable whose vaule remains constant throughout

# Lists - a collection of elements, can be a mix of strings, numbers, floats, etc., EVEN FUNCTIONS
Stuff = ['Rock', 'Tree', 'Wood', 'Bark', 'Soil', 'Dirt', 'Poop', 'Grass', 'Mountain', 32, 234.22]
print(type(Stuff))

# Selecting values from a list - Each value has a designated number counted from 0
# Rock is 0, Tree is 1 and so on.
# Can be used to easily create messages and such
message = (f'Hello there {Stuff[1].upper()}. I am {Stuff[3].title()}.')
print(message)

sample_list = ['Item 1', 'Item 2', 'Item 3']
print(sample_list)
sample_list[1] = 'Item 45'
print(sample_list)

# using the list.append on a list or an empty list adds that object

sample_list.append('Item 34')
print(sample_list)

# To add an object on a specific index in a list, use the list.insert(index, object) statement
sample_list.insert(0, 'Newest Item FR')
print(sample_list)
# To delete any item, use the del list[] statement
del sample_list[-1]
print(sample_list)

# list.pop method by default removes the last item in the list and you can view the popped item by printing the assigned variable for pop
popped_list = sample_list.pop()
# ^ add the index in the () to specify which to remove and view
print(sample_list)
print(popped_list)

# same with list.pop method, but instead you specify the item rather than index.
# the list.remove method removes the first occurence of the value you specify

cars = ['honda', 'honda', 'toyota', 'mitsubishi', 'ford']
print(cars)
remove_car = 'honda'
cars.remove(remove_car)
print(cars)

# Exercises from page 41-42
guest_list = ['Robin Williams', 'Bob Ong', 'Tom Hanks', 'Nujabes', 'Jose Rizal']
aux_list = ['Bokman Brigand', 'Spot Securities', 'Tutong the Tyrant', 'Big Ben', 'Kitty the Kat']

g_count = len(guest_list)

import random as rand

# def print_slow(str):
#     """prints things depending on the speed you want  int >= 1 is slow"""
#     for letter in str:
#         sys.stdout.write(letter)
#         sys.stdout.flush()
#         time.sleep(0.03)

def guestdecline(position):
    """ Generates a random number based on the list given """
    return(rand.randrange(0,len(position)))

def guest_pop(listhere):
    """ Randomly chooses if a guest from the guest_list will decline invitation"""
    popped_list = listhere.pop
    return(listhere.pop(rand.randrange(0,g_count)))

for i in range(0,g_count):
    print(f'\nHello {guest_list[i]}, I am inviting you to dinner!')

for i in range(0, guestdecline(guest_list)):
    i = guest_pop(guest_list)
    print(f'\n***{i} declined the invite. Sorry.***')

while len(guest_list) != 5:
    for i in range(0, 5-len(guest_list)):
        i = aux_list[rand.randrange(0, len(aux_list))]
        print(f'\n{i} has been invited to dinner')
        guest_list.append(i)

print(guest_list[0:])

# Sorting
# Sort method PERMANENTLY changes the order of your list
# Sorted method serves as a preview mode of a sorted list

names = ['Archie', 'Zion', 'Belinda' , 'Mackerel', 'Scarceface', 'Celia']

print(f'\n{names}')
print(sorted(names))
print(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names)

# Reverse method only FLIPS the list, not rearrange alphabetically
names.reverse()
print(f'\n{names}\n')


#Pizza Exercise
pizzas = ['Pepperoni', 'Spinach', 'Triple Cheese', 'Mushroom Pizza']
comment = [' is a great pizza!', ' is a decent pizza.', ' is a good pizza!', ' is kinda mid for a pizza, sorry.']
for pizza in pizzas:
    print(f'{pizza}{comment[rand.randrange(0,len(comment))]}\n')
    
print('But in general, pizza is a great snack or even a meal!')

# Numerical List
# prints a list of even numbers from a given range
even_num = []
for i in range(2, 31, 2):
    even_num.append(i)
print(even_num)
    
numbers = list(range(1,21))
print(numbers)

squares = []

# for i in range(1,11):
#     square = i ** 2
#     squares.append(square)

# prints a list of square roots of the first 10 digits
y = int(input("Assign a positive integer <= 10: "))
for i in range(1,y+1):
    squares.append(i**2)
print(f'Square Root of {y} {squares}\n')

# prints a list of cube roots of the first 10 digits
x = int(input("Assign a positive integer <= 10: "))
n = [value**3 for value in range(1,x+1)]
print(f'Cube Root of {x} {n}\n')


# Multiplication table using for loop and .join(str)
n = int(input("Assign a positive integer <= 100: "))
print(f"Multiplication Table of the first {n} digits:")
for row in range(1,n+1):
        print('\t'.join(str(row*col) for col in range(1,n+1)))
