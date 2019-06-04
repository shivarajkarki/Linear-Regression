#program to fine prime

import time
import math
def v1(n):
	if n == 1:
		return False
	
	for x in range(2,n):
		if n % x == 0:
			return False
	return True


def v2(n):
	if n == 1:
		return False
	
	limit = 1 + math.floor(math.sqrt(n))
	for x in range(2, limit):
		if n % x == 0:
			return False
	return True
	
def v3(n):
	if n == 1:
		return False
	"""	
	if n > 2 and n % 2 == 0:
		return False
	"""	
		
	limit = 1 + math.floor(math.sqrt(n))
	for x in range(3, limit,2):
		if n % x == 0:
			return False
	return True
	
t0 = time.time()
for i in range(1, 100000):
#	print(i, v2(i))
	if (i % 2 != 0 and v3(i) == True):
		print(i)
t1 = time.time()
print('\n', t1-t0)
