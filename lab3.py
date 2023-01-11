def number (num: int) -> None :
    '''print number '''
    for i in range(num , 0 ,-1):
        for j in range(i , 0 , -1) :
            print(j , end= " ")
        print(" ")



number(5)
print (number.__doc__)