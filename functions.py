#exercise 1
def pyramids(rounds) -> None:
    '''This function takes 1 parameter of type int , then it prints out a triangular pattern'''
    while rounds != 0:
        result = ""
        number = rounds
        while number != 0:
            result = result + str(number) + " "
            number = number - 1
        print(result)
        rounds = rounds - 1

pyramids(5)

#exercise 2
print(pyramids.__doc__)