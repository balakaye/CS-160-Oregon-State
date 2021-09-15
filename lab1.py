
'''
# This line of code will create a variable binNum and
# assign the input to it using the assignment operator (=)
binNum = int(input("Enter a binary number "))
# Print the value in binNum to make sure you read it correctly
print(binNum)

print(binNum % 10)
binNum =binNum//10

print(binNum//2**3)
binNum=binNum-(binNum//2**3)2**3
print(binNum//2**2)
binNum=binNum-(binNum//2**2)2**2
print(binNum//2**1)
binNum=binNum-(binNum//2**1)2**1
print(binNum//2**0)
'''
'''
binary = input('Enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print(decimal)
'''
x= int(input("Enter binary number: "))
print(x)

if x >= 1000:
    decimal =+8
    x =-1000
if x >=100:
    decimal =+4
    x =-100
if x >=10:
    decimal =+2
    x =-10
if x >1:
    decimal =+1
    x =- 1


print(decimal)