def calculator():

    print("\nBasic Calculator.\n")

    num_1 = input('Enter your first number: ')
    operation = input('Enter your operation:\n1 for addition \n2 for subtraction \n3 for multiplication \n4 for division \n5 for exponet')
    num_2 = input('Enter your second number: ')

    if operation == ('1'):
        sum = float(num_1) + float(num_2)
        print('The answer is:',(sum))

    elif operation == ('2'):
        sum = float(num_1) - float(num_2)
        print('The answer is:',(sum))

    elif operation == ('3'):
        sum = float(num_1) * float(num_2)
        print('The answer is:',(sum))
    
    elif operation == ('4') and num_2 == ('0'):
        print('\nYou cannot divide by zero.')

    elif operation == ('4'):
        sum = float(num_1) / float(num_2)
        print('The answer is:',(sum))

    elif operation == ('5'):
        sum = float(num_1) ** float(num_2)
        print('The answer is:',(sum))

    else:
        print('Invalid operation.')

    restart = input('\nDo you want to enter another equation? yes or no?').lower()

    if restart == ('yes'):
        calculator()

    else:
        print('\nEnding Program.')
        quit()

calculator()