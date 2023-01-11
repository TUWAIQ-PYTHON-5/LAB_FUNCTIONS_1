def fun(x):
    ''' this is lab 1'''
    for i in range(x , 0 , -1):
        for j in range(i , 0 , -1):
            print(j , end=" ")
        print(" ")

fun(15)        
print(fun.__doc__)