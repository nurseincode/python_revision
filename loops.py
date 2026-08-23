# while loop

# number = 1
# while number <= 5:
#     print(number)
#     number +=1 

# for loop

# names = ['Dee', 'Dot', 'Dop', 'Tee']

# for name in names:
#     print(name)

# for name in enumerate(names):
#     print(name)

# fruits = ['apple', 'banana', 'cherry']
# for fruit in enumerate(fruits):
#     print(fruit)

# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# for index, name in enumerate(names):
#     print(f'{index+1}. {name}')

# List all numbers between 0 to 20 and state whether odd or even

# for i in range(0, 21):
#     if i % 2 == 0:
#         print(f'{i} is even')
#     else:
#         print(f'{i} is odd')

#  with ternary
# for num in range(0,21):
#     print(f'{num} is {'even' if num % 2 == 0 else 'odd'}')

# further refactor w caveat**
    #   print(f'{num} is {'odd' if num % 2 else 'even'}')


# for else

# for i in range(10):
#     print(i)
#     if i == 6:
#         break
# else:
#     print('loop finished')

# Output if a number is prime

number = 7

for i in range(2, number):
    if number % i == 0:
        print('not a prime')
        break
else:
    print('is prime')
    



