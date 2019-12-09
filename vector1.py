import sys
from reference import *

def vector1():
    seckey = bytes_from_int(0xB7E151628AED2A6ABF7158809CF4F3C762E7160F38B4DA56A784D9045190CFEF)
    msg = bytes_from_int(0x243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89)
    sig = schnorr_sign(msg, seckey)
    pubkey = pubkey_gen(seckey)

    # The point reconstructed from the public key has an odd Y coordinate.
    pubkey_point = point_from_bytes(pubkey)

if __name__ == '__main__':
    vector1()