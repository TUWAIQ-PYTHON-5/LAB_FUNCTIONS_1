
def my_function(p1 : int ) -> int:
    ''' this function print the parameter '''
    for i in range(p1, 0, -1):
        for j in range (i,0,-1):
            print(j, end="  ")
        print(" ")
my_function(7)

print(my_function.__doc__)