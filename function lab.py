def func1 (rows1 :int) -> int :
    '''this function will be return the number of parameters'''
    rows = rows1 
    return rows 
rows = 5 
for i in range(0, rows):
    for j in range(rows - i, 0, -1):
       print(j,end = '')
    print()
print (func1.__doc__)