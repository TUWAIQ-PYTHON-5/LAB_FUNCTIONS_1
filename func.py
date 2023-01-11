
def number(num):
    '''print this function'''
    for i in range(0,num+1):
        for x in range(num-i, 0 ,-1):
            print(x, end=" ")
  
        print(" ")
number(5)
print(number.__doc__)