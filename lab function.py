
def num1(n : int):
  '''  '''
  num = n
  return num
num = 5

for i in range(0, num):
    for j in range(num - i,0, -1):
        print(j, end="")
    print()
print(num1.__doc__)