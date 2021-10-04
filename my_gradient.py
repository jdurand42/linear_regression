import numpy as np
import matplotlib.pyplot as plt
import sys
import tkinter
import matplotlib
matplotlib.use('TkAgg')

def parser():
	try:
		file = open('./data.csv')
		tab = [[], []]
		file.readline() # throwing first line
		i = 1
		for line in file.readlines():
			b = line.split(",")
			i += 1
			if len(b) != 2 or b[0].isnumeric() == False or b[1][:-1].isnumeric() == False:
				print("Data file invalid: line: ", i, file=os.stderr, flush=True)
				exit(1)
			tab[0].append(int(b[0]))
			tab[1].append(int(b[1][:-1]))
		file.close()
	except:
		print('Data file not found, or invalid', file=sys.stderr, flush=True)
		exit(1)

	print('Data are parsed: Here they are: ')
	for i in range(0, len(tab[0])):
		print("x: {}; y: {}".format(tab[0][i], tab[1][i]))
	return tab

def openPredicator():
	try:
		file = open('./predicator.py', 'r+')
	except:
		print('Predicator file not found, or invalid', file=sys.stderr, flush=True)
		exit(1)
	return file


# for large data sets, due to overflow, the matrix are divided by a divisor
# by default it's 10000
# when writing the thetas in predicator.py, t0 is multiplied by the divisor to
# rescale the graph

# Protype: X, Y : Matrix
# fileOpener: a fonction if you need to update the thetas in a predicator file
# you have to write the fonction with the right name and error print
# put anything else if you don't want to use it
# div: A divisor to divide the sets to prevent overflow in large numbers
# learningRate: learningRate (alpha)
class Linear_Regression():
	def __init__(self, X, Y, fileOpener, div = 1, learningRate = 0.01):
		self.t = np.array([0, 0], dtype=np.float64)
		self.l = learningRate
		self.divisor = div
		self.X = X
		self.Y = Y
		self.fileOpener = fileOpener

	def predict(self):
		if len(X) == 0:
			pass
		Y_pred = np.array([], dtype=np.float64)
		for x in X:
			Y_pred = np.append(Y_pred, self.t[1] * x + self.t[0])
		return Y_pred

	def update_thetas(self):
		Y_pred = self.predict()
		m = len(self.X)
		self.t[0] = self.t[0] - (self.l * ((1/m) * (np.sum(Y_pred - self.Y))))
		self.t[1] = self.t[1] - (self.l * ((1/m) * (np.sum((Y_pred - self.Y) * self.X))))

	def getAccuracy(self):
		#if Y_pred == None:
		Y_pred = self.predict()
		m = len(Y_pred)
		b = np.array([], dtype=np.float64)
		for i in range(len(Y_pred)):
			if self.Y[i] != 0:
				b = np.append(b, abs(Y_pred[i] - self.Y[i]) / self.Y[i])
		return ((1 - np.sum(b)) / m)

	def getCost(self, Y_pred = np.array([])):
		m = len(self.X)
		if Y_pred == np.array([], dtype=np.float64):
			Y_pred = self.predict()
		j = (1 / 2 * m) * (np.sum(Y_pred - self.Y)**2)
		return j

	def plot_best_fit(self, fig = 'Best fit'):
		Y_pred = self.predict()
		f = plt.figure(fig)
		f.clear()
		plt.plot(self.X * self.divisor, Y_pred * self.divisor, color="red")
		plt.scatter(self.X * self.divisor, self.Y * self.divisor)
		#plt.plot(self.X, Y_pred, color="red")
		#plt.scatter(self.X, self.Y)
		f.show()

	def cleanExit(self, file):
		print('Error: could not write thetas into predicator file', file=sys.stderr, flush=True)
		file.closeFile()
		exit(1)

	def updateProgram(self):
		try:
			file = self.fileOpener()
		except:
			return
		data = file.read()
		iT0 = data.find("t0 =")
		if iT0 == -1:
			self.cleanExit(file)
		data = data.replace(data[iT0:data.find("\n", iT0)], 't0 = {}'.format(self.t[0] * self.divisor), 1)
		iT1 = data.find("t1 =")
		if iT1 == -1:
			self.cleanExit(file)
		data = data.replace(data[iT1:data.find("\n", iT1)], 't1 = {}'.format(self.t[1]), 1)
		print(self.t[0], self.t[1])
		file.seek(0)
		file.write(data)
		file.truncate()
		file.close()

div = 10000
b = parser()
file = openPredicator()
X = np.array(b[0], dtype=np.float64) / 10000
Y = np.array(b[1], dtype=np.float64) / 10000

steps = 100
epochs = 0
regression = Linear_Regression(X, Y, openPredicator, div)
Y_pred = regression.predict()
while 1:
	Y_pred = regression.predict()
	regression.update_thetas()
	epochs += 1
	if epochs % steps == 0:
		print('Epochs ellapsed: ', epochs)
		regression.plot_best_fit('Best fit')
		accuracy = regression.getAccuracy()
		regression.updateProgram()
		print('Accuracy is: ', accuracy)
		choice = input("Do you wish to quit? (y)/(n)?")
		if choice == 'y':
			break
