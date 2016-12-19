from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.ensemble import RandomForestClassifier as RFC
import numpy as np

numbers = []
test = []

#Populate the training array
with open('primes.txt') as f:
	for x in f.readlines():
		for a in x.split(' '):
			if a != '' and a != '\n':
				numbers.append(int(a))

#Populate test case array
with open('test.txt') as f:
	for x in f.readlines():
		for a in x.split(' '):
			if a != '' and a != '\n':
				test.append(int(a))
X = []
y = []
for a in range(0, 7120):
	X.append([a])
	y.append(a in numbers)
	a += 2

#Train Decision Tree Classifier (DTC) and Random Forest Classifier (RFC)
dtc = DTC()
dtc = dtc.fit(X, y)

rfc = RFC()
rfc = rfc.fit(X, y)

#Define accuracy vars
correct = [0, 0]
incorrect = [0, 0]
a = 8000       #Some starting point
limit = 9000   #Some ending point
while a < limit:
	dtcp = dtc.predict(a)[0]
	rfcp = rfc.predict(a)[0]
	#for some reason just comparing the two booleans wasn't working, so I had to make it two separate conditionals
	if dtcp:
		if a in numbers:
			correct[0] += 1
		else:
			incorrect[0] += 1
	else:
		if a not in numbers:
			correct[0] += 1
		else:
			incorrect[0] += 1
	if rfcp:
		if a in numbers:
			correct[1] += 1
		else:
			incorrect[1] += 1
	else:
		if a not in numbers:
			correct[1] += 1
		else:
			incorrect[1] += 1
	a += 1
	if(a % 2 == 0):
		a += 1
print "DTC Accuracy: " + str(100*correct[0]/(correct[0] + incorrect[0]))+"%"
print "RFC Accuracy: " + str(100*correct[1]/(correct[1] + incorrect[1]))+"%"