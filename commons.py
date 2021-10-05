import numpy as np
import matplotlib.pyplot as plt
import sys
import tkinter
import matplotlib
matplotlib.use('TkAgg')

t0 = 8497.743651469735
t1 = -0.021434369230796915

def predicate(X):
	Y_pred = np.array([], dtype=np.float64)
	for x in X:
		Y_pred = np.append(Y_pred, (t1 * x) + t0)
	return (Y_pred)

def drawGraph(X, Y, legend):
	f = plt.figure(legend)
	plt.scatter(X, Y, color="red")
	plt.grid(True)
	plt.plot(X, Y)
	plt.show()

def printPreds(X, Y_pred):
	for i in range(len(X)):
		print("Km: {}: price: {}".format(X[i], Y_pred[i]))

def parser():
	try:
		file = open('./data.csv')
		tab = [[], []]
		file.readline() # throwing first line
		i = 1
		for line in file.readlines():
			b = line.split(",")
			i += 1
			if len(b) != 2 or b[0].isnumeric() == False or b[1][:-1].isnumeric() == False or int(b[0]) < 0 or int(b[1][:-1]) < 0:
				print("Data file invalid: line: ", i," | only numeric positive values", file=os.stderr, flush=True)
				exit(1)
			tab[0].append(int(b[0]))
			tab[1].append(int(b[1][:-1]))
		file.close()
	except:
		print('Data file not found, or invalid', file=sys.stderr, flush=True)
		sys.exit(1)

	print('Data are parsed: Here they are: ')
	for i in range(0, len(tab[0])):
		print("x: {}; y: {}".format(tab[0][i], tab[1][i]))
	return tab
