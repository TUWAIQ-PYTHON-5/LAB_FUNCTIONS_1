def pattern (num :int) -> int:
    '''this functon'''
    while num != 0:
        print(num, end="")
        num = num-1

usrNumber: int = int(input("Enter a Number"))

while usrNumber != 0:
    pattern(usrNumber)
    print()
#    print(value)
    usrNumber = usrNumber -1
print(pattern.__doc__)
