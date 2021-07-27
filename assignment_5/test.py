import gmpy2
from random import randrange
from bisect import bisect_left
  
def BinarySearch(a, x):
	i = bisect_left(a, x)
	if i != len(a) and a[i] == x:
		return i
	else:
		return -1
    
B = pow(2, 20)
x0 = 0
x1 = 0
f = open("p.txt", "+r")
p = int(f.read())
f.close()

f = open("g.txt", "+r")
g = int(f.read())
f.close()

f = open("h.txt", "+r")
h = int(f.read())
f.close()

table = [0] * (B + 1)

g_inverse = gmpy2.powmod(g, p - 2, p)
g_to_B = gmpy2.powmod(g, B, p)

left = h
table[0] = left

for x in range(1, B + 1):
	
	left = (left * g_inverse) % p
	table[x] = left

print("Constructed table!")

indexes_table = sorted(range(len(table)), key=lambda k: table[k])
table = [table[i] for i in indexes_table]

print("Sorted list!")

right = 1

for x in range(0, B + 1):

	i = BinarySearch(table, right)
	
	if i != -1:
	
		print(right)
	
		x1 = indexes_table[i]
		x0 = x
		
		print("x1 = " + str(x1))
		print("x0 = " + str(x0))
		
		break
		
	right = (right * g_to_B)  % p
		
if not x0:
	
	print("Not found")
	
else:

	x = x0 * B + x1

	print("x = " + str(x))
	
	h_calculated = gmpy2.powmod(g, x, p)
	
	if h != h_calculated:
	
		print(h_calculated)
		print(h)
		print("Wrong h!")