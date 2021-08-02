import gmpy2
import math
import binascii
    
f = open("n_1.txt", "+r")
N = int(f.read())
f.close()

f = open("y_4.txt", "+r")
y = int(f.read())
f.close()

A = gmpy2.isqrt(N)
A += 1
	
x = gmpy2.isqrt(A * A - N)
	
p = A - x	
q = A + x
	
if N - p * q == 0:
	
	phi = (p - 1) * (q - 1)
	
	e = 65537
	
	d = gmpy2.powmod(e, -1, phi)
	
	x = gmpy2.powmod(y, d, N)
	x_hex = hex(x)
	x_hex = x_hex[2 : len(x_hex)]
	x_hex = "0" + x_hex
	
	CT_bytearray = bytearray.fromhex(x_hex)
	
	print(CT_bytearray)W
	