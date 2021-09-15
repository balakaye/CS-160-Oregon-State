
while True:
    run = input('Would you like to do a calculation or exit the program? (calc/exit): ').lower()

    if run == 'calc':

        while True:
            calc = input('Which calculator would you like to use? Programmer or Scientific: ').lower()

            if calc == 'programmer':
                
                while True:
                    num=int(input('Enter a number below 256: ')) 
                    if (num >= 0 and num <= 255):
                        print(num//2**7) 
                        num=num-(num//2**7)*2**7 
                        print(num//2**6)
                        num=num-(num//2**6)*2**6
                        print(num//2**5)
                        num=num-(num//2**5)*2**5
                        print(num//2**4)
                        num=num-(num//2**4)*2**4
                        print(num//2**3)
                        num=num-(num//2**3)*2**3
                        print(num//2**2)
                        num=num-(num//2**2)*2**2
                        print(num//2**1)
                        num=num-(num//2**1)*2**1
                        print(num//2**0)
                        break

                    elif num<0 or num>255:
                        print('Error: number has to be a positive integer or below 256!')
                        continue
                    else:
                        print('Error: invalid input')
                        continue

                binary = input('Enter a 8-bit binary number: ')
                decimal = 0
                for digit in binary:    
                    decimal = decimal*2 + int(digit)

                print(decimal)
                break
            
            if calc == 'scientific':

                def calculator():

                    num_1 = input('Enter your first number: ')
                    operation = input('1 for addition \n2 for subtraction \n3 for multiplication \n4 for division \n5 for exponet \nEnter your operation: ')
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
                        print('Error: invalid operation.')
                        
                calculator()
                break
                
            else:
                print('Error: please enter a valid input:]')
                continue

    elif run == 'exit':
        print('Ending program')
        quit()

    elif run!='calc' or run!='exit':
        print('Error: please enter a valid input:]')
        continue



