# LAB_FUNCTIONS_1

## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
'''
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   
'''
### Document the newly created function. describe what it does, then print the documentation. 

def pattern (num :int) -> int:
    ''' This Function Arrange and print all the numbers under certin givin number'''
    while num != 0:
        print(num, end=' ')
        num = num-1
    
usrNumber: int = int(input("Enter a Number"))

while usrNumber != 0:
    pattern(usrNumber)
    print ()
#    print(value)
    usrNumber = usrNumber -1

print(pattern.__doc__)