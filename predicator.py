import numpy as np
import matplotlib.pyplot as plt
import sys
import tkinter
import matplotlib
matplotlib.use('TkAgg')

t0 = 8487.802590428824
t1 = -0.021356199213165873

def estimatePrice(x):
	return t0 + (t1 * x)

def predicate(X):
	Y_pred = np.array([], dtype=np.float64)
	for x in X:
		Y_pred = np.append(Y_pred, (t1 * x) + t0)
	return (Y_pred)

def drawGraph(X, Y_pred):
	f = plt.figure('estimated price')
	plt.scatter(X, Y_pred, color="red")
	plt.grid(True)
	plt.plot(X, Y_pred)
	plt.show()


def printPreds(X, Y_pred):
	for i in range(len(X)):
		print("Km: {}: price: {}".format(X[i], Y_pred[i]))

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
	drawGraph(X, Y_pred)

main()
