#%%
import sys
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

learningRate = 1

def mean(set):
	if len(set) == 0:
		return 0
	return sum(set) / len(set)

def getScalar(x, y):
	p = []
	for i in range(0, len(x)):
		p.append(x[i] * y[i])
	print(p)
	return p

def getSquared(b):
	p = []
	for i in range(0, len(b)):
		p.append(b[i] ** 2)
	return p

def estimatedPrice(x, a, b):
	return (x * a) + b

def getB(set, tmpA, tmpB):
	res = 0
	for i in range(0, len(set)):
		res += (estimatedPrice(set[i][0], tmpA, tmpB) - set[i][1])
		print(res)
	return learningRate * res / len(set)

def getA(set, tmpA, tmpB):
	res = 0
	for i in range(0, len(set)):
		res += ((tmpB - set[i][1]) * set[i][0])
	return learningRate * res / len(set)

def getSlope(x, y):
	slope = (mean(x) * mean(y) - mean(getScalar(x, y))) / (mean(x) ** 2 - mean(getSquared(x)))
	# slope = (len(x) * sum(getScalar(x, y)) - sum(x) * sum(y)) / (len(x) * sum(getSquared(x)) - (sum(x) ** 2))
	return slope

def getYInt(x, y, slope):
	yInt = mean(y) - slope * mean(x)
	# yInt = (sum(y) * sum(getSquared(x)) - (sum(x) * sum(getScalar(x, y)))) / (len(x) * sum(getSquared(x)) - (sum(x) ** 2))
	return yInt

def printPred(set, a, b):
	for i in range(0, len(set)):
		print("x: {}; y: {}, estimated: {}".format(set[i][0], set[i][1], estimatedPrice(set[i][0], a, b)))

def getAB(set, tmpA, tmpB):
	b = getB(tab, tmpA, tmpB)
	a = getA(tab, tmpA, b)

	print("a: {}, b: {}, learningRate: {}".format(a, b, learningRate))
	return (a, b)

try:
	file = open('./data.csv')
	tab = []
	file.readline() # throwing first line
	i = 1
	for line in file.readlines():
		b = line.split(",")
		t = []
		i += 1
		if len(b) != 2 or b[0].isnumeric() == False or b[1][:-1].isnumeric() == False:
			print("Data file invalid: line: ", i, file=os.stderr, flush=True)
			exit(1)
		tab.append([int(b[0]), int(b[1][:-1])])
	file.close()
except:
	print('Data file not found, or invalid', file=os.stderr, flush=True)
	exit(1)

print('Data are parsed: Here they are: ')
x = []
y = []
for i in range(0, len(tab)):
	print("x: {}; y: {}".format(tab[i][0], tab[i][1]))
	x.append(tab[i][0])
	y.append(tab[i][1])


plt.plot(x, y, 'ro')
slope = getSlope(x, y)
yInt = getYInt(x, y, slope)

print("slope: {}, yInt: {}".format(slope, yInt))
count = 100
# thetas = getAB(tab, 0, 0)
#print(thetas[0])
#a = getFirstA(tab)
printPred(tab, slope, yInt)

plt.plot([0, 260000], [0 * slope + yInt, 260000 * slope + yInt])
plt.xlabel('Miles (Km)')
plt.ylabel('Price')
plt.show()
