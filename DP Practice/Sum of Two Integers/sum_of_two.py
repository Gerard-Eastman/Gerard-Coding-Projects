

def getSum(a: int,b: int)-> int:
    c = int(0)
    while(b != 0):
        c = a & b
        a = a ^ b
        b = c << 1
    return a

answer = getSum(int(input("A equals?\n")), int(input("B equals?\n")))
print("Their sum is {}\n".format(answer))