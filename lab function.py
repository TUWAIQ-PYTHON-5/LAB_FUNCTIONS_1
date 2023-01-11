
def num1(n : int):
  '''  '''
 
  for i in range(n, 0,-1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

num1(5)
print(num1.__doc__)