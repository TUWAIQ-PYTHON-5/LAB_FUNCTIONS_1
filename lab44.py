def numbers(number):
     '''the function take numbers and print it in pattern'''
     for i in range(number,0,-1):
        for j in range(i,0,-1):
          print(j , end=" ")
        print(" ")

print(numbers.__doc__)

numbers(5)
