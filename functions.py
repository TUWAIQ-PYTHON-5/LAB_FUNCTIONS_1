def name_age( age:int) -> None:
    ''' print number'''
    for i in range(age, 0, -1):
        for j in range(i, 0, -1):
             print(j, end= " ")
        print(" ")

name_age(10)
print (name_age.__doc__)


