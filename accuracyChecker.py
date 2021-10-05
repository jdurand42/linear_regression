import numpy as np
import matplotlib.pyplot as plt
import sys
import tkinter
import matplotlib
from commons import *
matplotlib.use('TkAgg')

def drawAccGraph(X, Y, Y_pred, acc):
	f = plt.figure("Accuracy: {}".format(acc))
	plt.grid(True)
	plt.plot(X, Y_pred)
	plt.scatter(X, Y_pred, color="blue")
	plt.scatter(X, Y, color='green')
	for i in range(len(Y)):
		plt.plot([X[i], X[i]], [Y[i], Y_pred[i]], color="red")
	plt.show()

def getAccuracy(Y, Y_pred):
		#if Y_pred == None:
	m = len(Y_pred)
	b = np.array([], dtype=np.float64)
	for i in range(len(Y_pred)):
		if Y[i] != 0:
			b = np.append(b, abs(Y_pred[i] - Y[i]) / Y[i])
	return (abs((1 - np.sum(b)) / m))

def main():
	print("Formula: (t0 + t1 * X): {} + {} * X".format(t0, t1))
	b = parser()
	X = np.array(b[0], dtype=np.float64)
	Y = np.array(b[1], dtype=np.float64)
	Y_pred = predicate(X)
	acc = getAccuracy(Y, Y_pred)
	print("Accuracy is: {}".format(acc))
	drawAccGraph(X, Y, Y_pred, acc)

main()
