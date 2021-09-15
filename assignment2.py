
# User enters input, turns into interger, assigns num to a number
num=int(input('Enter a number below below 256: ')) 

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


binary = input('Enter a 8-bit binary number: ')
decimal = 0
for digit in binary:    
    decimal = decimal*2 + int(digit)

print(decimal)