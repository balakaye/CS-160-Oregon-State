#print function prints the string
'''
print("hello world")

print(223%10)
print(223/10)
print(int(223/10))
'''

#num=int(input('Enter a number: '))



#print(bin(227))
'''
print(num%10)
print(int(num/10))
num=num//10
'''
#print(3%2)

print(10%2)
print(10//2)

print(223%2) #this will give me the last digit in the number
print(223//2) #this will give me everything to the left of the last digit

num=int(input('Enter a number: '))
'''
print(num%2)
num=num//2
print(num%2)
num=num//2
print(num%2)
num=num//2
print(num%2)
num=num//2
'''

print(num//2**3)
num=num-(num//2**3)*2**3
print(num//2**2)
num=num-(num//2**2)*2**2
print(num//2**1)
num=num-(num//2**1)*2**1
print(num//2**0)