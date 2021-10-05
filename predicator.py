import numpy as np
import matplotlib.pyplot as plt
import sys
import tkinter
import matplotlib
from commons import *
matplotlib.use('TkAgg')

#t0 = 8329.012623961815
#t1 = -0.02010757852496406

def main():
	args = sys.argv[1:]
	x = []
	X = np.array([], dtype=np.float64)
	if len(args) == 0:
		print('Usage: python3 predicator.py <Miles(Km) 1> ... <Miles (km) 2>')
		exit(0)
	for el in args:
		if el.isnumeric() == False:
			print('Error: unreconized parameter: {}, only numeric values are accepted'.format(el), file=sys.stderr, flush=True)
			exit(1)
		x.append(int(el))
		X = np.append(X, int(el))
	# print('Sample: ', X)
	Y_pred = predicate(X)
	print(Y_pred)
	printPreds(x, Y_pred)
	drawGraph(X, Y_pred, 'Prediction of estimated price')

main()
