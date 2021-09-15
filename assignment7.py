def isAlphaNum(s: str) -> bool:
        
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9' or char == '_':
            return True
        else:
            return False


def isFloatingPoint(n: str) -> bool:

    check = True
    decimal = True
    power = True
    for i in range(len(n)):
        if n[0] == '+' or n[0] == '-' and len(n) > 1:
            check = check and True
        elif n[i] in '1234567890':
            check = check and True
        elif n[i] == '.' and i < len(n)-1 and decimal:
            if n[i+1] in '1234567890':
                check = check and True
                decimal = False
            else:
                check = False
        elif n[i] == 'e' or n[i] == 'E' and i < len(n)-1 and power:
            if i>0:
                check = check and True
                power = False
            else:
                check = False
        else:
            check = False
    return check



def main():
    n = input('Enter any number: ')
    print(isFloatingPoint(n))

    s = input('Enter any character or number: ')
    print(isAlphaNum(s))

main()