
error=True
while(error==True):
    letter = input("Enter a letter: ")
    if(len(letter)==1 and ((letter >= 'A' and letter <= 'Z') or (letter >= 'a' and letter <= 'z'))):
        print('alphabet character/letter')
        error=False
    else:
        print('Error: not a single character or letter to check.')

try:
    num=int(input("enter a number: "))
except:
    print('Error, not a number')
