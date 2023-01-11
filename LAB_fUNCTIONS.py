
## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
def function (num):
    '''
    I used insted for loop to print the numbers in rows by rows 
    with dec the numbers 

    '''
    for x in range (num, 0 , -1):
        for y in range (x , 0 , -1):
            print(y, end=' ')
        print(" ")

function(5)

### Document the newly created function. describe what it does, then print the documentation. 

print(function.__doc__)


