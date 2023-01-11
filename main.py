def numbers(number1:int) -> int:
    '''this function will print the numbers desc order'''

    for r in range(number1,0,-1):
        for c in range(r,0,-1):
            print(c,end=" ")
        print()
    
numbers(5)