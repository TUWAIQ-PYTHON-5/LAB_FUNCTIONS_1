def function (num):
    '''this function to print reverse number'''
    for i in range (1, num +1):
        line = ''
        for j in reversed (range (1,(num +1)- i)):
            line += str(j)
        print(line)
function(5)
print (function.__doc__)