import numpy as np
import csv as csv
from sklearn import tree

# sex, age, siblings

X = [
	[1, 20, 1], 
	[0, 10, 0], 
	[0, 10, 0], 
	[1, 8, 2]]

Y = [1, 
	1, 
	0, 
	0]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

malePersonOne = [1, 20, 0]
print clf.predict([ malePersonOne ])[0]






# read in from csv file
csv_file_object = csv.reader(open('train.csv', 'rb')) # Load in the training csv file
header = csv_file_object.next() # Skip the fist line as it is a header
train_data=[] # Create a variable called 'train_data'
for row in csv_file_object: # Skip through each row in the csv file
    train_data.append(row[1:]) # adding each row to the data variable
    # print row[1:]
train_data = np.array(train_data) #Then convert from a list to an array

# build our X from it
