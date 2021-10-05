# linear_regression
Simple linear regression to predict estimated price of a second hand car
Tested only in WSL2 for now

-> data.csv: Data set with miles(km) and selling price of cars

-> predicator.py:
	python3 predicator.py [Miles1 Miles2 ... MilesN]
		0 <= Miles
	Print estimated price with saved values of theta0 and theta1

-> trainer.py:
	python3 trainer.py
	Train the model and update t0 and t1 every steps of epochs

-> accuracyChecker.py
 	python3 accuracyChecker.py
	Print accuracy, actual and estimated prices of data.csv with saved theta0 and theta1

-> commons.py:
	Commons file where theta0 and theta1 are saved
	contains some fuction usable by all 3 programs

-> trainer_without_gradient.py
	an independant trainer that uses a single formula to find theta0 and theta1
	does not update thetas in commons
