from ctypes.wintypes import HACCEL


H = 1.00794
C = 12.01070
O = 15.99940


def MolWeight(a, b, c):
    print(a*H+b*C+c*O)


int1 = float(input("number of H atoms= "))
int2 = float(input("number of C atoms= "))
int3 = float(input("number of O atoms= "))
MolWeight(int1, int2, int3)
