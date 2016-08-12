from math import *

def euclidean_dist(x,y):
	return sum(abs(a - b) for a, b in zip(x, y))


print euclidean_dist([1,1], [2,2])
print euclidean_dist([0,3,4,5],[7,6,3,-1])