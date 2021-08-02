import gmpy2
import math
    
f = open("n_2.txt", "+r")
N = int(f.read())
f.close()

A = gmpy2.isqrt(N)
A += 1
	
while True:

	x = gmpy2.isqrt(A * A - N)
	
	p = A - x
	A += 1
		
	if (N % p) != 0:
	
		continue
		
	q = A + x
	
	print("p = " + str(p))
	print("q = " + str(q))
		
	if p < q:
		
		print("p is smaller")
			
	else:
			
		print("q is smaller")
		
	break