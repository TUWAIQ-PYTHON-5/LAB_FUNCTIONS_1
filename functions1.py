
def function(y):
    ''' here where i can put  the doc '''
    par = y
    return par
x = 5
for i  in range(0, 5):
    for j in range(x - i, 0, -1):
        print(j, end=' ')
    print()
print(function.__doc__)