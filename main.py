# LAB_FUNCTIONS_1

## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1   

### Document the newly created function. describe what it does, then print the documentation


def printNumber(num1 : int):
    '''This function is doing print only'''
    for i in range(0  ,num1 + 1):
        for j in range(num1 -i , 0 , -1):
            print(j, end=' ')
        print()    


printNumber(6)
print(printNumber.__doc__)

       

    

