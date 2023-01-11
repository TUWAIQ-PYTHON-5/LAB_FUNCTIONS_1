

def myFunction(num):
    ''' here where i can put  the doc '''

    for i in range (num , 0, -1):
        for j in range (i,0,-1):
            print (j , end=" ")
        print (" ")

myFunction(10)
print(myFunction.__doc__)
