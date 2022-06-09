# calculator function
def calculator(int1, int2, op):
    if op == '*':
        print(int1*int2)
    if op == '/':
        print(int1/int2)
    if op == '-':
        print(int1-int2)
    if op == '+':
        print(int1+int2)
    if op == '%':
        print(int1 % int2)
    if op == '//':
        print(int1//int2)


num1 = int(input("enter num1= "))
num2 = int(input("enter num2= "))
a = input('enter operator= ')
calculator(num1, num2, a)
