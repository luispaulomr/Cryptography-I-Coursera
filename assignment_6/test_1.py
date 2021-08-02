import gmpy2
import math
    
f = open("n_1.txt", "+r")
N = int(f.read())
f.close()

A = gmpy2.isqrt(N)
A += 1
	
x = gmpy2.isqrt(A * A - N)
	
p = A - x	
q = A + x
	
if N - p * q == 0:
	
	print("p = " + str(p))
	print("q = " + str(q))
		
	if p < q:
		
		print("p is smaller")
			
	else:
			
		print("q is smaller")