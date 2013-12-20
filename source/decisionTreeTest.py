import numpy as np
import csv as csv
from sklearn import tree

# sex, age, siblings

X = [
	[1, 20, 1], 
	[0, 10, 0], 
	[0, 5, 0], 
	[1, 8, 2],
	[1, 15, 0], 
	[1, 5, 0], 
	[0, 25, 0]]

Y = [1, 
	1, 
	0, 
	0,
	1, 
	1, 
	0]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

malePersonOne = [0, 80, 0]
print clf.predict([ malePersonOne ])[0]