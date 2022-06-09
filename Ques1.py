def decToBinary(a):
    if a >= 1:
        decToBinary(a//2)
    print(a % 2, end='')


num = int(input("enter number= "))
decToBinary(num)