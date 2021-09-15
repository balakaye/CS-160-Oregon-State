num = int(input('Enter a number:  '))

def pattern (n: int, i: int):
    if n == 0:
        return pattern(n/2, i)

    for k in range(i):
        print(" ", end='')
    for k in range(n):
        print("* ", end='')
    print("")

    pattern(n//2, i + n)
pattern (num,0)