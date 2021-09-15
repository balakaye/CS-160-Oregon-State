
def fun(a: int, b: int) -> int:
    #if (a == b):
        #return 1
    if (a < b):
        return fun(a+1, b) + fun(a, b-1)
    else:
        return fun(a-1, b) + fun(a, b+1)
def main():
    print(fun(2, 4))

main()
'''
def pow_iterative(base: int, exp: int) -> int:
    result=1
    for n in range(exp):
        result = result * base
    return result
def main():
    base=int(input("Enter the base: "))
    exp=int(input("Enter the exponent: "))
    print(pow_iterative(base, exp))
main()
'''