def my_function(p1 : int ) -> int:
    ''' this function print the parameter '''
    par1 = p1
    return par1
par1 = 5
for i  in range(0, 5):
    for j in range(par1 - i, 0, -1):
        print(j, end=' ')
    print()
print(my_function.__doc__)


'''

def my_function(p1 : int ) -> int:
 'this function print the parameter '
    par1 = p1
    return par1
res = my_function(5)
print(res)
print(my_function.__doc__)

'''