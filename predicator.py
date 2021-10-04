import numpy as np
import matplotlib.pyplot as plt
import sys
import tkinter
import matplotlib
matplotlib.use('TkAgg')

t0 = 0.6032888905708175
t1 = -0.002052359791241146

def estimatePrice(x):
	return t0 + (t1 * x)

def predicate(X):
	Y_pred = np.array([])
	for x in X:
		Y_pred = np.append(Y_pred, estimatePrice(x))
	return (Y_pred)

def drawGraph(X, Y_pred):
	f = plt.figure('estimated price')
	plt.scatter(X, Y_pred)
	plt.grid(True)
	plt.plot(X, Y_pred)
	plt.show()

def main():
	args = sys.argv[1:]
	X = np.array([])
	if len(args) == 0:
		print('Usage: python3 predicator.py <Miles(Km) 1> ... <Miles (km) 2>')
		exit(0)
	for el in args:
		if el.isnumeric() == False:
			print('Error: unreconized parameter: {}, only numeric values are accepted'.format(el), file=sys.stderr, flush=True)
			exit(1)
		X = np.append(X, int(el))
	print('Sample: ', X)
	Y_pred = predicate(X)
	drawGraph(X, Y_pred)


main()
