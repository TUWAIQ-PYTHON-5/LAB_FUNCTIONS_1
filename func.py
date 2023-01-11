#Create a function 
def myFunc(num):

    for i in range(num,0,-1):
        for j in range(i , 0 , -1 ): 
            print(j , end= " ")
        print("")
   
myFunc(5)

print("-----------------------------")

#describe what it does
def somePrint()-> None:
    """Print something"""
    print("hello world")

somePrint()

