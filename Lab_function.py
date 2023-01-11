
def number(x : int ) -> int:
    '''  function will print the parameter '''
    for i in range(x, 0, -1):
        for j in range (i,0,-1):
            print(j, end="  ")
        print(" ")
number(5)

print(number.__doc__)