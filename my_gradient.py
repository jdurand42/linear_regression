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


class Linear_Regression():
	def __init__(self, X, Y, file, div = 10000, learningRate = 0.01):
		self.t = [0, 0]
		self.l = learningRate
		self.divisor = div
		self.X = X
		self.Y = Y
		self.file = file

	def predict(self):
		if len(X) == 0:
			pass
		Y_pred = np.array([])
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
		b = np.array([])
		for i in range(len(Y_pred)):
			if self.Y[i] != 0:
				b = np.append(b, abs(Y_pred[i] - self.Y[i]) / self.Y[i])
		return (1 - np.sum(b)) / m

	def getCost(self, Y_pred = np.array([])):
		m = len(self.X)
		if Y_pred == np.array([]):
			Y_pred = self.predict()
		j = (1 / 2 * m) * (np.sum(Y_pred - self.Y)**2)
		return j

	def plot_best_fit(self, fig = 'Best fit'):
		Y_pred = self.predict()
		f = plt.figure(fig)
		f.clear()
		plt.plot(self.X * self.divisor, Y_pred * self.divisor, color="red")
		plt.scatter(self.X * self.divisor, self.Y * self.divisor)
		f.show()

	def updateProgram(self):
		self.file = openPredicator()
		data = self.file.read()
		iT0 = data.find("t0 =")
		if iT0 == -1:
			print('Error: could not write thetas into predicator file', file=sys.stderr, flush=True)
			self.closeFile()
			exit(1)
		data = data.replace(data[iT0:data.find("\n", iT0)], 't0 = {}'.format(self.t[0]), 1)
		iT1 = data.find("t1 =")
		if iT1 == -1:
			print('Error: could not write thetas into predicator file', file=sys.stderr, flush=True)
			self.closeFile()
			exit(1)
		data = data.replace(data[iT1:data.find("\n", iT1)], 't1 = {}'.format(self.t[1]), 1)
		print(self.t[0], self.t[1])
		self.file.seek(0)
		self.file.write(data)
		self.file.truncate()
		self.closeFile()


	def closeFile(self):
		self.file.close()

div = 10000
b = parser()
file = openPredicator()
X = np.array(b[0]) / div
Y = np.array(b[1]) / div

steps = 100
epochs = 0
regression = Linear_Regression(X, Y, file, div)
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
			regression.closeFile()
			break