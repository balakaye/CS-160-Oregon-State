import random

user_input = int(input('Enter the amount of random numbers you want: '))


large = 0
for x in range(user_input):
    ranNum = random.randint(0,5)
    print('Random number' + str(5) + ' is ' + str(ranNum))

    if (ranNum > large):
        large = ranNum


print('The largest number is: ' + str(large))