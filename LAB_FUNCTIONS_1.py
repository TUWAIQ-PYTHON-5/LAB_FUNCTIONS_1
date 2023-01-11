## Create a function that takes 1 parameter of type int , then it prints out the result formatted 
# like the following patter (if we give it 5 for example):
# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1   

def triangle( num : int):
    '''the triangle funaction take an integer number as a parammeter then make tringle by decrsing one number every time until number 1'''
    count = num
    exit = num
    exit = exit - 1
    while count != 0 :
        print(count, "" ,end="")
        count = count-1
        if exit == 0:
            break

    else :   
        print("")  
        triangle(exit)

triangle(5)

### Document the newly created function. describe what it does, then print the documentation. 
print()
print(triangle.__doc__)
