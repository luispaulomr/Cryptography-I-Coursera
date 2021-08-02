import gmpy2

f = open("n_3.txt", "+r")
N = int(f.read())
f.close()

d, r = gmpy2.isqrt_rem(6 * N)
A = d + 1 if r > 0 else 0

# M = (3p + 2q) / 2
# 3p = M + i - 0.5 = A + i - 1
# 2q = M - i + 0.5 = A - i

# i ^ 2 - i = A ^ 2 - A - 6
# 6N = A^2 - i^2 - A + i
# i^2 - i + A^2 - A - 6N
    
a = 1
b = -1
c = -((A**2) - A - (6 * N))

roots = [gmpy2.div(-b - gmpy2.isqrt(b**2 - 4*a*c), 2*a),
	gmpy2.div(-b + gmpy2.isqrt(b**2 - 4*a*c), 2*a)]

for root in roots:
	p = gmpy2.div(A + root - 1, 3)
	q = gmpy2.div(A - root, 2)

	if gmpy2.mul(p, q) == N:
		min_factor = min(p, q)
		print(min_factor)