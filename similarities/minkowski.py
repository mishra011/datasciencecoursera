from math import *
from decimal import Decimal

def nth_root(value, n_root):
	root_value = 1/ float(n_root)
	return round(Decimal(value) ** Decimal(root_value))


def minkowski_dist(x,y,p_value):
	return nth_root(sum(pow(abs(a-b),p_value) for a, b in zip(x,y)), p_value)

print minkowski_dist([0,3,4,5],[7, 6,3,-1], 3)