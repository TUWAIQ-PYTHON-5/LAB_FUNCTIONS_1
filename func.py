
def number(num):
    for i in range(0,num+1):
        for x in range(num-i, 0 ,-1):
            print(x, end=" ")
  
        print(" ")
number(5)