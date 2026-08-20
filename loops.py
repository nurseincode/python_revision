# while loop

# number = 1
# while number <= 5:
#     print(number)
#     number +=1 

# for loop

names = ['Dee', 'Dot', 'Dop', 'Tee']

# for name in names:
#     print(name)

for name in enumerate(names):
    print(name)

# fruits = ['apple', 'banana', 'cherry']
# for fruit in enumerate(fruits):
#     print(fruit)

# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

for index, name in enumerate(names):
    print(f'{index+1}. {name}')
