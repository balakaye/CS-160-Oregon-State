#ask user user for an input, 
num = int(input('Enter a positive integer: '))


def fib_recursive(n):
    if n<0:
        print("Incorrect input")

    elif n==0:
        return 0

    elif n==1:
        return 1

    else:
        return fib_recursive(n-1)+fib_recursive(n-2)

print(fib_recursive(num))

x = int(input('Enter an integer for the base: '))
y = int(input('Enter an integer for the exponent: '))

def power(x, y):
    if y == 0:
        return 1

    if y >= 1:
        return x * power(x, y - 1)
print(power(x, y))




