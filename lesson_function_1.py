# LAB_FUNCTIONS_1

## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

#5 4 3 2 1   
#4 3 2 1   
#3 2 1   
#2 1   
#1   





def triangle (x : int):
    ''' 
    you can but any number to display it as reverse triangle 

    '''

    for i in range (x,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print(" ")

triangle(5)

### Document the newly created function. describe what it does, then print the documentation. 
print(triangle.__doc__)