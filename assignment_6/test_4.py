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
	
	#print(hex(gmpy2.powmod(y, d, N)))
	#print(pow(y, d))
	
	#result = bytearray.fromhex(hex(gmpy2.powmod(y, d, N)))
	
	#print(result)
	
	#some_int = gmpy2.powmod(y, d, N)
	#some_int = gmpy2.int()
	#some_bytes = some_int.to_bytes(32, sys.byteorder)
	#my_bytearray = bytearray(some_bytes)
	
	x = gmpy2.powmod(y, d, N)
	x_hex = hex(x)
	x_hex = x_hex[2 : len(x_hex)]
	print(x_hex)
	x_hex = "0" + x_hex
	print(x_hex)
	
	#print(x_hex[253])
	
	CT_bytearray = bytearray.fromhex(x_hex)
	
	print(CT_bytearray)
	
	for byte in CT_bytearray:
	
		#print(byte)
		if byte == 0:
		
			print("LUL")
	
	#print(binascii.unhexlify(hex(x)[2:]))
	
	#print(CT_bytearray)
	