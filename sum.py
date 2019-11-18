import sys
from reference import *

def sum_points():
    G = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
    res = point_add(G, G)
    print(hex(res[0]).upper())
    print(hex(res[1]).upper())

if __name__ == '__main__':
    sum_points()